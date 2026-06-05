---
name: ieee-manuscript-review
description: Review an IEEE Transactions manuscript against the bundled IEEEtran HOWTO references and produce a reader-friendly manuscript review report, preferably as a standalone HTML file with explicit reference support.
---

# IEEE Transactions Paper Review Skill

Use this skill to review a manuscript intended for an IEEE Transactions journal against the requirements stated in `IEEEtran_HOWTO.pdf` and `IEEEtran_bst_HOWTO.pdf`.

Apply only requirements that are explicitly supported by those two references. If you notice a real issue that is not covered there, report it as a general editorial suggestion instead of an IEEEtran compliance issue.

## When to Use

- Use this skill when the user asks for an IEEE Transactions format or style review.
- Use it for PDF reviews, LaTeX source reviews, or pre-submission self-checks.

## Instructions

### 1. Scope and Evidence

- Separate findings into two groups:
  - `IEEEtran compliance issues`: supported directly by `IEEEtran_HOWTO.pdf` or `IEEEtran_bst_HOWTO.pdf`.
  - `General editorial issues`: useful comments that are not stated in those references.
- Do not present a personal preference, lab convention, or other style guide as an IEEEtran requirement.
- If only a PDF is available, restrict comments to what is visible in the rendered manuscript.
- If LaTeX source is available, you may also check source-level IEEEtran usage when the HOWTO explicitly discusses it.

### 2. Title, Abstract, and Index Terms

- Check that the title follows normal title capitalization and does not use math or other special symbols.
- Check that the abstract is placed where IEEEtran expects it for the manuscript mode in use:
  - standard journal and technote papers place it after `\maketitle`
  - `compsoc` and `transmag` journal layouts place abstract and index terms in single-column form below the author names
- Check that the abstract generally avoids math, special symbols, and citations.
- Check that journal and technote papers include index terms / keywords.
- Check that keywords do not use math or special symbols.

### 3. Template Mode and Section Structure

- Check that the manuscript appears to use the correct IEEEtran mode for the target venue: journal, technote, peer review, `compsoc`, or `transmag`.
- For standard IEEE journal layouts, check that the manuscript is in two-column format unless it is clearly a draft or peer-review layout.
- For non-`compsoc` IEEEtran layouts, check section numbering against IEEEtran's default structure:
  - sections: upper-case Roman numerals
  - subsections: upper-case letters
  - subsubsections: Arabic numerals
  - paragraphs: lower-case letters
- For `compsoc` mode, check that section numbering is Arabic.
- If the manuscript visibly matches a technote or `compsoc` conference layout, note that `\paragraph` headings are not normally allowed there.

### 4. Figures

- Check that figure captions appear below the figures.
- When LaTeX source is available, check that figure labels are declared after or inside the caption.
- In standard IEEE papers, figure references should use `Fig.`; IEEE Computer Society conference papers use `Figure`.
- Check rendered figures for obvious quality problems that conflict with IEEEtran's graphics guidance:
  - vector graphics such as EPS or PDF are preferred for line art
  - photos may be bitmap graphics
  - visibly pixelated or degraded line art should be flagged
- For subfigures, check that labels are presented as `(a)`, `(b)`, and so on when used.
- Note that IEEEtran says many IEEE papers describe subfigures in the main caption instead of relying only on separate subcaptions.

### 5. Tables

- Check that table captions appear above the tables.
- Check that table captions follow title-style capitalization, as shown in the IEEEtran examples.
- In table captions, check that units and letters used as mathematical symbols stay upright rather than small caps.
- Check that table numbering follows IEEE style as shown in the IEEEtran examples, such as `TABLE I` and `TABLE II`.
- If the rendered table is visibly cramped or hard to read, report that as a formatting issue.

### 6. Equations and Math

- Check that equations referenced in the text are numbered.
- Do not require numbers for displayed equations that are intentionally unnumbered.
- Check that equation references follow IEEE style by using the equation number in parentheses, for example `(1)`.
- Flag equations that overrun the column width; IEEEtran makes this the author's responsibility.
- If multiline equations are used, check whether they are broken cleanly within the available column width.
- Treat double-column equations as exceptional; IEEEtran says they are rare and should be used with care.

### 7. Citations and References

- Check that citations use IEEE-style bracketed numbers.
- Do not flag sorted or compressed adjacent citations by themselves; IEEEtran explicitly supports IEEE-style sorting and compression through `cite.sty`.
- Check that the bibliography is unsorted for normal IEEE submission use, meaning references appear in citation order rather than alphabetical order.
- Check that journal names are abbreviated in IEEE style.
- For IEEE publication names, treat `IEEEabrv.bib` conventions as the reference point mentioned by `IEEEtran_bst_HOWTO.pdf`.
- For online references, check that IEEE-style URL formatting is used:
  - the URL appears with the prefix `[Online]. Available:`
  - IEEE does not place punctuation at the end of the URL
- If consecutive references repeat the same author names, note that IEEEtran normally replaces repeated names with a long dash.
- If BibTeX entries are available, note that full author names are preferred in the `.bib` data because `IEEEtran.bst` abbreviates them automatically as needed.
- Do not require DOI fields for every reference; that requirement is not stated in `IEEEtran_bst_HOWTO.pdf`.

### 8. Floats and Special Structures

- IEEE journals strongly favor top-of-page floats. Bottom floats are rare, and in-text `here` placement is usually not used except in IEEE Computer Society conferences.
- IEEE journals do not place floats in the first column of the first page and rarely do so in the second column of the first page.
- If the manuscript contains a floating `Algorithm` structure or another non-figure, non-table float, flag it: IEEEtran says the only floating structures IEEE uses are figures and tables.
- Flag content forced across the middle of the two text columns; IEEEtran explicitly warns against that style.

### 9. Editorial Conventions Check

- Always run a separate editorial pass after the IEEEtran compliance pass.
- Report editorial convention findings only as `General editorial issues`, not as IEEEtran compliance issues, unless the HOWTO references explicitly support the point.
- In the editorial pass, check for:
  - undefined or inconsistently expanded abbreviations
  - inconsistent capitalization of technical terms
  - unclear or overloaded sentences
  - subject-verb disagreement
  - inconsistent verb tense
  - unnecessary contractions in formal academic prose
  - repeated wording, vague wording, or imprecise claims
  - awkward figure, table, and equation callouts
  - missing transitions or unclear logical flow between paragraphs
- Prefer comments that are concrete and localizable, not broad taste-based rewrites.

### 10. Output Format

By default, create a standalone `.html` report in the workspace and tell the user the file path. Use a descriptive filename such as `ieee-manuscript-review-report.html` unless the user provides a document name. If the user asks for inline output only, use the compact Markdown fallback below.

For a concrete example of the expected HTML output, see `examples/ieee-manuscript-review-example-report.html`.

Use the same reader-friendly report structure as `grammar-check`:

1. **Summary**: Count IEEEtran compliance issues and general editorial issues, then list the highest-impact patterns.
2. **Before and After**: Show affected original excerpts, rendered observations, or source snippets beside the recommended revision or action.
3. **Highlighted Differences**: Show text changes inline using deletion and insertion styling where a rewrite is appropriate. For layout, source, figure, table, or bibliography issues without a direct prose rewrite, state the recommended action clearly.
4. **Manuscript Review Notes**: Use a table with location, observed issue, recommended revision/action, category, reference support, and plain-language explanation.
5. **Clean Revision Checklist**: Provide the final action list without markup.

Use this HTML structure as the report baseline:

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>IEEE Manuscript Review Report</title>
  <style>
    body { font-family: Arial, sans-serif; line-height: 1.55; margin: 2rem; color: #1f2937; }
    h1, h2 { line-height: 1.2; }
    .summary { border-left: 4px solid #2563eb; padding-left: 1rem; }
    .comparison { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 1rem; }
    .panel { border: 1px solid #d1d5db; border-radius: 6px; padding: 1rem; background: #f9fafb; }
    .diff del { background: #fee2e2; color: #991b1b; text-decoration: line-through; }
    .diff ins { background: #dcfce7; color: #166534; text-decoration: none; }
    table { border-collapse: collapse; width: 100%; }
    th, td { border: 1px solid #d1d5db; padding: 0.5rem; vertical-align: top; }
    th { background: #f3f4f6; text-align: left; }
    pre { white-space: pre-wrap; font-family: inherit; }
    @media (max-width: 800px) { .comparison { grid-template-columns: 1fr; } body { margin: 1rem; } }
  </style>
</head>
<body>
  <h1>IEEE Manuscript Review Report</h1>

  <section class="summary">
    <h2>Summary</h2>
    <ul>
      <li><strong>IEEEtran compliance issues:</strong> [number]</li>
      <li><strong>General editorial issues:</strong> [number]</li>
      <li><strong>Main patterns:</strong> [short pattern summary]</li>
    </ul>
  </section>

  <section>
    <h2>Before and After</h2>
    <div class="comparison">
      <div class="panel">
        <h3>Observed</h3>
        <pre>[original excerpt, rendered observation, or source snippet]</pre>
      </div>
      <div class="panel">
        <h3>Recommended</h3>
        <pre>[recommended revision or action]</pre>
      </div>
    </div>
  </section>

  <section>
    <h2>Highlighted Differences</h2>
    <p class="diff">[diff text with <del>removed text</del> and <ins>added text</ins>, or clear non-prose action]</p>
  </section>

  <section>
    <h2>Manuscript Review Notes</h2>
    <table>
      <thead>
        <tr>
          <th>Location</th>
          <th>Observed</th>
          <th>Recommendation</th>
          <th>Category</th>
          <th>Reference</th>
          <th>Why</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>[section/figure/table/equation/reference/source cue]</td>
          <td>[short observed issue]</td>
          <td>[short recommended revision or action]</td>
          <td>[IEEEtran compliance issue / General editorial issue]</td>
          <td>[IEEEtran_HOWTO.pdf / IEEEtran_bst_HOWTO.pdf / General editorial suggestion]</td>
          <td>[plain-language explanation]</td>
        </tr>
      </tbody>
    </table>
  </section>

  <section>
    <h2>Clean Revision Checklist</h2>
    <pre>[action list without markup]</pre>
  </section>
</body>
</html>
```

For short inline checks or when HTML is not wanted, use this compact Markdown format:

```markdown
## Before and After

Observed:
> <original excerpt, rendered observation, or source snippet>

Recommended:
> <recommended revision or action>

## Difference

<observed phrase or issue> -> <recommended revision or action>

## Manuscript Review Notes

| Location | Observed | Recommendation | Category | Reference | Why |
|---|---|---|---|---|---|
| <section/figure/table/equation/reference/source cue> | <short observed issue> | <short recommended revision or action> | <IEEEtran compliance issue / General editorial issue> | <IEEEtran_HOWTO.pdf / IEEEtran_bst_HOWTO.pdf / General editorial suggestion> | <plain-language explanation> |

## Reader-Friendly Summary

- <highest-impact compliance or editorial fix>
- <second-highest-impact compliance or editorial fix>
- <optional note about material that appears compliant>
```

## Rules

- List IEEEtran compliance issues before general editorial issues in the notes table and checklist.
- For each issue, provide a precise location such as the section title, paragraph, figure number, table number, equation number, reference number, or source snippet.
- When possible, name which reference supports the comment: `IEEEtran_HOWTO.pdf` or `IEEEtran_bst_HOWTO.pdf`.
- Do not present a comment as an IEEEtran compliance issue unless it is supported by the bundled HOWTO references.
- In HTML reports, escape user-supplied text before inserting it into HTML; only generated `<del>` and `<ins>` tags should be markup.
- Use `<del>` for removed original wording and `<ins>` for inserted revised wording in the highlighted difference section.
- If no issues are found, say so clearly and include a short checklist of items that were verified.
