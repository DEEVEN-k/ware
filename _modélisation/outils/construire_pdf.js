// Construit _modélisation/Waɖɛ_Modélisation.pdf à partir des fichiers Markdown du dossier.
// Prérequis : pandoc, Playwright (Chromium). Mermaid est téléchargé dans outils/vendor/ au besoin.
// Usage : node _modélisation/outils/construire_pdf.js
const { execFileSync } = require('child_process');
const fs = require('fs');
const path = require('path');
const https = require('https');
const { chromium } = require('playwright');

const DOSSIER = path.resolve(__dirname, '..');
const RACINE = path.resolve(DOSSIER, '..');
const VENDOR = path.join(__dirname, 'vendor', 'mermaid.min.js');
const MERMAID_URL = 'https://cdn.jsdelivr.net/npm/mermaid@11.4.1/dist/mermaid.min.js';
const SORTIE = path.join(DOSSIER, 'Waɖɛ_Modélisation.pdf');
const LOGO = path.join(RACINE, '00 Commun aux deux pays', '01 Ware identité visuelle', 'LOGOTYPE HORIZONTALE.png');
const CHAPITRES = [
  '01-contexte-et-cas-utilisation.md',
  '02-diagrammes-de-classes.md',
  '03-diagrammes-etats.md',
  '04-flux-et-activites.md',
  '05-logigrammes.md',
  '06-diagrammes-de-sequence.md',
  '07-modele-physique-donnees.md',
  '08-architecture-composants.md',
  '11-formulaires-configurables.md',
];

function telecharger(url, dest) {
  return new Promise((ok, ko) => {
    fs.mkdirSync(path.dirname(dest), { recursive: true });
    https.get(url, (res) => {
      if (res.statusCode !== 200) return ko(new Error(`HTTP ${res.statusCode} sur ${url}`));
      const f = fs.createWriteStream(dest);
      res.pipe(f);
      f.on('finish', () => f.close(ok));
    }).on('error', ko);
  });
}

function versHtml(fichier) {
  const html = execFileSync('pandoc', ['-f', 'gfm', '-t', 'html', path.join(DOSSIER, fichier)], { encoding: 'utf8' });
  // pandoc produit <pre class="mermaid"><code>…</code></pre> : on retire <code> pour Mermaid.
  return html.replace(/<pre class="mermaid"><code>([\s\S]*?)<\/code><\/pre>/g, '<pre class="mermaid">$1</pre>');
}

// Les écarts du README sont repris en annexe : on en extrait la section dédiée.
function annexeEcarts() {
  const md = fs.readFileSync(path.join(DOSSIER, 'README.md'), 'utf8');
  const i = md.indexOf('## Écarts relevés');
  const extrait = '# Annexe : écarts relevés dans les livrables\n' + md.slice(i).replace(/^## Écarts relevés[^\n]*\n/, '');
  return execFileSync('pandoc', ['-f', 'gfm', '-t', 'html'], { input: extrait, encoding: 'utf8' });
}

const CSS = `
@page { size: A4 landscape; margin: 14mm 14mm 16mm 14mm; }
:root { --dark:#00370B; --green:#00901D; --light:#EAF5EC; --ink:#1d2a20; --muted:#5b6b5f; --line:#cfdcd2; }
body { font-family: "DejaVu Sans", Arial, sans-serif; color: var(--ink); font-size: 9.2pt; line-height: 1.42; margin: 0; background:#fff; }
h1 { color: var(--dark); font-size: 18pt; border-bottom: 2px solid var(--green); padding-bottom: 4px; break-before: page; margin-top: 0; }
h2 { color: var(--dark); font-size: 13pt; margin: 14px 0 6px; break-after: avoid; }
h3 { color: var(--green); font-size: 10.5pt; margin: 10px 0 4px; break-after: avoid; }
p, li { margin: 0 0 5px; }
table { border-collapse: collapse; width: 100%; font-size: 8.2pt; margin: 6px 0 10px; }
th { background: var(--dark); color: #fff; text-align: left; padding: 4px 6px; }
td { border-bottom: 1px solid var(--line); padding: 3px 6px; vertical-align: top; }
tr { break-inside: avoid; }
code { font-family: "DejaVu Sans Mono", monospace; font-size: 8pt; background: #f1f4f2; padding: 0 3px; border-radius: 3px; }
blockquote { margin: 6px 0; padding: 6px 10px; background: var(--light); border-left: 3px solid var(--green); }
pre.mermaid { text-align: center; margin: 8px 0 12px; break-inside: avoid; background: none; }
pre.mermaid svg { max-width: 100% !important; max-height: 168mm; height: auto; }
.cover { height: 175mm; display: flex; flex-direction: column; justify-content: space-between; }
.cover img { width: 70mm; }
.cover .k { color: var(--green); font-weight: 700; letter-spacing: .14em; text-transform: uppercase; font-size: 9pt; }
.cover h1 { border: 0; font-size: 30pt; break-before: auto; margin: 6px 0 8px; }
.cover .lead { font-size: 12pt; color: var(--muted); max-width: 200mm; }
.cover .meta { font-size: 8.5pt; color: var(--muted); border-top: 1px solid var(--line); padding-top: 6px; }
.toc { columns: 2; font-size: 10pt; }
`;

(async () => {
  if (!fs.existsSync(VENDOR)) await telecharger(MERMAID_URL, VENDOR);
  const corps = CHAPITRES.map(versHtml).join('\n');
  const logo = 'data:image/png;base64,' + fs.readFileSync(LOGO).toString('base64');
  const date = new Date().toLocaleDateString('fr-FR', { day: 'numeric', month: 'long', year: 'numeric' });
  const html = `<!doctype html><html lang="fr"><head><meta charset="utf-8"><title>Waɖɛ – Modélisation</title>
<style>${CSS}</style></head><body>
<div class="cover"><div><img src="${logo}"></div>
<div><div class="k">Dossier de conception</div><h1>Modélisation de Waɖɛ</h1>
<p class="lead">Contexte et cas d'utilisation, diagrammes de classes, d'états, de flux, logigrammes de qualification,
diagrammes de séquence, modèle physique PostgreSQL et architecture des composants .NET.</p></div>
<div class="meta">Établi d'après les livrables AMELEGAL v1.0 (septembre 2026). Backend ASP.NET Core (.NET 10), PostgreSQL, front React.
Généré le ${date}. Les sources Mermaid font foi : dossier <code>_modélisation/</code> du dépôt.</div></div>
<h1 style="break-before:page">Sommaire</h1><ol class="toc">
<li>Contexte et cas d'utilisation</li><li>Diagrammes de classes</li><li>Diagrammes d'états</li><li>Flux et activités</li>
<li>Logigrammes de qualification</li><li>Diagrammes de séquence</li><li>Modèle physique des données</li><li>Architecture des composants</li><li>Formulaires configurables</li>
<li>Annexe : écarts relevés dans les livrables</li></ol>
${corps}
${annexeEcarts()}
<script>${fs.readFileSync(VENDOR, 'utf8')}</script>
<script>
mermaid.initialize({ startOnLoad: false, securityLevel: 'loose', theme: 'base',
  themeVariables: { fontFamily: 'DejaVu Sans, Arial', fontSize: '13px', primaryColor: '#EAF5EC', primaryBorderColor: '#00901D',
    primaryTextColor: '#00370B', lineColor: '#4d6b55', secondaryColor: '#f6faf7', tertiaryColor: '#ffffff',
    actorBkg: '#EAF5EC', actorBorder: '#00901D', noteBkgColor: '#FDF4E3', noteBorderColor: '#B7791F' },
  flowchart: { htmlLabels: true, wrappingWidth: 220 }, sequence: { mirrorActors: false, wrap: true }, er: { useMaxWidth: true } });
mermaid.run({ querySelector: 'pre.mermaid' })
  .then(() => { document.body.dataset.ok = '1'; })
  .catch(e => { document.body.dataset.err = String(e && e.message || e); });
</script></body></html>`;

  const tmp = path.join(__dirname, 'vendor', 'modelisation.html');
  fs.writeFileSync(tmp, html);
  const navigateur = await chromium.launch();
  const page = await navigateur.newPage();
  await page.goto('file://' + tmp);
  await page.waitForFunction(() => document.body.dataset.ok || document.body.dataset.err, null, { timeout: 120000 });
  const err = await page.evaluate(() => document.body.dataset.err);
  const enErreur = await page.evaluate(() =>
    [...document.querySelectorAll('pre.mermaid')].filter(p => !p.querySelector('svg') || p.textContent.includes('Syntax error')).length);
  if (err || enErreur) { console.error('Erreur Mermaid :', err, `(${enErreur} diagramme(s) en échec)`); process.exitCode = 1; }
  await page.pdf({ path: SORTIE, format: 'A4', landscape: true, printBackground: true, displayHeaderFooter: true,
    headerTemplate: '<span></span>',
    footerTemplate: '<div style="font-size:7pt;color:#5b6b5f;width:100%;padding:0 14mm;display:flex;justify-content:space-between;font-family:Arial"><span>Waɖɛ · Modélisation</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>',
    margin: { top: '12mm', bottom: '16mm', left: '14mm', right: '14mm' } });
  await navigateur.close();
  console.log('PDF écrit :', SORTIE);
})();
