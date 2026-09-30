from pathlib import Path
root=Path(__file__).resolve().parent
html=(root/'src/template.html').read_text()
for marker,name in [('STYLE','style.css'),('CORE','core.js'),('ART','art.js'),('UI','ui.js')]:
    html=html.replace('/*'+marker+'*/',(root/'src'/name).read_text())
for name in ('index.html','MarsColony_v0.1.0.html'):
    (root/name).write_text(html)
print(f'Built {len(html.encode())} bytes; identical standalone and deployable HTML.')
