// 本地测试专用 CDP 端口；产品启动命令不启用调试。
const fs = require('node:fs');
const os = require('node:os');
const path = require('node:path');
const { spawn, execFileSync } = require('node:child_process');
const { setTimeout: sleep } = require('node:timers/promises');

async function until(read, label) {
  const end = Date.now() + 12000;
  while (Date.now() < end) {
    const value = await read();
    if (value) return value;
    await sleep(80);
  }
  throw new Error(label);
}

async function run(exe) {
  const profile = fs.mkdtempSync(path.join(os.tmpdir(), 'formweave-electron-probe-'));
  const child = spawn(exe, ['--remote-debugging-port=0', '--remote-debugging-address=127.0.0.1',
    '--user-data-dir=' + profile], { stdio: 'ignore' });
  let socket;
  try {
    const portFile = path.join(profile, 'DevToolsActivePort');
    const port = await until(() => fs.existsSync(portFile) &&
      fs.readFileSync(portFile, 'utf8').split('\n')[0], '未获得测试端口');
    const target = await until(async () => (await (await fetch('http://127.0.0.1:' + port + '/json/list')).json())
      .find(row => row.type === 'page' && row.url.endsWith('index.html')), '未找到本地窗口');
    socket = new WebSocket(target.webSocketDebuggerUrl);
    await new Promise((resolve, reject) => { socket.onopen = resolve; socket.onerror = reject; });
    let id = 0;
    async function command(method, params = {}) {
      const key = ++id;
      return new Promise((resolve, reject) => {
        const timeout = setTimeout(() => reject(new Error('CDP 超时')), 4000);
        const listen = event => {
          const msg = JSON.parse(event.data);
          if (msg.id !== key) return;
          clearTimeout(timeout);
          socket.removeEventListener('message', listen);
          if (msg.error || msg.result.exceptionDetails) reject(new Error(method + ' ' + JSON.stringify(msg.error || msg.result.exceptionDetails)));
          else resolve(msg.result);
        };
        socket.addEventListener('message', listen);
        socket.send(JSON.stringify({ id: key, method, params }));
      });
    }
    async function evaluate(expression) {
      const reply = await command('Runtime.evaluate', { expression, returnByValue: true });
      return reply.result.value;
    }
    await until(async () => await evaluate("document.readyState === 'complete' && !!document.getElementById('open')"),
      '页面未就绪');
    for (const select of [true, false]) {
      await evaluate("document.getElementById('open').click()");
      await sleep(200);
      if (await evaluate("document.getElementById('status').textContent.includes('失败')")) {
        throw new Error('文件选择 IPC 失败');
      }
      const args = ['-B', path.join(__dirname, 'dialog.py'), String(child.pid)];
      if (select) args.push(__filename);
      execFileSync('python', args, { windowsHide: true, timeout: 14000 });
      const expected = select ? '已选择：' + path.basename(__filename) : '已取消选择';
      let observed;
      try {
        await until(async () => {
          observed = await evaluate("document.getElementById('status').textContent");
          return observed === expected;
        }, '文件对话框结果未回传到页面');
      } catch (error) {
        throw new Error(error.message + '；期望 ' + expected + '，实际 ' + observed);
      }
      console.log(expected);
      if (select && process.argv[3]) {
        await until(async () => !(await evaluate("document.getElementById('status').getAnimations().length")),
          '回执动效未结束');
        const shot = await command('Page.captureScreenshot', { format: 'png' });
        fs.writeFileSync(process.argv[3], Buffer.from(shot.data, 'base64'));
      }
    }
    await evaluate('setTimeout(() => window.close(), 50)');
    await until(() => child.exitCode !== null, '窗口未退出');
    if (child.exitCode !== 0) throw new Error('应用退出码异常');
  } finally {
    if (socket) socket.close();
    if (child.exitCode === null) child.kill();
    // 仅删除本次创建的唯一配置目录；失败时显示路径以便人工检查。
    if (path.dirname(profile) !== os.tmpdir() || fs.lstatSync(profile).isSymbolicLink()) {
      throw new Error('配置目录边界不符：' + profile);
    }
    fs.rmSync(profile, { recursive: true, force: false, maxRetries: 5, retryDelay: 300 });
  }
}

run(path.resolve(process.argv[2])).catch(error => { console.error(error.message); process.exitCode = 1; });
