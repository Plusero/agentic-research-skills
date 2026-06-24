---
name: iec-network-drawio
description: Create or revise IEC 60617-style distribution-grid diagrams in Draw.io/.drawio files. Use when the user asks to migrate, redraw, clean up, align, validate, or convert MV/LV network figures while preserving electrical topology.
---

# IEC Network Draw.io

## Core Rule

Preserve the original electrical topology and spatial layout unless the user explicitly asks for a redesign. Improve symbols, spacing, alignment, and readability without changing feeder order, branch positions, protection placement, or network connectivity.

For new diagrams without an existing source, establish the topology from the user's description first. Do not invent feeders, devices, ratings, switch states, or distributed energy resources that were not provided or explicitly requested.

## Workflow

1. Inspect the source `.drawio` XML and any reference screenshots or exported images before editing. If creating a new diagram, inspect the user's topology description and identify any missing connectivity details.
2. Inventory the topology: source or MV grid, MV bus, switches or breakers, transformer, LV bus, feeders, branches, loads, measurements, and legend.
3. Decide whether the task is a symbol replacement, alignment cleanup, busbar insertion, full redraw, or validation-only pass.
4. Modify only the requested or necessary elements. Keep branch endpoints and feeder order stable unless the user asks for layout changes.
5. Generate or edit the diagram as editable Draw.io `mxCell` primitives, not as a flattened screenshot or embedded raster.
6. Render or export the final `.drawio`, then visually inspect alignment, symbol overlap, label clutter, and unintended crossings.

## Topology Rules

- Do not convert a radial feeder drawing into a row-based topology unless explicitly requested.
- Preserve open points, switches, protection devices, and measurement locations when they exist in the source.
- Add an LV busbar only as a structural common bus for existing LV feeder taps.
- When adding an LV busbar to a radial layout, extend it far enough to span the feeder tap points while preserving original feeder positions.
- Connect feeders to busbars cleanly at aligned tap points.
- Do not add PV, storage, protection, or measurement symbols unless they are present in the source or requested by the user.

## Symbol Standards

Use these conventions by default:

- **Busbar**: thick black horizontal line. Label only meaningful busbars such as `MV bus` and `LV bus`.
- **External grid or upstream network**: cross-hatched square, connected to the upstream side of the network.
- **MV node**: represent an MV node as a busbar, not as a filled black circle.
- **LV node**: filled black circle at explicit LV bus, feeder, branch, or numbered node connection points. Use these solid balls by default for numbered LV nodes, as in common distribution-feeder figures.
- **Load**: filled arrow connected to the busbar or to an LV node. Follow the source or layout direction; use a downward arrow only when no orientation is implied. Do not add extra vertical strokes inside the load symbol.
- **Transformer in main diagram**: two vertical overlapping transparent rings. Do not draw any conductor through the rings. Stop the conductor above the top ring and resume below the lower ring.
- **Transformer in legend**: horizontal overlapping transparent rings.
- **Rings**: use transparent or no fill so both ring outlines remain visible at the overlap.
- **Switch or breaker**: keep the source device location and state. Use a simple IEC-style open contact, closed contact, or breaker block only when the source implies that device.
- **PV**: do not include PV, `L/P`, or `Load/PV` labels unless explicitly requested.

## Draw.io Implementation

- Use editable `mxCell` primitives: groups, edges, ellipses, rectangles, and text labels.
- Prefer structured XML parsing and generation over ad hoc string replacement.
- Use orthogonal connectors for feeders and branches unless the source drawing intentionally uses another routing style.
- Use black strokes and Times-style labels when matching technical IEC figures.
- Keep consistent stroke widths within symbol classes: busbars should be visually heavier than feeders and symbol outlines.
- Keep page dimensions tight enough to frame the diagram without unnecessary whitespace.
- Preserve stable element IDs when making small edits to an existing `.drawio` file, unless regeneration is simpler and safe.

## Labels And Legend

- Keep labels sparse and technical.
- Label `MV bus` and `LV bus` when those busbars exist.
- Use a small legend for symbols that appear in the drawing, typically `External grid`, `Bus`, `Load`, `Transformer`, and any switch or breaker symbol actually present.
- Remove legend entries for components that do not exist in the diagram.
- Place labels so they do not cross conductors, overlap symbols, or obscure switch states.

## Alignment Rules

- Align LV load nodes on a grid: same feeder column means same `x`; equivalent load levels across feeders should share the same `y`.
- Align feeder tap points along the LV busbar.
- Center branch endpoints and load arrows on the connected busbar or LV node, regardless of arrow direction.
- Keep transformer rings centered on the main vertical conductor path, with visible gaps where the conductor stops and resumes.

## Output Rules

- Return a user-facing `.drawio` file unless the user only asked for review or validation.
- If generating companion exports, keep the `.drawio` as the source of truth and treat PNG/PDF/SVG exports as previews.
- Report any topology ambiguity instead of silently guessing a new network structure.

## Validation Checklist

Before final delivery:

- Confirm the `.drawio` XML parses cleanly.
- Confirm the diagram remains editable as Draw.io primitives.
- Confirm no unintended `PV`, `L/P`, or `Load/PV` text remains unless requested.
- Confirm no conductor lines cross through transformer rings.
- Confirm transformer ring overlaps are visible.
- Confirm explicit LV connection nodes use filled black circles unless another node style was requested.
- Confirm LV nodes are aligned horizontally and vertically.
- Confirm labels and legend entries match the actual symbols in the drawing.
- Render or export the `.drawio` and inspect the actual visual output. If Draw.io export tooling is unavailable, report that limitation and perform XML-level checks for geometry, labels, and symbol consistency instead.
