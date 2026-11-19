const { chromium } = require('playwright');
const assert = require('node:assert/strict');
const path = require('node:path');
const { pathToFileURL } = require('node:url');

async function probe(executablePath, screenshotPrefix) {
  const browser = await chromium.launch({ executablePath, headless: true });
  try {
    const page = await browser.newPage({ viewport: { width: 1180, height: 780 }, offline: true });
    const exceptions = [];
    const network = [];
    page.on('pageerror', error => exceptions.push(error.message));
    page.on('request', request => {
      if (/^https?:/.test(request.url())) network.push(request.url());
    });
    const preview = path.resolve(__dirname, '../skills/formweave-preview/assets/visual-motion-preview.html');
    await page.goto(pathToFileURL(preview).href);
    const cards = page.getByRole('group', { name: '素材卡片' }).getByRole('button');
    const title = page.locator('#asset-name');
    const receipt = page.getByRole('status');
    const grid = page.getByRole('button', { name: '网格', exact: true });
    const compact = page.getByRole('button', { name: '紧凑', exact: true });
    const material = page.getByRole('tab', { name: '材质' });
    const overview = page.getByRole('tab', { name: '概览' });
    const reduce = page.locator('#reduce');
    const settleCards = () => page.waitForFunction(() =>
      [...document.querySelectorAll('.card')].every(card => card.getAnimations().length === 0));

    assert.equal(await cards.count(), 3);
    assert.equal(await title.innerText(), '环形光谱');
    await cards.nth(1).hover();
    assert.equal(await title.innerText(), '折面试样');
    assert.match(await receipt.innerText(), /已选中：环形光谱/);
    await cards.nth(2).hover();
    assert.equal(await title.innerText(), '轨迹研究');
    await page.locator('h1').hover();
    assert.equal(await title.innerText(), '环形光谱');
    await grid.focus();
    await page.keyboard.press('Tab');
    assert.ok(await overview.evaluate(tab => tab === document.activeElement));
    await page.keyboard.press('Tab');
    await page.keyboard.press('Tab');
    assert.ok(await cards.nth(1).evaluate(card => card === document.activeElement));
    assert.equal(await title.innerText(), '折面试样');
    await page.keyboard.press('Enter');
    assert.match(await receipt.innerText(), /已选中：折面试样/);
    assert.equal(await cards.nth(1).getAttribute('aria-pressed'), 'true');
    await page.keyboard.press('Tab');
    assert.equal(await title.innerText(), '轨迹研究');
    await page.keyboard.press('Escape');
    assert.equal(await title.innerText(), '折面试样');

    const stage = page.locator('.stage');
    const beforeTab = await stage.boundingBox();
    await overview.focus();
    await page.keyboard.press('ArrowRight');
    assert.ok(await material.evaluate(tab => tab === document.activeElement));
    assert.equal(await material.getAttribute('aria-selected'), 'true');
    assert.ok(await page.getByRole('tabpanel', { name: '材质' }).isVisible());
    assert.deepEqual(await stage.boundingBox(), beforeTab);
    await page.keyboard.press('ArrowLeft');
    assert.equal(await overview.getAttribute('aria-selected'), 'true');
    assert.equal(await page.getByRole('tabpanel').count(), 1);

    await grid.click();
    await settleCards();
    assert.equal(await grid.getAttribute('aria-pressed'), 'true');
    const gridEnd = await cards.first().boundingBox();
    await compact.click();
    await settleCards();
    const compactEnd = await cards.first().boundingBox();
    assert.ok(gridEnd.width - compactEnd.width > 60 && compactEnd.x - gridEnd.x > 80);

    await cards.nth(1).focus();
    const reversal = await page.evaluate(() => {
      const card = document.querySelector('.card');
      const shot = element => {
        const { x, y, width, height } = element.getBoundingClientRect();
        return { x, y, width, height };
      };
      const toolbar = document.querySelector('.section-bar');
      const anchor = shot(toolbar);
      const focus = document.activeElement;
      document.querySelector('[data-view-choice="grid"]').click();
      const outgoing = card.getAnimations()[0];
      outgoing.pause();
      outgoing.currentTime = 85;
      const intermediate = shot(card);
      document.querySelector('[data-view-choice="compact"]').click();
      const incoming = card.getAnimations()[0];
      incoming.pause();
      incoming.currentTime = 0;
      const from = shot(card);
      incoming.currentTime = 110;
      const toward = shot(card);
      document.querySelector('[data-view-choice="grid"]').click();
      const latest = card.getAnimations()[0];
      latest.pause();
      latest.currentTime = 0;
      const repeat = shot(card);
      document.querySelectorAll('.card').forEach(item =>
        item.getAnimations().forEach(animation => animation.finish()));
      return { intermediate, from, toward, repeat, after: shot(card), anchor,
        toolbar: shot(toolbar), sameFocus: focus === document.activeElement,
        priorCancelled: outgoing.playState === 'idle' && incoming.playState === 'idle' };
    });
    assert.ok(reversal.intermediate.width > compactEnd.width + 5 && reversal.intermediate.width < gridEnd.width - 5);
    assert.ok(reversal.toward.x > reversal.from.x && reversal.toward.width < reversal.from.width);
    for (const axis of ['x', 'y', 'width', 'height']) {
      assert.ok(Math.abs(reversal.from[axis] - reversal.intermediate[axis]) <= 1, `第一次改向跳位：${axis}`);
      assert.ok(Math.abs(reversal.repeat[axis] - reversal.toward[axis]) <= 1, `第二次改向跳位：${axis}`);
      assert.ok(Math.abs(reversal.after[axis] - gridEnd[axis]) <= 1, `最终位置错误：${axis}`);
    }
    assert.deepEqual(reversal.toolbar, reversal.anchor);
    assert.ok(reversal.sameFocus && reversal.priorCancelled);
    assert.equal(await cards.count(), 3);
    assert.equal(await cards.nth(1).getAttribute('aria-pressed'), 'true');

    await compact.click();
    await settleCards();
    const themeBefore = await stage.boundingBox();
    const foregroundBefore = await title.evaluate(element => getComputedStyle(element).color);
    if (screenshotPrefix) {
      await reduce.click();
      await page.locator('h1').click();
      await page.screenshot({ path: `${screenshotPrefix}-dark.png` });
    }
    await page.getByRole('button', { name: '浅色', exact: true }).click();
    assert.deepEqual(await stage.boundingBox(), themeBefore);
    assert.notEqual(await title.evaluate(element => getComputedStyle(element).color), foregroundBefore);
    assert.equal(await cards.nth(1).getAttribute('aria-pressed'), 'true');
    if (screenshotPrefix) {
      await page.locator('h1').click();
      await page.screenshot({ path: `${screenshotPrefix}-light.png` });
      await reduce.click();
    }

    const cancelledByPreference = await page.evaluate(() => {
      const first = document.querySelector('.card');
      document.querySelector('[data-view-choice="grid"]').click();
      const started = first.getAnimations().length > 0;
      document.querySelector('#reduce').click();
      return started && first.getAnimations().length === 0;
    });
    assert.ok(cancelledByPreference);
    assert.equal(await reduce.getAttribute('aria-pressed'), 'true');
    assert.equal(await grid.getAttribute('aria-pressed'), 'true');
    await material.click();
    assert.equal(await page.evaluate(() => document.getAnimations().length), 0);
    assert.equal(await material.getAttribute('aria-selected'), 'true');
    await reduce.click();
    await page.emulateMedia({ reducedMotion: 'reduce' });
    await page.waitForFunction(() => document.querySelector('#reduce').disabled);
    await compact.click();
    assert.equal(await page.evaluate(() => document.getAnimations().length), 0);
    assert.equal(await compact.getAttribute('aria-pressed'), 'true');

    await page.emulateMedia({ reducedMotion: 'no-preference' });
    await page.waitForFunction(() => !document.querySelector('#reduce').disabled);
    for (const width of [590, 390]) {
      await page.setViewportSize({ width, height: 700 });
      await grid.click();
      assert.ok(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth));
      assert.equal(await page.locator('#dock').evaluate(element => element.getAnimations({ subtree: true }).length), 0);
      assert.equal(await cards.count(), 3);
      assert.ok((await cards.last().boundingBox()).width > 0);
      await compact.click();
      assert.ok(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth));
    }
    await page.emulateMedia({ forcedColors: 'active' });
    assert.equal(await page.locator('.ambient').evaluate(element => getComputedStyle(element).display), 'none');
    assert.equal(await cards.nth(1).getAttribute('aria-pressed'), 'true');
    assert.deepEqual(network, []);
    assert.deepEqual(exceptions, []);
    console.log('通过：深浅材质、悬停与键盘、局部标签、两次中途反向、焦点与选中、减少动效、窄窗、强制颜色与离线');
  } finally {
    await browser.close();
  }
}

probe(process.argv[2], process.argv[3]).catch(error => { console.error(error); process.exitCode = 1; });
