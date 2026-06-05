---
name: paper-readability-check
description: Check the readability of an academic paper draft and produce a reader-friendly before/after readability report, preferably as a standalone HTML file with explicit checklist references.
---

# Paper Readability Check

Use this skill when the user asks to evaluate or improve readability for a paper draft, manuscript section, or paragraph.

## Readability Strategy Checklist

Apply every check below to the provided text:

1. **Purposeful sentences**: Every sentence should advance the reader's understanding; remove sentences that restate obvious facts or serve only as filler.
2. **Limit sentence content**: Keep each sentence to no more than two distinct ideas.
3. **Emphasis hierarchy**: Emphasize important points and de-emphasize minor supporting points; ensure what needs emphasis receives appropriate prominence.
4. **Information ordering**: Present old/given information before new information to build logical flow.
5. **General-to-specific**: Move from general to specific when presenting information.
6. **Paragraph focus**: Keep focus on the key message with clear paragraph structure; each paragraph should have a single central point.
7. **Subject-verb proximity**: Avoid top-heavy sentence structures; keep the main subject close to its verb and near the start of the sentence.
8. **Consistent terminology**: Use consistent key terms; avoid "elegant variation" (using different words for the same concept) when it reduces clarity, but vary phrasing when it aids understanding.
9. **Demonstrative clarity**: Use "this," "these," and "those" with a summary noun phrase when referring to an idea in a previous sentence (e.g., "this result" instead of just "this").
10. **Explicit references**: Avoid empty "it" subjects (e.g., "It is important that..."); make sure pronoun references are explicit and unambiguous.
11. **Logical connections**: Use linking and transition devices to keep logical connections clear between ideas.
12. **Conciseness**: Use as few words as possible and as many as necessary; eliminate redundancy without sacrificing clarity.
13. **Voice choice**: Prefer active voice where suitable in context, but use passive voice when the actor is unknown, unimportant, or when the object should be emphasized.
14. **Parallel structure**: Use parallel structure for items in a series, comparisons, and coordinated elements.
15. **Sentence variety**: Use a controlled variety of simple, compound, and complex sentences to communicate relationships clearly.

## Instructions

1. Read the full input text once before annotating.
2. Evaluate readability at both sentence level and paragraph level using the checklist.
3. Report only concrete issues that are visible in the provided text.
4. For each issue, include:
   - exact location (section/paragraph/sentence cue)
   - violated checklist item number
   - why readability is reduced
   - one concise rewrite suggestion
5. If no issue exists for a checklist item, do not invent one.
6. Keep suggestions faithful to the original technical meaning.
7. If a sentence has multiple readability problems, list each problem separately.
8. Prioritize high-impact issues first (logic flow, overloaded sentences, unclear references), then style-level issues.

## Output Format

By default, create a standalone `.html` report in the workspace and tell the user the file path. Use a descriptive filename such as `paper-readability-check-report.html` unless the user provides a document name. If the user asks for inline output only, use the compact Markdown fallback below.

For a concrete example of the expected HTML output, see `examples/paper-readability-check-example-report.html`.

Use the same reader-friendly report structure as `grammar-check`:

1. **Summary**: Count readability revisions and list the highest-impact patterns.
2. **Before and After**: Show the original text and a readability-improved version side by side.
3. **Highlighted Differences**: Show suggested readability changes inline using deletion and insertion styling.
4. **Readability Notes**: Use a table with location, original phrase, suggested revision, checklist reference, and plain-language explanation.
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
      <li><strong>Main patterns:</strong> [short pattern summary]</li>
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
          <td>[plain-language explanation of the readability issue]</td>
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
| <paragraph/sentence cue> | <short original phrase> | <short suggested revision> | Item <number>: <checklist name> | <plain-language explanation> |

## Reader-Friendly Summary

- <highest-impact readability fix or pattern>
- <second-highest-impact readability fix or pattern>
- <optional note about text that was already clear>
```

## Rules

- Do not change technical claims or introduce new content.
- Do not provide grammar-only nitpicks unless they affect readability.
- Do not provide vague feedback; every issue must be localized.
- Keep output concise, specific, and directly actionable.
- In HTML reports, escape user-supplied text before inserting it into HTML; only generated `<del>` and `<ins>` tags should be markup.
- Use `<del>` for removed original wording and `<ins>` for inserted revised wording in the highlighted difference section.
- If no readability issues are found, say so clearly and include the revised text unchanged.
