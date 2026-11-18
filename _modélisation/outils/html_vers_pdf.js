// Convertit une page HTML en PDF A4 avec Chromium (Playwright), avec pied de page numéroté.
// Usage : node html_vers_pdf.js <entrée.html> <sortie.pdf> "<titre du pied de page>" [paysage]
const { chromium } = require('playwright');

(async () => {
  const [entree, sortie, titre, orientation] = process.argv.slice(2);
  const navigateur = await chromium.launch();
  const page = await navigateur.newPage();
  await page.goto('file://' + entree, { waitUntil: 'load' });
  await page.pdf({
    path: sortie, format: 'A4', landscape: orientation === 'paysage', printBackground: true, displayHeaderFooter: true,
    headerTemplate: '<span></span>',
    footerTemplate: `<div style="font-size:7pt;color:#5b6b5f;width:100%;padding:0 14mm;display:flex;justify-content:space-between;font-family:Arial"><span>${titre}</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>`,
    margin: { top: '14mm', bottom: '16mm', left: '14mm', right: '14mm' },
  });
  await navigateur.close();
})();
