from pathlib import Path
p=Path(__file__).resolve().parent
s=(p/'src/template.html').read_text()
for token,file in [('STYLE','style.css'),('CORE','core.js'),('ART','art.js'),('UI','ui.js')]:
    s=s.replace('/* '+token+' */',(p/'src'/file).read_text())
for name in ['index.html','MarsColony_v0.1.0.html']:(p/name).write_text(s)
print('Built',len(s.encode()),'bytes')
