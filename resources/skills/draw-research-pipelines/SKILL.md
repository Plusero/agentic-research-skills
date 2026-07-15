---
name: draw-research-pipelines
description: Create, revise, and validate publication-ready scientific pipeline and workflow figures in Draw.io from manuscripts, methods, code, schemas, sketches, or existing diagrams. Use for research pipelines, model architectures, data flows, experimental protocols, study designs, system architectures, graphical abstracts, and requests to draw, redraw, simplify, or quality-check a scientific workflow figure.
---

# Draw Research Pipelines

Create an accurate, legible, editable pipeline figure. Model the science first, build the figure in Draw.io, and visually inspect the rendered export before delivery.

## Workflow

1. **Define the message.** Identify what the reader must understand, the intended audience, required content, output format, and publication constraints. Ask only when ambiguity could change the scientific meaning.

2. **Map the pipeline.** Extract inputs, outputs, stages, transformations, persistent entities, branches, merges, loops, intermediate states, and quality-control gates. Every arrow must express a clear relationship or action.

3. **Choose the structure.** Use the simplest faithful layout: linear, branched, cyclic, layered, multiscale, or comparative. Establish one dominant reading direction and route secondary or feedback paths around the main flow.

4. **Build in Draw.io.** Use Draw.io (`.drawio`) as the editable source for pipeline figures. Use vector shapes and a consistent grammar: shapes for entity types, colors for phases or categories, line styles for relationship types, and arrowheads for direction. Direct-label elements where practical and keep recurring entities visually consistent.

5. **Fit a 16:9 slide.** Unless another format is specified, design for a widescreen 16:9 slide and leave sufficient margins for presentation use. Set the Draw.io page or export bounds to a 16:9 aspect ratio and remove excess whitespace. Keep every label at least 18 pt at final slide size, and ensure strokes, arrowheads, and spacing remain clear when the complete figure is viewed on one slide. Reduce label density or simplify the figure rather than shrinking the text.

6. **Export and visually inspect.** Export vector PDF and a PNG preview, then the agent must open and visually check the rendered figure at its intended placement on a 16:9 slide. Do not rely only on source structure or automated checks. Confirm:

   - all stages, dependencies, branches, and outputs are scientifically correct;
   - reading order, hierarchy, and arrow direction are immediately clear;
   - labels are legible at final size and terminology matches the manuscript;
   - shapes, colors, and line styles retain one meaning throughout;
   - crossings, bends, clutter, and unused whitespace are minimized;
   - nothing is clipped, overlapping, misaligned, pixelated, or font-dependent;
   - the figure remains understandable in grayscale and with common color-vision deficiencies.

Revise and re-inspect until every check passes. Never declare the figure complete without opening the rendered export and checking it visually at final size.

## Design rules

- Make the main path obvious at a glance and traceable in detail.
- Group related steps into named phases and place labels near their objects.
- Use arrows for meaningful transformations, not decoration.
- Keep each connector's final segment straight and perpendicular to the target edge, and place terminal bends far enough from the target that the arrowhead clearly points into it rather than sideways or backward.
- Show concrete inputs, meaningful intermediate states, and final outputs.
- Use a small color-vision-deficiency-safe palette with redundant shape or line cues.
- When the complete workflow figure is placed on a 16:9 slide, render every label at least 18 pt at final slide size; reduce label density or simplify the figure rather than using smaller text.
- Remove unexplained acronyms, decorative clutter, and details that do not support the figure's message.
- Use published examples only as inspiration; do not reproduce distinctive artwork.

## Deliverables

Provide:

- editable `.drawio` source;
- publication-ready vector PDF and PNG preview;
- concise caption and accessible alt text;
- brief assumptions and visual-validation note.
