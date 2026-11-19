document.querySelectorAll('[data-filter]').forEach(button => {
  button.addEventListener('click', () => {
    const chosen = button.dataset.filter;
    document.querySelectorAll('[data-filter]').forEach(b => b.setAttribute('aria-pressed', String(b === button)));
    let count = 0;
    document.querySelectorAll('[data-project-category]').forEach(item => {
      item.hidden = chosen !== 'all' && item.dataset.projectCategory !== chosen;
      if (!item.hidden) count++;
    });
    const counter = document.querySelector('[data-result-count]');
    if (counter) counter.textContent = `${count}개 프로젝트`;
  });
});
document.querySelector('[data-print]')?.addEventListener('click', () => window.print());
// Retain links from the previous single-page portfolio.
const formerCaseIds = new Set(['rtos','serial-simulator','mds','piyou','billage','codehive','argus','flightstick','maknae','model-transition']);
const caseId = location.hash.slice(1);
if (document.body.dataset.page === 'teaching' && formerCaseIds.has(caseId)) {
  location.replace(`projects/${caseId}.html`);
}
