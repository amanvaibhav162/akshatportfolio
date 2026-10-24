---
name: hairline
description: >-
  Use when someone asks for a Hairline figure, isometric line animation, interactive line drawing, or runs /hairline. Draws isometric line figures on the engine of @lucasmarkes/hairline, or adopts existing SVG drawings into reactive figures, outputting single self-contained HTML files.
argument-hint: "[idea or file.svg]"
---

# Hairline: Isometric Line Figures

You are making or adopting figures in the Hairline style (`@lucasmarkes/hairline`): an isometric line drawing, built from rounded solids in a single stroke, that answers the pointer. It ships as one self-contained HTML file with nothing to install. The six figures of `@lucasmarkes/hairline` are the standard; `examples/terrain.js` and `examples/riffle.js` are two reference implementations in this folder.

You write one thing: the figure. The engine (`kernel.js`) and the page (`bench.html`) are fixed. Never edit them, never paste a changed copy of them, and never rewrite what the kernel already gives you.

Every file named below is in this skill's folder. The figure and the page are written in the working directory: run `python build.py` (or `node build.mjs`), `node validate.mjs` (or manual rule inspection), and `node look.mjs` from there.

---

## Workflows

### Mode A: Create a New Figure from an Idea (`/hairline` or `/hairline-create`)

#### 1. Concept
Read `concepts.md`. Offer 2–3 concepts, one line each:
> **Name.** The object. What the pointer does to it. What the read-out says. Where the tour stops.
Wait for the person to pick, or take the concept with the strongest rest pose.

#### 2. Build
1. Read `rules.md`. The 10 rules are strict requirements:
   - Rule 01: Input only through `HL.pointer(stage, { move, leave })`; never measure screen coordinates.
   - Rule 04: No custom colors, gradients, fills, or shadows. Only kernel CSS classes (`sil`, `hi`, `lo`, `nf`, `fo`, `dash`, `dot`).
   - Rule 07: No external clocks/intervals/timers. Use `HL.register(stage, tick)`.
   - Rule 09: Prism solids with silhouettes and creases.
   - Rule 10: No text in the figure; words go to `read.textContent`.
2. Inspect `kernel.js` header index down to `var HL`.
3. Choose the closest example: `examples/terrain.js` (continuous field) or `examples/riffle.js` (discrete items).
4. Write `<name>.js` in the working directory:
   - Call `mount({ stage, svg, read }, value)` returning `{ set, destroy }`.
   - End file with `hairline({ name, means, rules, range, tour, mount })`.
5. Assemble the standalone page:
   `python build.py <name>.js` (or `node build.mjs <name>.js`)
   This creates `hairline-<name>.html`.

#### 3. Check & Validate
- Check code against `rules.md` and run `node validate.mjs hairline-<name>.html` (or inspect rules listed in `validate.mjs` manually if Node is unavailable).
- Check with browser / browser subagent or `node look.mjs <name>.js`.

#### 4. Hand over
Provide `hairline-<name>.html` and report:
- The metaphor: what the object is, and what the pointer does to it
- The rules it leans on
- The tour stops

---

### Mode B: Adopt an Existing SVG (`hairline-adopt`)

1. Read the provided `.svg` file (proportions, key contours, solids).
2. Never trace or animate the raw SVG directly: rebuild its object from 3D isometric solids on the Hairline engine.
3. Propose gestures for how the pointer interacts with the rebuilt object.
4. Follow the build and assembly steps above to generate `hairline-<name>.html`.
