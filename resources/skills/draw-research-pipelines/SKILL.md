---
name: draw-research-pipelines
description: Create, revise, and validate publication-ready research pipeline and workflow figures from manuscripts, method descriptions, source code, data schemas, rough sketches, or existing diagrams. Use for model architectures, data flows, experimental protocols, study designs, system architectures, graphical abstracts, and requests to draw, redraw, simplify, or quality-check a scientific workflow figure.
---

# Draw Research Pipelines

## Goal

Turn scientific source material into an accurate, legible, and editable workflow figure. Model the scientific process first, draw it second, and validate the rendered result last.

## Workflow

### 1. Establish the figure contract

- Identify the audience, publication venue, target dimensions, output format, and required level of detail.
- Infer reasonable defaults when these constraints are absent.
- Ask a question only when an ambiguity could materially change the scientific meaning.
- Write a one-sentence statement of what the reader should understand from the figure.

### 2. Extract the semantic graph

Before drawing, identify:

- inputs and outputs;
- stages and transformations;
- data, samples, models, instruments, and other persistent entities;
- branches, merges, feedback loops, repetitions, and quality-control gates;
- intermediate artifacts or state changes that carry scientific meaning;
- uncertain or omitted details.

Represent arrows as explicit relationships or actions. Do not stabilize the layout until the semantic graph is coherent.

### 3. Select a visual archetype

Choose the simplest structure that preserves the science:

- linear for a dominant sequence;
- branched for alternatives or parallel paths;
- cyclic for genuine iteration or feedback;
- layered for software, model, or system levels;
- multiscale for movement between spatial or temporal scales;
- symmetric for paired or comparative workflows.

Prefer one dominant reading direction. Route secondary paths and feedback loops around the main spine.

### 4. Explore and select a layout

- Produce two or three low-fidelity candidates when the structure admits meaningfully different layouts.
- Score candidates for scientific fidelity, reading order, hierarchy, crossings, label proximity, compactness, and accessibility.
- Select the strongest candidate and record any deliberate simplifications.

### 5. Render an editable figure

- Use vector graphics by default.
- Apply a consistent visual grammar: shape for entity type, color for category or phase, line style for relationship type, and arrowheads for direction.
- Preserve the visual identity of recurring samples, datasets, models, or outputs.
- Direct-label elements where possible instead of relying on a distant legend.
- Show concrete inputs, scientifically meaningful intermediate states, and the final research output.
- Keep text, strokes, spacing, and icons legible at the intended publication size.
- Use a small color-vision-deficiency-safe palette with redundant shape, pattern, or line cues.

### 6. Validate and revise

Render the final export and inspect it visually. Check:

1. **Scientific fidelity** — Every required stage, dependency, branch, and output is correct.
2. **Topology** — The start, direction, and endpoint are immediately apparent; crossings and unnecessary bends are minimized.
3. **Hierarchy** — Major phases dominate supporting detail, and related operations are visibly grouped.
4. **Semantic consistency** — Shapes, colors, names, arrows, and line styles retain one meaning throughout.
5. **Legibility and accessibility** — Text survives final-size viewing; the figure remains understandable in grayscale and with common color-vision deficiencies.
6. **Production quality** — Nothing is clipped, misaligned, pixelated, or dependent on unavailable fonts.
7. **Caption consistency** — Terminology, numbering, abbreviations, and claims agree with the manuscript.

Revise until all checks pass. Never declare the figure complete without inspecting the rendered output at its intended size.

## Core design rules

- Make the figure understandable at two speeds: rapid orientation and detailed tracing.
- Establish one dominant visual path.
- Group related steps into clearly named phases.
- Keep labels next to the objects they describe.
- Use arrows to communicate meaningful transformations, not decoration.
- Move feedback loops to the perimeter when possible.
- Minimize crossings, bends, branches, and decorative clutter.
- Avoid unexplained acronyms and details that do not support the figure's main claim.
- Ensure the caption adds nuance rather than basic navigation instructions.
- Use external examples for design inspiration only; do not reproduce another paper's figure or distinctive artwork.

## Deliverables

Provide, as appropriate:

- an editable SVG, Draw.io, PowerPoint, or equivalent source file;
- a publication-ready PDF and high-resolution PNG;
- a concise figure caption and accessible alt text;
- an optional JSON or YAML diagram specification for reproducibility;
- a short note describing assumptions, simplifications, and validation results.
