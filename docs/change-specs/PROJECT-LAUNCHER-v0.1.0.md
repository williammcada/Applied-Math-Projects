# Applied Math Projects launcher v0.1.0

Authorized by William McAda's 9 October 2026 request for a teacher project selector, QR display, and direct iPad navigation; Netlify destination supplied in the conversation.

Baseline: a94c503b955464c26e738b2e60268efcfadb4175. Handbook: fd4330863f4cc0812180fbf1de122970a42c7885; AI-START-HERE, UNIVERSAL-RULES, CONDITIONAL-STANDARDS (S-02/S-04/S-05), RELEASE-CHECKLIST consulted.

## Contract
- Root index.html provides illustrated project cards, mathematical focus, approximate duration, Open project and Share with students.
- Four implemented directories are launchable: road-trip-planner, food-truck-business-launch, theme-park-designer, powers-of-ten. Mars Colony is explicitly coming soon because baseline has no runnable entry point.
- Share opens an accessible dialog with project title, locally generated high-contrast QR with four-module quiet zone, clickable URL, copy control and projection/full-screen control. Escape/Close returns focus to the launching button. Clipboard/fullscreen failure offers usable fallback.
- URLs resolve from the hosted homepage directory, work under Netlify root and GitHub project subpaths, and exclude query/hash. File-protocol copies use the canonical Netlify origin.
- Instructions tell students to scan using iPad Camera and tap its link. No accounts, class sessions, tracking or QR service. Existing progress is browser/origin-local; moving from GitHub Pages requires existing export/import.
- Preserve all existing project HTML byte-for-byte. The new homepage carries v0.1.0 in title and footer. Existing original artwork is reused as static SVG previews.
- Primary classroom host: https://mcada-applied-math.netlify.app/; main branch, root publish directory, no build command. This supersedes the prior GitHub Pages classroom-host choice.

## Verification
Decode each QR independently and compare with its project link; verify all hosted entry points; test switching projects, keyboard close/focus, responsive widths, copy fallback and projection mode. Check original application hashes unchanged. Preserve implementation checkpoint before tests, exact tested candidate afterward. Physical iPad camera and school-network checks remain Not run until observed.
