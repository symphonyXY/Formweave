const button = document.querySelector('#open');
const status = document.querySelector('#status');
let feedback;
function report(state, text) {
  if (feedback) feedback.cancel();
  status.dataset.state = state;
  status.textContent = text;
  if (!matchMedia('(prefers-reduced-motion: reduce)').matches)
    feedback = status.animate([{opacity: .72}, {opacity: 1}], {duration: 140});
}
button.addEventListener('click', async () => {
  if (button.disabled) return;
  button.disabled = true;
  report('busy', '正在选择文件…');
  try {
    const name = await window.files.pickName();
    report(name === null ? 'cancelled' : 'done', name === null ? '已取消选择' : '已选择：' + name);
  } catch {
    report('error', '打开失败，请重试');
  } finally {
    button.disabled = false;
    button.focus();
  }
});
