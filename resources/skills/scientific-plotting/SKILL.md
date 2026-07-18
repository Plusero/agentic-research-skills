---
name: scientific-plotting
description: Create and validate scientific figures in Python using Matplotlib and SciencePlots. Use when the user asks to plot data, generate a paper figure, reproduce a chart, or revise a scientific plot's layout or styling.
---

# Scientific Plotting

## Setup

Install SciencePlots when it is absent:

```bash
pip install SciencePlots
```

SciencePlots requires a LaTeX installation for styles that set `text.usetex=True`. If LaTeX is unavailable and installation is outside the task scope, use `plt.rc_context({"text.usetex": False})` and report the substitution.

Start plotting scripts with:

```python
import matplotlib.pyplot as plt
import scienceplots
```

## Construction Rules

1. Apply `science` as the base style. Add `ieee`, `nature`, `notebook`, or `grayscale` only under the conditions in the style table below.
2. Do not call `ax.set_title()` or `plt.title()` unless the user explicitly requests an in-figure title.
3. Label every displayed axis. Include units in parentheses; use `(dimensionless)` when the quantity has no unit and omit the parenthetical only for category labels.
4. When two or more series share an axes, add a legend with one entry per series. Use the variable, treatment, model, or scenario name as the entry text.
5. Export a PDF or SVG. Also export a PNG preview when the requested deliverable is vector-only.
6. Set `figsize` explicitly. Use the user's dimensions; otherwise use `(3.5, 2.6)` inches for a single-column figure and `(7.16, 3.5)` inches for a double-column figure.
7. Call `fig.tight_layout()` before saving. If it emits a warning or leaves clipping, replace it with explicit `subplots_adjust` values.
8. Use `with plt.style.context([...]):` when the script creates figures that use different style sets.
9. Distinguish series by at least two of color, marker, and line style when the figure must work in grayscale or has more than four series.

## Style Selection

| Condition | Style list |
|---|---|
| No venue specified | `['science']` |
| IEEE Transactions or IEEE conference | `['science', 'ieee']` |
| Nature-family journal | `['science', 'nature']` |
| Notebook, poster, or presentation | `['science', 'notebook']` |
| Grayscale output requested | `['science', 'grayscale']` |

## Template

```python
import matplotlib.pyplot as plt
import scienceplots

with plt.style.context(['science']):
    fig, ax = plt.subplots(figsize=(3.5, 2.6))

    ax.plot(x, y, label='Series label')
    ax.set_xlabel('Variable (unit)')
    ax.set_ylabel('Variable (unit)')
    ax.legend()

    fig.tight_layout()
    fig.savefig('dependent-variable-vs-independent-variable.pdf')
    fig.savefig('dependent-variable-vs-independent-variable.png', dpi=300)
```

## Validation

1. Run the completed script and require a zero exit status.
2. Open the PNG preview at its exported dimensions and verify:
   - every requested series, annotation, panel, and reference line is present;
   - every displayed axis has a label and unit treatment matching rule 3;
   - the legend has one entry per plotted series and no entry is truncated;
   - no label, tick label, legend, annotation, or panel identifier overlaps another text or data element;
   - no text or plotted element crosses the image boundary;
   - color, marker, and line-style assignments satisfy rule 9;
   - the pixel dimensions equal the requested dimensions or the `figsize × dpi` values.
3. Open the PDF or SVG at 400% zoom and verify that text and line art show no raster pixels or compression blocks.
4. Revise, rerun, and repeat the checks after the final code change.

## Deliverables

- runnable Python source with all imports;
- PDF or SVG output;
- PNG preview;
- the values used for style list, figure size, and DPI;
- a statement that the script exited successfully and the visual checks passed.
