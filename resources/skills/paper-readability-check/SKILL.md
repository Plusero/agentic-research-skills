---
name: paper-readability-check
description: Check an academic paper draft against sentence- and paragraph-level readability criteria, then produce revised text and a before/after report with checklist references. Use for paper drafts, manuscript sections, and academic paragraphs.
---

# Paper Readability Check

## Readability Strategy Checklist

Apply every check below to the provided text:

1. **Duplicate content**: Flag a sentence when it repeats a proposition from the preceding two sentences without adding data, a qualification, an inference, a citation, or a transition.
2. **Claims per sentence**: Split a sentence that contains more than two independently supportable claims.
3. **Claim placement**: Put the paragraph's controlling claim in its first sentence unless the paragraph explicitly uses a question-answer or evidence-conclusion structure; in those structures, put the claim immediately after the question or evidence.
4. **Given-before-new order**: Introduce an entity or term before using its abbreviation, pronoun, synonym, or consequence.
5. **Category-before-instance order**: Define a category, method class, or comparison criterion before listing its members, variants, or results.
6. **Paragraph scope**: Assign one controlling claim to each paragraph. Move a sentence when it neither supports, qualifies, contrasts with, nor derives from that claim.
7. **Subject-verb distance**: Flag a main clause when more than 12 words intervene between its subject and finite verb; revise by moving or converting the intervening material unless a technical name or fixed quotation causes the distance.
8. **Terminology mapping**: Use one term for one concept. Replace a synonym when the text has not defined a distinction between it and the established term.
9. **Demonstrative clarity**: Use "this," "these," and "those" with a summary noun phrase when referring to an idea in a previous sentence (e.g., "this result" instead of just "this").
10. **Explicit references**: Replace an empty `it` subject with the actor, result, condition, or claim it denotes. Flag a pronoun when two or more preceding noun phrases match its number and gender.
11. **Named logical relations**: Add a connective when adjacent sentences have an unstated cause, contrast, condition, example, or sequence relation. Use a connective that names that relation.
12. **Redundancy**: Delete repeated propositions and phrases whose removal changes no claim, qualification, condition, or citation scope.
13. **Voice choice**: Use active voice when the actor is known and performs the paragraph's focal action. Use passive voice when the actor is absent from the evidence or when the acted-on entity is the paragraph's established subject.
14. **Parallel structure**: Use parallel structure for items in a series, comparisons, and coordinated elements.
15. **Repeated syntax**: Flag four consecutive sentences that begin with the same subject or use the same clause pattern; revise at least one without changing the stated relation between ideas.

## Instructions

1. Read the full input text once before annotating.
2. Evaluate readability at both sentence level and paragraph level using the checklist.
3. Report only passages that meet a checklist condition above.
4. For each issue, include:
   - exact location (section/paragraph/sentence cue)
   - violated checklist item number
   - the exact words that meet the checklist condition
   - one rewrite
5. If no issue exists for a checklist item, do not invent one.
6. Preserve claims, mathematical relations, units, citations, terminology, and degree of certainty.
7. If a sentence has multiple readability problems, list each problem separately.
8. Order issues by document location, then by checklist item number when multiple items apply to the same passage.

## Output Format

By default, create `paper-readability-check-report.html` in the workspace, or `<input-name>-readability-check.html` when the input has a filename. If the user asks for inline output only, use the Markdown format below.

For a concrete example of the expected HTML output, see `examples/paper-readability-check-example-report.html`.

Use these report sections:

1. **Summary**: Count revisions and list checklist items in descending order by occurrence count.
2. **Before and After**: Show the original text and a readability-improved version side by side.
3. **Highlighted Differences**: Show suggested readability changes inline using deletion and insertion styling.
4. **Readability Notes**: Use a table with location, original phrase, suggested revision, checklist reference, and one sentence naming the matched condition and its effect on interpretation.
5. **Clean Revised Text**: Provide the final readability-improved text without markup.

Use this HTML structure as the report baseline:

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Paper Readability Check Report</title>
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
  <h1>Paper Readability Check Report</h1>

  <section class="summary">
    <h2>Summary</h2>
    <ul>
      <li><strong>Total readability revisions:</strong> [number]</li>
      <li><strong>Counts by checklist item:</strong> [item names and counts in descending order]</li>
    </ul>
  </section>

  <section>
    <h2>Before and After</h2>
    <div class="comparison">
      <div class="panel">
        <h3>Original</h3>
        <pre>[original text]</pre>
      </div>
      <div class="panel">
        <h3>Revised</h3>
        <pre>[readability-improved text]</pre>
      </div>
    </div>
  </section>

  <section>
    <h2>Highlighted Differences</h2>
    <p class="diff">[diff text with <del>removed text</del> and <ins>added text</ins>]</p>
  </section>

  <section>
    <h2>Readability Notes</h2>
    <table>
      <thead>
        <tr>
          <th>Location</th>
          <th>Original</th>
          <th>Revision</th>
          <th>Checklist</th>
          <th>Why</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>[paragraph/sentence cue]</td>
          <td>[short original phrase]</td>
          <td>[short suggested revision]</td>
          <td>Item [number]: [checklist name]</td>
          <td>[matched checklist condition and its effect on interpretation]</td>
        </tr>
      </tbody>
    </table>
  </section>

  <section>
    <h2>Clean Revised Text</h2>
    <pre>[readability-improved text without markup]</pre>
  </section>
</body>
</html>
```

For short inline checks or when HTML is not wanted, use this compact Markdown format:

```markdown
## Before and After

Original:
> <original text>

Revised:
> <readability-improved text>

## Difference

<original phrase> -> <suggested revision>

## Readability Notes

| Location | Original | Revision | Checklist | Why |
|---|---|---|---|---|
| <paragraph/sentence cue> | <short original phrase> | <short suggested revision> | Item <number>: <checklist name> | <matched condition and effect on interpretation> |

## Summary

- <most frequent checklist item and count>
- <second-most frequent checklist item and count>
- <number of paragraphs with no revisions>
```

## Rules

- Do not change technical claims or introduce new content.
- Do not report a grammar issue unless the same passage also meets one of checklist items 1–15.
- Quote the affected span and identify its paragraph and sentence number for every issue.
- Give one imperative edit instruction or one replacement passage for every issue.
- In HTML reports, escape user-supplied text before inserting it into HTML; only generated `<del>` and `<ins>` tags should be markup.
- Use `<del>` for removed original wording and `<ins>` for inserted revised wording in the highlighted difference section.
- If no checklist condition is met, write `No readability issues found under the checklist.` and include the supplied text unchanged.
