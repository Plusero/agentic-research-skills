---
name: iec-network-drawio
description: Create or revise IEC 60617-style distribution-grid diagrams in Draw.io/.drawio files. Use when the user asks to migrate, redraw, clean up, align, validate, or convert MV/LV network figures while preserving electrical topology.
---

# IEC Network Draw.io

## Core Rule

Preserve every source node, edge, device state, feeder order, branch point, protection location, measurement location, and relative left/right and above/below relationship unless the user explicitly requests a topology or layout change.

For new diagrams without an existing source, establish the topology from the user's description first. Do not invent feeders, devices, ratings, switch states, or distributed energy resources that were not provided or explicitly requested.

## Workflow

1. Inspect the source `.drawio` XML and any reference screenshots or exported images before editing. If creating a new diagram, inspect the user's topology description and identify any missing connectivity details.
2. Inventory the topology: source or MV grid, MV bus, switches or breakers, transformer, LV bus, feeders, branches, loads, measurements, and legend.
3. Decide whether the task is a symbol replacement, alignment cleanup, busbar insertion, full redraw, or validation-only pass.
4. Edit the cells named by the request and any cells whose endpoints or bounding boxes must move to prevent an overlap caused by that edit. Preserve all other cell IDs and geometry.
5. Generate or edit the diagram as editable Draw.io `mxCell` primitives, not as a flattened screenshot or embedded raster.
6. Render or export the final `.drawio` and perform every check in the validation checklist on the rendered output.

## Page Rules

1. Unless the user supplies other dimensions, use a 13.333 × 7.5 inch page and keep the drawing bounds at least 5% of the page width and height from each page edge.
2. Use fonts of at least 18 pt at final page size.

## Topology Rules

- Do not convert a radial feeder drawing into a row-based topology unless explicitly requested.
- Preserve open points, switches, protection devices, and measurement locations when they exist in the source.
- Add an LV busbar only as a structural common bus for existing LV feeder taps.
- When adding an LV busbar to a radial layout, start it 12 pt before the first feeder tap and end it 12 pt after the last feeder tap while preserving every tap's original coordinate on the busbar axis.
- Center each feeder endpoint on its busbar tap and leave no gap between the endpoint and busbar.
- Do not add PV, storage, protection, or measurement symbols unless they are present in the source or requested by the user.
- Route conductors as horizontal or vertical segments by default. Avoid tilted or diagonal lines; use orthogonal bends when a connection cannot be drawn as a single straight segment.

## Symbol Standards

Use these conventions by default:

- **Busbar**: black horizontal line with a 3 pt stroke. Label an MV bus `MV bus` and an LV bus `LV bus`; do not label an unlabeled intermediate conductor as a bus.
- **External grid or upstream network**: square with diagonal strokes in both directions at no more than 6 pt spacing. Clip every hatch stroke at the square boundary.
- **MV node**: represent an MV node as a busbar, not as a filled black circle.
- **LV node**: filled black circle at explicit LV bus, feeder, branch, or numbered node connection points.
- **Load**: filled triangular arrowhead connected by a stem of at least 12 pt. Center the stem on the triangle base and make it perpendicular to that base. Use the source arrow direction; when the source has no load arrows, use one direction for every load, defaulting to downward. Change an individual direction only when the default would make its bounding box overlap another element. Do not add a stroke inside the triangle.
- **Transformer in main diagram**: two overlapping transparent rings, oriented vertically or horizontally to match the original layout. Terminate the incoming conductor at the first ring boundary and begin the outgoing conductor at the second ring boundary; no conductor segment may enter either ring interior. Label the transformer with source-specified voltage levels, such as `MV/LV transformer` or `HV/MV transformer`; if the source gives no voltage levels, use `Transformer`.
- **Transformer in legend**: horizontal overlapping transparent rings.
- **Load in legend**: horizontal line of at least 12 pt with a filled arrowhead followed by the label `Load`. Do not include an LV node marker in the load legend.
- **Rings**: use transparent or no fill and keep both ring outlines present in the overlap region.
- **Switch or breaker**: keep the source device location and state. Use an open contact only for a source-marked open device, a closed contact only for a source-marked closed device, and a breaker block only for a source-marked breaker.
- **PV**: do not include PV, `L/P`, or `Load/PV` labels unless explicitly requested.

## Draw.io Implementation

- Use editable `mxCell` primitives: groups, edges, ellipses, rectangles, and text labels.
- Parse the XML and modify `mxCell` elements by ID; do not edit the XML with unrestricted string replacement.
- Use orthogonal connectors for feeders and branches. Preserve a non-orthogonal source connector only when the requested change does not include rerouting it.
- Use black strokes by default. Preserve the source typeface; for a new diagram, use a Times-family typeface.
- Use 3 pt strokes for busbars and 1.5 pt strokes for feeders, branches, and symbol outlines unless the source uses other explicit values that must be preserved.
- Give every instance of the same symbol class the same width, height, stroke width, and font size.
- Apply the page dimensions and margins in the Page Rules section.
- Preserve the ID of every source cell that remains in the output.

## Labels And Legend

- Label `MV bus` and `LV bus` when those busbars exist.
- Do not label feeders with IDs such as `F1`, `F2`, or `Feeder 1` unless the user explicitly requests feeder labels or the source diagram already uses them and the task is to preserve existing labels.
- Add exactly one legend entry for each symbol class used in the drawing that is not identified by an adjacent label.
- Enclose the legend in a dashed rectangular box.
- Place the legend outside the network bounding box with at least a 12 pt gap and keep its bounding box inside the page margins.
- Remove legend entries for components that do not exist in the diagram.
- Place all labels so they do not cross conductors, overlap symbols, touch arrowheads, or obscure switch states.

## Alignment Rules

- Align LV load nodes on a grid: nodes on the same feeder use the feeder's `x` coordinate, and nodes at the same edge-count distance from the LV bus use the same `y` coordinate.
- Align feeder tap points along the LV busbar.
- Center branch endpoints and load arrows on the connected busbar or LV node, regardless of arrow direction.
- Use the same load-arrow direction for all loads unless a source direction is being preserved or the default direction causes a bounding-box overlap.
- Use right-angle bends so every feeder and branch segment is horizontal or vertical.
- Center both transformer rings on the conductor axis and terminate conductors at the ring boundaries as specified under Symbol Standards.
- Keep at least 6 pt between a text bounding box and any symbol or conductor that the text does not label. A label may touch neither its target symbol nor an arrowhead.
- Reuse the same dimensions for every instance of a symbol class.
- Keep the legend inside the existing page and at least 12 pt from the network bounding box.

## Output Rules

- Return a user-facing `.drawio` file unless the user only asked for review or validation.
- If generating companion exports, keep the `.drawio` as the source of truth and treat PNG/PDF/SVG exports as previews.
- Report any topology ambiguity instead of silently guessing a new network structure.

## Validation Checklist

Before final delivery:

- Confirm the `.drawio` XML parses without an error.
- Confirm the diagram remains editable as Draw.io primitives.
- Confirm no unintended `PV`, `L/P`, or `Load/PV` text remains unless requested.
- Confirm no conductor lines cross through transformer rings.
- Confirm both ring outlines are present in the transformer overlap region.
- Confirm explicit LV connection nodes use filled black circles unless another node style was requested.
- Confirm LV nodes are aligned horizontally and vertically.
- Confirm all load arrows point in the same direction except arrows preserving a different source direction or avoiding a documented overlap.
- Confirm every new or rerouted conductor segment is horizontal or vertical.
- Confirm every instance of a symbol class has the same width, height, stroke width, and font size.
- Confirm no text overlaps or touches symbols, conductors, arrowheads, or other labels.
- Confirm feeder labels such as `F1` and `F2` are absent unless explicitly requested or intentionally preserved from the source.
- Confirm the legend is enclosed in a dashed box, stays inside the page margins, and is at least 12 pt from the network bounding box.
- Confirm labels and legend entries match the actual symbols in the drawing.
- Render or export the `.drawio` and inspect it at full-page size. Confirm every label is at least 18 pt, no two text bounding boxes overlap, no text bounding box intersects an unrelated conductor or symbol, and no element crosses the page boundary. If Draw.io export tooling is unavailable, report that limitation and perform the same geometry checks from the XML bounding boxes.
