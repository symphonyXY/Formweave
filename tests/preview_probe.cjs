// 运行方法见 docs/validation.md。使用实际浏览器验证独立 HTML。
const { chromium } = require('playwright');
const assert = require('node:assert/strict');
const path = require('node:path');
const { pathToFileURL } = require('node:url');

async function probe(executablePath, screenshot) {
  const browser = await chromium.launch({ executablePath, headless: true });
  try {
    const page = await browser.newPage({ viewport: { width: 1180, height: 780 } });
    const errors = [];
    page.on('pageerror', error => errors.push(error.message));
    const preview = path.resolve(__dirname, '../skills/formweave-preview/assets/inventory-preview.html');
    await page.goto(pathToFileURL(preview).href);
    const rows = page.locator('tbody tr');
    const boxes = rows.getByRole('checkbox');
    const filter = name => page.getByRole('button', { name, exact: true }).click();
    const focused = selector => page.locator(selector).evaluate(e => e === document.activeElement);
    assert.equal(await rows.count(), 72);
    for (const [label, count] of [['有差异', 54], ['相符', 18], ['全部', 72]]) {
      await filter(label);
      assert.equal(await rows.count(), count);
    }
    const footerTop = await page.locator('footer').evaluate(e => e.getBoundingClientRect().top);
    await page.locator('#query').fill('无此物料');
    assert.equal(await page.locator('footer').evaluate(e => e.getBoundingClientRect().top), footerTop);
    assert.equal(await rows.count(), 0);
    assert.ok(await page.locator('#empty').isVisible());
    await page.locator('#clear').click();
    assert.ok(await focused('#query'));
    await page.locator('#density').click();
    assert.equal(await page.locator('#density').getAttribute('aria-pressed'), 'true');
    await page.locator('#density').click();
    await filter('有差异');
    await page.locator('#all').focus();
    await page.keyboard.press('Tab');
    assert.ok(await focused('tbody tr.current input'));
    for (const key of ['Space', 'ArrowDown', 'Space', 'ArrowDown', 'ArrowUp']) {
      await page.keyboard.press(key);
    }
    assert.match(await page.locator('#detail').innerText(), /P-2002[\s\S]*盘盈 2/);
    assert.match(await page.locator('#selection').innerText(), /2 项/);
    await page.keyboard.press('Tab');
    assert.ok(await focused('summary'));
    await page.keyboard.press('Shift+Tab');
    if (screenshot) await page.screenshot({ path: screenshot });
    await page.keyboard.press('Control+Enter');
    await page.keyboard.press('Escape');
    assert.match(await page.locator('#receipt').innerText(), /已取消，完成 \d+\/2/);
    assert.ok(await focused('tbody tr.current input'));
    await page.locator('#start').click();
    await filter('相符');
    await page.waitForFunction(() => document.querySelector('#receipt').textContent === '已完成 2 项，有差异 2 项');
    assert.equal(await page.locator('#start').isDisabled(), true);
    await page.setViewportSize({ width: 390, height: 700 });
    assert.ok(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth));
    assert.equal(await page.locator('details').getAttribute('open'), null);
    await page.locator('summary').click();
    await page.emulateMedia({ reducedMotion: 'reduce' });
    await boxes.nth(2).focus();
    assert.equal(await page.locator('#detail').evaluate(e => e.getAnimations().length), 0);
    await page.locator('#all').check();
    assert.match(await page.locator('#selection').innerText(), /18 项/);
    await page.locator('#start').click();
    await page.waitForFunction(() => document.querySelector('progress').value >= 1);
    await page.locator('#cancel').click();
    const partial = (await page.locator('#receipt').innerText()).match(/已取消，完成 (\d+)\/18/);
    assert.ok(partial && Number(partial[1]) > 0 && Number(partial[1]) < 18);
    assert.deepEqual(errors, []);
    console.log('通过：筛选、空结果、键盘查看与多选、模拟校验/取消、范围快照、窄窗、紧凑视图和减少动效');
  } finally {
    await browser.close();
  }
}

probe(process.argv[2], process.argv[3]).catch(error => { console.error(error); process.exitCode = 1; });
