---
name: grammar-check
description: Check text for grammar, punctuation, mechanics, and usage errors, then produce a reader-friendly before/after correction report, preferably as a standalone HTML file with explicit rule references.
---

# Grammar Check

Use this skill when the user asks to check, proofread, correct, polish, or review grammar in prose, academic writing, emails, documentation, reports, or short passages.

## Grammar Rules

Apply every rule below to the supplied text:

1. **Subject-verb agreement**: Make the verb agree with the grammatical subject in number and person, including with compound subjects, intervening phrases, and collective nouns.
2. **Verb tense and aspect**: Use tense consistently and choose the tense/aspect that matches the timing, duration, and sequence of events.
3. **Sentence completeness**: Fix fragments, comma splices, fused sentences, and run-on sentences.
4. **Pronoun agreement and reference**: Make pronouns agree with their antecedents and ensure every pronoun points to a clear noun or noun phrase.
5. **Articles and determiners**: Use "a," "an," "the," quantifiers, and possessives correctly for countability, specificity, and idiom.
6. **Prepositions and particles**: Use idiomatic prepositions and verb particles; correct missing, extra, or mismatched prepositions.
7. **Modifier placement**: Place adjectives, adverbs, participial phrases, and limiting modifiers near the words they modify; fix dangling or misplaced modifiers.
8. **Parallel structure**: Use matching grammatical forms in lists, comparisons, headings, and coordinated phrases.
9. **Word form and part of speech**: Use the correct noun, verb, adjective, adverb, gerund, or infinitive form.
10. **Word choice and idiom**: Correct non-idiomatic phrasing, confused words, and incorrect collocations while preserving the intended meaning.
11. **Punctuation**: Use commas, semicolons, colons, apostrophes, quotation marks, parentheses, and end punctuation according to the sentence structure.
12. **Capitalization**: Capitalize proper nouns, titles, acronyms, sentence starts, and headings consistently.
13. **Spelling and typographical errors**: Correct misspellings, duplicated words, missing words, and obvious typos.
14. **Hyphenation and compounds**: Use hyphens for compound modifiers and established terms where needed for clarity.
15. **Number, abbreviation, and symbol consistency**: Keep number style, abbreviations, units, symbols, and spacing internally consistent.

## Instructions

1. Read the full text before making corrections.
2. Preserve the user's meaning, tone, terminology, formatting, and technical claims.
3. Correct grammar and mechanics directly when the fix is clear.
4. If multiple valid corrections exist, choose the most natural option for the surrounding context.
5. If a sentence is ambiguous, explain the ambiguity instead of guessing.
6. Report only visible issues from the supplied text; do not invent issues to cover every rule.
7. Combine repeated instances of the same minor issue when that is easier to read.
8. Prefer concise explanations that teach the rule without lecturing.
9. Show the difference between the original and corrected text whenever practical.
10. If the user asks only for a clean corrected version, provide the corrected text first and keep notes brief.
11. If the text is long, group issues by paragraph or section and focus on the most important corrections.

## Output Format

By default, create a standalone `.html` report in the workspace and tell the user the file path. Use a descriptive filename such as `grammar-check-report.html` unless the user provides a document name. If the user asks for inline output only, use the compact Markdown fallback below.

For a concrete example of the expected HTML output, see `examples/grammar-check-example-report.html`.

The HTML report must include these reader-friendly sections:

1. **Summary**: Count major issue types and list the highest-impact patterns.
2. **Before and After**: Show the original text and corrected text side by side.
3. **Highlighted Differences**: Show changes inline using deletion and insertion styling.
4. **Grammar Notes**: Use a table with location, original phrase, corrected phrase, rule reference, and plain-language explanation.
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
          <td>[plain-language explanation]</td>
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
| <paragraph/sentence cue> | <short original phrase> | <short corrected phrase> | Rule <number>: <rule name> | <plain-language explanation> |

## Reader-Friendly Summary

- <highest-impact correction or pattern>
- <second-highest-impact correction or pattern>
- <optional note about text that was already clear>
```

## Rules

- Do not change factual content, citations, variables, code, equations, names, or quoted text unless the user explicitly asks.
- Do not rewrite for style beyond what is needed to fix grammar, mechanics, or idiomatic usage.
- Do not mark dialect-specific variants as errors unless the user requested a specific variety of English.
- When English variety matters and the user did not specify one, keep the existing variety if it is consistent; otherwise use standard American English.
- Keep tables readable by using short phrases in cells. Move longer explanations below the table if needed.
- In HTML reports, escape user-supplied text before inserting it into HTML; only generated `<del>` and `<ins>` tags should be markup.
- Use `<del>` for removed original wording and `<ins>` for inserted corrected wording in the highlighted difference section.
- If no grammar issues are found, say so clearly and include the corrected text unchanged.
