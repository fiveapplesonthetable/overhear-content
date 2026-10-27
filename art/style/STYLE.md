# Art house style

One **square 1024x1024** cartoon per scene, flat and calm, readable at a 56 px thumbnail. Reference images in this
folder (`*.webp`, with their `*.svg` sources and `contact-sheet.webp`): look at them before drawing anything.

## Style text
Rounded shapes, no outlines, dot eyes, rosy blush, flat fills. **One dominant colour per image** with a lighter
"spotlight" circle behind the action and a darker floor. Cream `#FFF6EA` for paper, plates, cups and chef whites;
ink `#2E2A3A` for faces and small details. Skin tones `#F6D2B5` (light), `#D9A074` (medium), `#9A6341` (deep).
Blush `#F0808A`. Two or three characters at most, big and simple, one clear key moment (a gesture, an object, an
emotion). **No text, letters, numbers, logos or signs anywhere** (the art must work in any UI language; clocks and
calendars show shapes, not digits). No photoreal, no gradients-heavy rendering, no outlines, no real people's likeness:
characters are stylised cartoons inspired by the roles, not portraits of actors.

## Reusable prompt (fill the <...> slots)
```
Flat vector-style cartoon illustration, square 1:1, 1024x1024. Rounded shapes, no outlines, dot eyes, soft rosy
blush, flat fills with a lighter spotlight circle behind the subject and a darker floor. Dominant colour: <COLOUR
NAME + HEX>. Cream #FFF6EA for plates/paper/whites, ink #2E2A3A for faces. Calm, warm, slightly humorous mood.
Scene: <LOCATION>. Key moment: <ONE SENTENCE: who does what, with which prop>. Characters (draw exactly as
described): <PASTE the matching lines from out/<show>/characters.md>. Simple composition, big shapes, readable as a
small thumbnail. Absolutely no text, letters, numbers, logos or signs.
```
Negative prompt (if the tool has one): text, letters, numbers, watermark, outline, photo, realistic, 3d render, gradient
mesh, extra fingers, blur.

## Consistency
- Draw every recurring character from their entry in `out/<show>/characters.md` (hair, clothes, colours, props,
  signature feature), same colours every time. Add a new character to the sheet the first time one is drawn.
- Vary the dominant colour from scene to scene within an episode; keep location colours stable across episodes
  (the kitchen is always the same teal/steel tones, etc.; note them in `characters.md` under "Places").
- Pick the dominant colour from the emotional temperature of the scene (warm = friendly, cool = tense).

## Delivery
`out/<show>/sNNeNN/scene-NN.webp` (1024x1024, WebP quality ~85, a few dozen KB; PNG `scene-NN.png` is accepted but
keep repo size down, convert with `cwebp -q 85` or Pillow). If you can't call an image model, hand-author an SVG
(`gen_reference.py` here shows the small helper library used for the existing set: heads, bodies, arms, props) and
rasterise it to 1024x1024 WebP. Check the picture visually before pushing.

## Existing cast (seed for `characters.md`)
Anya (copper ponytail), the Chef (toque + moustache), Lena (dark curls), Lea (blonde bob), Arlette (silver bun +
glasses), Hervé (beard + tie). The existing set (dominant colours): surprise pink `#EC8DAE`, cafe caramel `#C98B5E`,
market green `#6BB26D`, kitchen slate `#6E86A0`, knife teal `#2E9A96`, lunch tomato `#E2604F`, agency lilac
`#A58BD3`, telephone sky `#78B9E8`, appointment mint `#86CDB2`.
