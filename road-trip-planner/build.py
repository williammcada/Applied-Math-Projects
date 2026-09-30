#!/usr/bin/env python3
"""Build both self-contained entry points from checked-in, dependency-free sources."""
from pathlib import Path
root = Path(__file__).resolve().parent
html = (root / 'src/template.html').read_text()
for token, name in [('STYLE', 'style.css'), ('CORE', 'core.js'), ('ART', 'art.js'), ('UI', 'ui.js')]:
    source = (root / 'src' / name).read_text()
    if '</script' in source.lower():
        raise ValueError(f'Unsafe closing script tag in {name}')
    html = html.replace(f'/* {token} */', source)
for name in ('index.html', 'RoadTripPlanner_v0.1.0.html'):
    (root / name).write_text(html)
print(f'Built identical HTML entry points: {len(html.encode()):,} bytes each.')
