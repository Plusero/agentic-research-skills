---
name: ieee-manuscript-review
description: Review an IEEE Transactions manuscript against the bundled IEEEtran HOWTO references and produce an HTML or Markdown report that separates sourced compliance findings from editorial findings. Use for PDF reviews, LaTeX source reviews, and pre-submission IEEE Transactions checks.
---

# IEEE Transactions Paper Review Skill

Use this skill to review a manuscript intended for an IEEE Transactions journal against the requirements stated in `IEEEtran_HOWTO.pdf` and `IEEEtran_bst_HOWTO.pdf`.

Classify a finding as an IEEEtran compliance issue only when one of the two bundled references states the applicable rule. Classify a finding that matches an item in the editorial checklist below as a general editorial issue when neither reference states the rule.

## Instructions

### 1. Scope and Evidence

- Separate findings into two groups:
  - `IEEEtran compliance issues`: supported directly by `IEEEtran_HOWTO.pdf` or `IEEEtran_bst_HOWTO.pdf`.
  - `General editorial issues`: findings that match the editorial checklist but are not stated in those references.
- Do not present a personal preference, lab convention, or other style guide as an IEEEtran requirement.
- If only a PDF is available, restrict comments to what is visible in the rendered manuscript.
- If LaTeX source is available, you may also check source-level IEEEtran usage when the HOWTO explicitly discusses it.

### 2. Title, Abstract, and Index Terms

- Compare title capitalization with the title-style capitalization used by the target journal or supplied template. Record every math expression and non-alphanumeric symbol in the title.
- Check that the abstract is placed where IEEEtran expects it for the manuscript mode in use:
  - standard journal and technote papers place it after `\maketitle`
  - `compsoc` and `transmag` journal layouts place abstract and index terms in single-column form below the author names
- Record every math expression, special symbol, and citation in the abstract, and cite the HOWTO guidance for avoiding it.
- Check that journal and technote papers include index terms / keywords.
- Check that keywords do not use math or special symbols.

### 3. Template Mode and Section Structure

- Map the target venue to `journal`, `technote`, `peerreview`, `compsoc`, or `transmag`, then compare that mode with the class options in the LaTeX source or the rendered layout. Ask for the target venue when the mapping cannot be determined from the request or manuscript.
- For standard IEEE journal layouts, require two columns unless the source contains a draft or peer-review class option or the rendered manuscript is labeled as a draft or review copy.
- For non-`compsoc` IEEEtran layouts, check section numbering against IEEEtran's default structure:
  - sections: upper-case Roman numerals
  - subsections: upper-case letters
  - subsubsections: Arabic numerals
  - paragraphs: lower-case letters
- For `compsoc` mode, check that section numbering is Arabic.
- Record every `\paragraph` heading in a technote or `compsoc` conference manuscript and cite the HOWTO restriction for those modes.

### 4. Figures

- Check that figure captions appear below the figures.
- When LaTeX source is available, check that figure labels are declared after or inside the caption.
- In standard IEEE papers, figure references should use `Fig.`; IEEE Computer Society conference papers use `Figure`.
- Inspect rendered figures at 200% zoom for these conditions from IEEEtran's graphics guidance:
  - vector graphics such as EPS or PDF are preferred for line art
  - photos may be bitmap graphics
  - flag line art when individual pixels or compression blocks are visible at 200% zoom
- For subfigures, verify that identifiers use `(a)`, `(b)`, and so on. If separate subcaptions are absent, verify that the main caption maps each identifier to its description.

### 5. Tables

- Check that table captions appear above the tables.
- Check that table captions follow title-style capitalization, as shown in the IEEEtran examples.
- In table captions, check that units and letters used as mathematical symbols stay upright rather than small caps.
- Check that table numbering follows IEEE style as shown in the IEEEtran examples, such as `TABLE I` and `TABLE II`.
- Report a table formatting issue when text overlaps a rule or another text element, a cell is clipped, or the table exceeds the column or page boundary.

### 6. Equations and Math

- Check that equations referenced in the text are numbered.
- Do not require numbers for displayed equations that are intentionally unnumbered.
- Check that equation references follow IEEE style by using the equation number in parentheses, for example `(1)`.
- Flag equations that overrun the column width; IEEEtran makes this the author's responsibility.
- For multiline equations, verify that every line stays inside the column, alignment points use the same relation or operator class, and no equation element overlaps its number.
- Record every double-column equation and cite IEEEtran's warning that this construction is rare; do not classify it as noncompliant without an additional violated rule.

### 7. Citations and References

- Check that citations use IEEE-style bracketed numbers.
- Do not flag sorted or compressed adjacent citations by themselves; IEEEtran explicitly supports IEEE-style sorting and compression through `cite.sty`.
- For a submission manuscript, verify that references appear in first-citation order rather than alphabetical order.
- Check that journal names are abbreviated in IEEE style.
- For IEEE publication names, treat `IEEEabrv.bib` conventions as the reference point mentioned by `IEEEtran_bst_HOWTO.pdf`.
- For online references, check that IEEE-style URL formatting is used:
  - the URL appears with the prefix `[Online]. Available:`
  - IEEE does not place punctuation at the end of the URL
- Record consecutive references that repeat the same author names instead of using the IEEEtran long dash.
- If BibTeX entries are available, record author fields that contain initials where the authors' full names are available in the supplied source; `IEEEtran.bst` performs abbreviation during formatting.
- Do not require DOI fields for every reference; that requirement is not stated in `IEEEtran_bst_HOWTO.pdf`.

### 8. Floats and Special Structures

- Record each bottom-of-page or in-text float and compare it with the HOWTO's top-of-page guidance. Apply the stated exception for IEEE Computer Society conferences.
- Record each first-page float and its column. Cite the HOWTO distinction between the prohibited first column and discouraged second column.
- If the manuscript contains a floating `Algorithm` structure or another non-figure, non-table float, flag it: IEEEtran says the only floating structures IEEE uses are figures and tables.
- Flag content forced across the middle of the two text columns; IEEEtran explicitly warns against that style.

### 9. Editorial Conventions Check

- Always run a separate editorial pass after the IEEEtran compliance pass.
- Report editorial convention findings only as `General editorial issues`, not as IEEEtran compliance issues, unless the HOWTO references explicitly support the point.
- In the editorial pass, check for:
  - undefined or inconsistently expanded abbreviations
  - inconsistent capitalization of technical terms
  - a sentence with more than two independently supportable claims
  - subject-verb disagreement
  - inconsistent verb tense
  - contractions outside quotations
  - a proposition repeated within the preceding two sentences without a new qualification, citation, or result
  - figure, table, or equation callouts that omit the object number or use a different number from the object
  - adjacent paragraphs whose cause, contrast, condition, example, or sequence relation is not stated
- For every editorial finding, quote the affected span, identify its section and paragraph or object number, and provide one replacement or imperative edit instruction.

### 10. Output Format

By default, create `ieee-manuscript-review-report.html` in the workspace, or `<input-name>-ieee-review.html` when the input has a filename. If the user asks for inline output only, use the Markdown format below.

For a concrete example of the expected HTML output, see `examples/ieee-manuscript-review-example-report.html`.

Use these report sections:

1. **Summary**: Count IEEEtran compliance issues and general editorial issues, then list issue types in descending order by count.
2. **Before and After**: Show affected original excerpts, rendered observations, or source snippets beside the recommended revision or action.
3. **Highlighted Differences**: Show prose changes with deletion and insertion styling. For a non-prose issue, use an imperative action that names the affected object and the required property.
4. **Manuscript Review Notes**: Use a table with location, observed issue, recommended revision/action, category, reference support, and one sentence stating the violated check.
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
      <li><strong>Counts by issue type:</strong> [issue types and counts in descending order]</li>
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
    <p class="diff">[diff text with <del>removed text</del> and <ins>added text</ins>, or imperative non-prose action]</p>
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
          <td>[violated check and resulting mismatch]</td>
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
| <section/figure/table/equation/reference/source cue> | <short observed issue> | <short recommended revision or action> | <IEEEtran compliance issue / General editorial issue> | <IEEEtran_HOWTO.pdf / IEEEtran_bst_HOWTO.pdf / General editorial suggestion> | <violated check and resulting mismatch> |

## Summary

- <most frequent issue type and count>
- <second-most frequent issue type and count>
- <number of checked categories with no findings>
```

## Rules

- List IEEEtran compliance issues before general editorial issues in the notes table and checklist.
- For each issue, provide a precise location such as the section title, paragraph, figure number, table number, equation number, reference number, or source snippet.
- For every IEEEtran compliance issue, name `IEEEtran_HOWTO.pdf` or `IEEEtran_bst_HOWTO.pdf` and give the PDF page plus section or paragraph cue.
- Do not present a comment as an IEEEtran compliance issue unless it is supported by the bundled HOWTO references.
- In HTML reports, escape user-supplied text before inserting it into HTML; only generated `<del>` and `<ins>` tags should be markup.
- Use `<del>` for removed original wording and `<ins>` for inserted revised wording in the highlighted difference section.
- If no issues are found, write `No IEEEtran compliance or editorial issues found under the listed checks.` and list each checked section by its heading number.
