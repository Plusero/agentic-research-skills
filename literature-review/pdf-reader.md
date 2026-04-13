---
name: summarize-academic-pdf-with-sources
description: Read an academic publication in PDF format and produce a structured Markdown summary. Use when the user asks to summarize a research paper, journal article, conference paper, or any .pdf academic document.
---

# Academic PDF Summary

## Instructions

1. Identify the PDF path provided by the user.
2. Read the PDF content with available file-reading tools.
3. Extract the core points with evidence from the paper text:
   - Main contributions
   - Key limitations
   - Open questions raised by the work
   - Trivial but important implementation or methodological details
4. Write the summary to a `.md` file in the workspace.
5. For every bullet point, append a source location in this format: `(Source: p.<page>, <section or paragraph cue>)`.
6. Use exactly this section order and heading text:

```markdown
Contributions

1. contribution1 (Source: p.3, Introduction, para 2)
2. contribution2 (Source: p.5, Method, "Model architecture" paragraph)
3. contribution3 (Source: p.7, Results, Table 2 discussion)

Limitations:

1. contribution1 (Source: p.8, Limitations section, para 1)
2. contribution2 (Source: p.9, Discussion, final paragraph)
3. contribution3 (Source: p.6, Ablation study paragraph)

Questions:

1. Questions 1 (Source: p.9, Future work paragraph)
2. Questions 2 (Source: p.4, Assumptions subsection)
3. Questions 3 (Source: p.10, Conclusion)

Trivial but important Details

1. detail1 (Source: p.11, Appendix A, hyperparameters list)
2. detail2 (Source: p.6, Training setup paragraph)
3. detail3 (Source: p.5, Dataset preprocessing paragraph)
```

## Output Rules

- Keep each list item concise and specific.
- Ground every point in the paper content; do not invent claims.
- If the paper has fewer than three strong points for a section, use the best available evidence and keep wording explicit.
- Every list item must include a source location with page number and a pinpoint cue (section title, table/figure reference, or short paragraph locator).
- Preserve the exact heading capitalization and punctuation shown in the template.
- Output only Markdown in the generated `.md` file.
