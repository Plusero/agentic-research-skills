---
name: grammar-check
description: Check text for grammar, punctuation, mechanics, and usage errors, then produce corrected text and a before/after report with a numbered rule reference for every change. Use for proofreading prose, academic writing, emails, documentation, reports, or short passages.
---

# Grammar Check

## Grammar Rules

Apply every rule below to the supplied text:

1. **Subject-verb agreement**: Make the verb agree with the grammatical subject in number and person, including with compound subjects, intervening phrases, and collective nouns.
2. **Verb tense and aspect**: Use tense consistently and choose the tense/aspect that matches the timing, duration, and sequence of events.
3. **Sentence completeness**: Fix fragments, comma splices, fused sentences, and run-on sentences.
4. **Pronoun agreement and reference**: Make pronouns agree with their antecedents and flag a pronoun when two or more preceding noun phrases match its number and gender.
5. **Articles and determiners**: Use "a," "an," "the," quantifiers, and possessives correctly for countability, specificity, and idiom.
6. **Prepositions and particles**: Use idiomatic prepositions and verb particles; correct missing, extra, or mismatched prepositions.
7. **Modifier placement**: Place adjectives, adverbs, participial phrases, and limiting modifiers near the words they modify; fix dangling or misplaced modifiers.
8. **Parallel structure**: Use matching grammatical forms in lists, comparisons, headings, and coordinated phrases.
9. **Word form and part of speech**: Use the correct noun, verb, adjective, adverb, gerund, or infinitive form.
10. **Word choice and idiom**: Correct non-idiomatic phrasing, confused words, and incorrect collocations while preserving the intended meaning.
11. **Punctuation**: Use commas, semicolons, colons, apostrophes, quotation marks, parentheses, and end punctuation according to the sentence structure.
12. **Capitalization**: Capitalize proper nouns, titles, acronyms, sentence starts, and headings consistently.
13. **Spelling and typographical errors**: Correct misspellings, duplicated words, missing words required by the sentence grammar, and character transpositions.
14. **Hyphenation and compounds**: Use hyphens for compound modifiers and established terms where needed for clarity.
15. **Number, abbreviation, and symbol consistency**: Keep number style, abbreviations, units, symbols, and spacing internally consistent.

## Instructions

1. Read the full text before making corrections.
2. Preserve every factual claim, degree of certainty, technical term, citation, paragraph boundary, list structure, and formatting element not implicated by a correction.
3. Apply a correction directly when one option satisfies the applicable rule without changing a property listed in step 2.
4. When multiple corrections satisfy the rule, choose the option with the fewest changed words; if tied, choose the option consistent with the document's existing English variety and terminology.
5. If a sentence is ambiguous, explain the ambiguity instead of guessing.
6. Report only visible issues from the supplied text; do not invent issues to cover every rule.
7. Combine repeated instances into one table row only when they use the same rule and the same original-to-corrected pattern; list every affected location in that row.
8. Explain each correction in one sentence that names the grammatical mismatch and the rule that resolves it.
9. Show every changed span with paired `<del>` and `<ins>` markup in HTML or an `original -> correction` pair in Markdown.
10. If the user requests only corrected text, return only corrected text and do not create a report.
11. For inputs longer than 1,500 words, group table rows by the input's section headings, or by paragraph ranges when headings are absent.

## Output Format

By default, create `grammar-check-report.html` in the workspace, or `<input-name>-grammar-check.html` when the input has a filename. If the user asks for inline output only, use the Markdown format below.

For a concrete example of the expected HTML output, see `examples/grammar-check-example-report.html`.

The HTML report must include these sections:

1. **Summary**: Report the total corrections and issue types in descending order by count.
2. **Before and After**: Show the original text and corrected text side by side.
3. **Highlighted Differences**: Show changes inline using deletion and insertion styling.
4. **Grammar Notes**: Use a table with location, original phrase, corrected phrase, rule reference, and one sentence naming the mismatch and correction rule.
5. **Clean Corrected Text**: Provide the final corrected text without markup.

Use this HTML structure as the report baseline:

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Grammar Check Report</title>
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
  <h1>Grammar Check Report</h1>

  <section class="summary">
    <h2>Summary</h2>
    <ul>
      <li><strong>Total corrections:</strong> [number]</li>
      <li><strong>Counts by rule:</strong> [rule names and counts in descending order]</li>
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
        <h3>Corrected</h3>
        <pre>[corrected text]</pre>
      </div>
    </div>
  </section>

  <section>
    <h2>Highlighted Differences</h2>
    <p class="diff">[diff text with <del>removed text</del> and <ins>added text</ins>]</p>
  </section>

  <section>
    <h2>Grammar Notes</h2>
    <table>
      <thead>
        <tr>
          <th>Location</th>
          <th>Original</th>
          <th>Correction</th>
          <th>Rule</th>
          <th>Why</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>[paragraph/sentence cue]</td>
          <td>[short original phrase]</td>
          <td>[short corrected phrase]</td>
          <td>Rule [number]: [rule name]</td>
          <td>[grammatical mismatch and correction rule]</td>
        </tr>
      </tbody>
    </table>
  </section>

  <section>
    <h2>Clean Corrected Text</h2>
    <pre>[corrected text without markup]</pre>
  </section>
</body>
</html>
```

For short inline checks or when HTML is not wanted, use this compact Markdown format:

```markdown
## Before and After

Original:
> <original text>

Corrected:
> <corrected text>

## Difference

<original phrase> -> <corrected phrase>

## Grammar Notes

| Location | Original | Correction | Rule | Why |
|---|---|---|---|---|
| <paragraph/sentence cue> | <short original phrase> | <short corrected phrase> | Rule <number>: <rule name> | <grammatical mismatch and correction rule> |

## Summary

- <most frequent correction type and count>
- <second-most frequent correction type and count>
- <number of paragraphs with no corrections>
```

## Rules

- Do not change factual content, citations, variables, code, equations, names, or quoted text unless the user explicitly asks.
- Do not rewrite for style beyond what is needed to fix grammar, mechanics, or idiomatic usage.
- Do not mark dialect-specific variants as errors unless the user requested a specific variety of English.
- When the input mixes English varieties and the user did not specify one, use the variety represented by the greater number of variety-specific spellings; ask the user when the counts tie.
- Limit `Original`, `Correction`, and `Why` cells to 30 words each. Put additional explanation below the table and reference the table row number.
- In HTML reports, escape user-supplied text before inserting it into HTML; only generated `<del>` and `<ins>` tags should be markup.
- Use `<del>` for removed original wording and `<ins>` for inserted corrected wording in the highlighted difference section.
- If no grammar issues are found, write `No grammar issues found.` and include the supplied text unchanged.
