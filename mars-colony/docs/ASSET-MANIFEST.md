# Mars Colony v0.1.0 — Asset Manifest

All runtime art is original inline SVG authored for this application. It lives in `src/art.js` or `src/ui.js` and is embedded by `build.py`. No external artwork, icon font, web font, raster image, audio file or runtime CDN is used. Product credit: **A WILLIAM MCADA PRODUCT**. No third-party artwork license is asserted or required for these newly authored assets; repository ownership terms apply.

| Asset | Purpose and stage | Source / dimensions (viewBox) | Accessibility | Scale |
| --- | --- | --- | --- | --- |
| MC-A01 | Mars horizon; home and stage banner | `MCArt.scene`; 900 × 500 | SVG role=img; research-outpost description | Narrative only |
| MC-A02 | Water | `MCArt.icon('water')`; 100 × 100 | Decorative; adjacent Water label | Not to scale |
| MC-A03 | Oxygen | `MCArt.icon('oxygen')`; 100 × 100 | Decorative; adjacent Oxygen label | Not to scale |
| MC-A04 | Food | `MCArt.icon('food')`; 100 × 100 | Decorative; adjacent Food label | Not to scale |
| MC-A05 | Habitat | `MCArt.icon('habitat')`; 100 × 100 | Decorative; adjacent Habitat label | Not to scale |
| MC-A06 | Solar | `MCArt.icon('solar')`; 100 × 100 | Decorative; adjacent Solar label | Not to scale |
| MC-A07 | Battery | `MCArt.icon('battery')`; 100 × 100 | Decorative; adjacent Battery label | Not to scale |
| MC-A08 | Authoritative resource systems after checks; report | `system()` in UI; 270 × 195 per resource | Separate production arrow, storage box, consumption arrow; numeric units in text and SVG accessible label | Values authoritative; arrows not proportional |
| MC-A09 | Reduced solar scene; stage 6 | `MCArt.scene(6,…)`; 900 × 500 | Dust-reduced solar description | Narrative only |
| MC-A10 | Resilient ending; stage 8 | `MCArt.scene(8,…,'resilient')`; 900 × 500 | Outpost description plus adjacent result/criteria | Count-dependent habitats/arrays; not an engineering plan |
| MC-A11 | Limited-reserve ending; stage 8 | `MCArt.scene(8,…,'ready')`; 900 × 500 | Adjacent explicit Mission ready text; amber accents | Not to scale |
| MC-A12 | Delayed ending; stage 8 | `MCArt.scene(8,…,'delayed')`; 900 × 500 | Adjacent specific failed criteria; subdued structures | Not to scale |
| MC-A13 | Personalized printable patch | `MCArt.patch`; 300 × 330 | SVG role=img; patch label, alias/configuration/version in text | Decorative |
| Graph | Typed resource points; stage 5/report | `graph()` in UI; 760 × 360 | Labeled axes, unit-specific scale; adjacent typed point entries and daily table | Code-scaled days and selected resource stock |
| Favicon | Tab identity | `src/template.html`; inline 64 × 64 SVG data URI | Browser tab uses full text title | Decorative |

Required scenes are implemented rather than placeholders. Correctness of mathematical labels is checked in core/DOM tests; actual rendering, text fit, contrast and print rendering are not yet verified in a real browser. The original dossier Mars artwork remains untouched as source provenance and is not fetched at runtime.
