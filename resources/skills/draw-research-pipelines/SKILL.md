---
name: draw-research-pipelines
description: Create, revise, and validate scientific pipeline and workflow figures in Draw.io from manuscripts, methods, code, schemas, sketches, or existing diagrams. Use for research pipelines, model architectures, data flows, experimental protocols, study designs, system architectures, graphical abstracts, and requests to draw, redraw, simplify, or quality-check a scientific workflow figure.
---

# Draw Research Pipelines

Produce an editable `.drawio` file, a vector PDF, and a PNG that pass the checks below.

## Workflow

1. **Record the figure requirements.** Record the audience, process or claim to show, required nodes and relations, source terminology, output format, and publication dimensions. Ask the user when sources disagree or when missing information would change a node, edge, or reading order.

2. **Write a pipeline specification.** For each node, record an ID, display label, entity type, phase, inputs, and outputs. For each edge, record its source, target, and relation. Include branches, merges, loops, intermediate states, persistent entities, and quality-control gates found in the source material.

3. **Select the topology from the specification.** Use a linear layout for a sequence without branches; a branched layout for alternatives or converging inputs; an external return path for a loop; lanes for layers, scales, or responsible parties; and aligned panels for comparisons. Use left-to-right primary flow unless the publication format or source convention requires top-to-bottom flow.

4. **Build in Draw.io.** Use Draw.io (`.drawio`) as the editable source and use vector shapes. Assign one shape to each entity type, one fill color to each phase or category, one line style to each relation type, and arrowheads to directed relations. Apply each assignment throughout the figure and include a legend for any assignment not stated in the labels. Label an edge with a verb phrase when its relation is not already stated by the connected node labels.

5. **Fit the target page.** Unless another format is specified, set the page to 16:9 and keep all figure content at least 5% of the page width and height from each edge. At final page size, use a font size of at least 18 pt and a stroke width of at least 1.5 pt. If the content does not fit, combine nodes, shorten labels without changing terminology, or split the workflow into labeled panels; do not reduce the font below 18 pt.

6. **Export and inspect.** Export a vector PDF and a PNG preview at 1920 × 1080 px for a 16:9 figure. Open both exports and perform these checks at full-page view:

   - every node and edge in the pipeline specification appears once unless a documented duplication is required;
   - every connector starts at its recorded source and its arrowhead touches its recorded target;
   - the primary path follows the declared reading direction, while feedback edges run outside that path;
   - no connector crosses a node, label, or arrowhead;
   - no text is clipped, truncated, or overlapped, and every label is at least 18 pt at final size;
   - terminology and capitalization match the source material;
   - each shape, fill color, line style, and arrowhead has the assignment defined in step 4;
   - grayscale conversion preserves distinctions through shape or line-style differences;
   - at 400% PDF zoom, text and vector shapes show no raster pixels or compression blocks;
   - the export contains the specified page bounds and margins, with no content outside the page.

Revise and repeat the export checks until all items pass. Do not deliver a figure that has not been opened and inspected after its final export.

## Construction constraints

- Write process-node labels as verb phrases, artifact or data labels as noun phrases, and decision labels as questions.
- Put nodes assigned to the same phase inside a container labeled with that phase; do not use an unlabeled enclosure.
- Draw a connector only for a relation recorded in the pipeline specification.
- Keep each connector's final segment straight and perpendicular to the target edge. Place its last bend at least 12 pt from the target edge.
- Use zero bends for aligned nodes and no more than two orthogonal bends for a primary-path connector. Route feedback and secondary connectors outside the primary path.
- Use the Okabe–Ito palette or another named color-vision-deficiency-safe palette. Do not encode a distinction by color alone; pair color with shape, line style, or a text label.
- Expand each acronym on first use in the figure or its legend.
- Do not add decorative icons, background illustrations, gradients, or drop shadows.
- Do not trace or copy icons, illustrations, or complete layouts from published figures.

## Deliverables

Provide:

- editable `.drawio` source;
- vector PDF and PNG preview;
- caption and alt text;
- a list of assumptions and the completed export checks.
