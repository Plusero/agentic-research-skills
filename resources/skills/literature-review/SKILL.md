---
name: literature-review
description: Read an academic publication in PDF format and produce a source-located Markdown summary of its contributions, limitations, open questions, and reproducibility details. Use when the user asks to summarize a research paper, journal article, conference paper, or academic PDF.
---

# Academic PDF Summary

## Workflow

1. Resolve the PDF path supplied by the user and extract the text with page boundaries preserved.
2. Record claims under four categories:
   - **Contributions:** methods, datasets, systems, analyses, or empirical findings that the authors identify as additions relative to prior work.
   - **Limitations:** scope restrictions, assumptions, failure cases, negative results, missing evaluations, or resource constraints stated or demonstrated in the paper.
   - **Open Questions:** future-work questions stated by the authors. Label an unstated question as `Inferred` and cite the results or limitation from which it follows.
   - **Reproducibility Details:** dataset versions and splits, preprocessing, hyperparameters, initialization, stopping criteria, software versions, random seeds, hardware, and evaluation settings.
3. Attach one pinpoint source to every recorded claim: page number plus a section title, table or figure number, equation number, or quoted phrase of no more than eight words.
4. Write the result to `<paper-title-slug>-summary.md` in the workspace. Use lowercase ASCII letters, digits, and hyphens in the slug.
5. Use the section order and heading text shown below.

```markdown
## Contributions

1. <contribution> (Source: p.3, Introduction, para 2)

## Limitations

1. <limitation> (Source: p.8, Limitations, para 1)

## Open Questions

1. <question> (Source: p.9, Future work, para 1)

## Reproducibility Details

1. <detail> (Source: p.11, Appendix A, hyperparameters list)
```

## Output Checks

- Write each item as one claim in no more than two sentences.
- Include only claims supported at the cited location.
- Do not force a minimum item count. Emit an empty section followed by `No supported items found.` when no source passage supports that category.
- Verify that every page number exists in the PDF and that every section, table, figure, equation, or phrase cue occurs on that page.
- Preserve the heading text, order, and capitalization from the template.
- Write only Markdown to the generated file.
