const { app, BrowserWindow, dialog, ipcMain } = require('electron');
const path = require('node:path');
const { pathToFileURL } = require('node:url');

const page = path.join(__dirname, 'index.html');
const localURL = pathToFileURL(page).href;

function openWindow() {
  const win = new BrowserWindow({
    title: '织形 · 文件查看器', width: 670, height: 420,
    webPreferences: { preload: path.join(__dirname, 'preload.cjs'),
      sandbox: true, contextIsolation: true, nodeIntegration: false }
  });
  win.webContents.setWindowOpenHandler(() => ({ action: 'deny' }));
  win.webContents.on('will-navigate', event => event.preventDefault());
  return win;
}

async function selectName(win, choose) {
  const result = await choose(win, { properties: ['openFile'] });
  return result.canceled ? null : path.basename(result.filePaths[0]);
}

app.whenReady().then(async () => {
  const win = openWindow();
  ipcMain.handle('pick-name', event => {
    if (event.sender !== win.webContents || event.senderFrame !== win.webContents.mainFrame ||
        event.senderFrame.url !== localURL) throw new Error('来源不匹配');
    return selectName(win, dialog.showOpenDialog);
  });
  await win.loadFile(page);
  if (process.argv.includes('--smoke')) {
    const check = await win.webContents.executeJavaScript(
      "document.querySelector('h1').textContent === '文件查看器' && typeof window.files.pickName === 'function' && typeof require === 'undefined'");
    const picked = await selectName(win, async () => ({ canceled: false, filePaths: [page] }));
    const cancelled = await selectName(win, async () => ({ canceled: true, filePaths: [] }));
    app.exit(check && picked === 'index.html' && cancelled === null ? 0 : 2);
  }
}).catch(error => { console.error(error); app.exit(1); });
app.on('window-all-closed', () => app.quit());
