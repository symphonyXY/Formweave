// 运行方式见 docs/validation.md；Playwright 使用本机 Chromium 浏览器。
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
    assert.equal(await rows.count(), 72);
    for (const [label, count] of [['有差异',54], ['相符',18], ['全部',72]]) {
      await page.getByRole('button', { name: label, exact: true }).click();
      assert.equal(await rows.count(), count);
    }
    // 不让自动化框架等待动效完成，验证快速操作只呈现最新记录。
    await page.locator('.select').evaluateAll(buttons => {
      for (const index of [1, 3, 1]) buttons[index].click();
    });
    assert.match(await page.locator('#detail').innerText(), /P-2002[\s\S]*盘盈 2/);
    await page.locator('#query').fill('无此物料');
    assert.equal(await rows.count(), 0);
    assert.ok(await page.locator('#empty').isVisible());
    await page.locator('#clear').click();
    assert.equal(await rows.count(), 72);
    assert.ok(await page.locator('#query').evaluate(e => e === document.activeElement));
    await page.locator('#density').click();
    assert.equal(await page.locator('#density').getAttribute('aria-pressed'), 'true');
    await page.locator('#density').click();
    await page.locator('.select').nth(1).focus();
    await page.keyboard.press('Enter');
    await page.waitForFunction(() => !document.getElementById('detail').getAnimations().length);
    assert.match(await page.locator('#detail').innerText(), /P-2002/);
    if (screenshot) await page.screenshot({ path: screenshot });
    await page.setViewportSize({ width: 390, height: 700 });
    assert.ok(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth));
    await page.emulateMedia({ reducedMotion: 'reduce' });
    await page.locator('.select').nth(2).click();
    assert.equal(await page.locator('#detail').evaluate(e => e.getAnimations().length), 0);
    assert.deepEqual(errors, []);
    console.log('通过：筛选、快速切换、清除、键盘、紧凑视图、窄屏与减少动效');
  } finally {
    await browser.close();
  }
}

probe(process.argv[2], process.argv[3]).catch(error => { console.error(error); process.exitCode = 1; });
