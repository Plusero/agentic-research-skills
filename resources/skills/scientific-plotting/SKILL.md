---
name: scientific-plotting
description: Create publication-quality scientific figures in Python using Matplotlib and SciencePlots. Use when the user asks to plot data, generate figures for a paper, or improve the appearance of a scientific chart.
---

# Scientific Plotting

## Setup

Install SciencePlots before use:

```bash
pip install SciencePlots
```

SciencePlots requires a LaTeX installation. See the [FAQ](https://github.com/garrettj403/SciencePlots/wiki/FAQ#installing-latex) for installation instructions.

Always begin every plotting script with:

```python
import matplotlib.pyplot as plt
import scienceplots
```

## Rules

1. **Use SciencePlots styles**: Always apply the `science` style as the base. Combine with journal-specific styles when the target venue is known (e.g., `['science', 'ieee']` for IEEE papers, `['science', 'nature']` for Nature articles).
2. **No figure titles**: Never call `ax.set_title()` or `plt.title()`. Figures in scientific papers are identified by their caption, not an inline title.
3. **Always label axes**: Every axis must have a label with units in parentheses, e.g., `ax.set_xlabel('Frequency (GHz)')`.
4. **Include a legend when multiple data series are present**: Use `ax.legend()` with concise, descriptive labels.
5. **Save figures in vector format**: Export as `.pdf` or `.svg` for publication. Use `.png` only for quick previews or when vector output is not acceptable.
6. **Explicit figure size**: Always set figure size explicitly via `plt.figure(figsize=(width, height))` or `fig, ax = plt.subplots(figsize=(width, height))` rather than relying on defaults.
7. **Tight layout**: Call `fig.tight_layout()` or `plt.tight_layout()` before saving to avoid clipped labels.
8. **Use the context manager for temporary styles**: When applying a style only to one figure inside a larger script, use `with plt.style.context(['science', ...]):` instead of `plt.style.use(...)`.

## Style Selection Guide

| Target venue / context | Recommended style combination |
|---|---|
| General scientific paper | `'science'` |
| IEEE Transactions / conference | `['science', 'ieee']` |
| Nature family journals | `['science', 'nature']` |
| Jupyter notebook | `['science', 'notebook']` |
| Poster / presentation | `['science', 'notebook']` with larger `figsize` |
| Black-and-white print | `['science', 'ieee']` or add `'grayscale'` |

## Template

Use this template as the starting point for every new figure:

```python
import matplotlib.pyplot as plt
import scienceplots

with plt.style.context(['science']):
    fig, ax = plt.subplots(figsize=(4, 3))

    # --- plot data ---
    ax.plot(x, y, label='Series label')

    # --- axes labels (always include units) ---
    ax.set_xlabel('Variable (unit)')
    ax.set_ylabel('Variable (unit)')

    # --- legend (omit when only one series) ---
    ax.legend()

    fig.tight_layout()
    fig.savefig('figure.pdf')
```

## Output Rules

- Generate complete, runnable Python code.
- Do not add `plt.title()` or `ax.set_title()` calls anywhere in the output.
- Include all necessary imports at the top of the script.
- If sample data is needed to make the script runnable, generate it with NumPy (e.g., `np.linspace`, `np.random`).
- Prefer `fig, ax = plt.subplots(...)` over the implicit `plt` state machine API.
- When saving multiple figures, give each file a descriptive name that reflects its content.
