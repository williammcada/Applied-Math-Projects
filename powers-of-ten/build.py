from pathlib import Path
r=Path(__file__).resolve().parent
s=(r/'src/template.html').read_text()
for token,name in [('STYLE','style.css'),('LEGACY','legacy-core.js'),('CORE','core.js'),('ART','art.js'),('UI','ui.js')]:
    content=(r/'src'/name).read_text()
    if '</script' in content.lower():raise ValueError('Closing script tag in '+name)
    s=s.replace('/* '+token+' */',content)
for name in ['index.html','PowersOfTen_v0.2.0.html']:(r/name).write_text(s)
print('Built two identical standalone HTML files:',len(s.encode()),'bytes each')
