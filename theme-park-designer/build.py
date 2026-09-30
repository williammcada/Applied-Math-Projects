from pathlib import Path
p=Path(__file__).resolve().parent
html=(p/'src/template.html').read_text()
for token,name in [('STYLE','style.css'),('CORE','core.js'),('ART','art.js'),('UI','ui.js')]:
    content=(p/'src'/name).read_text()
    if '</script' in content.lower(): raise ValueError('Unsafe script closing tag')
    html=html.replace('/* '+token+' */',content)
for name in ['index.html','ThemeParkDesigner_v0.1.0.html']:(p/name).write_text(html)
print(f'Built byte-identical HTML files, {len(html.encode())} bytes each.')
