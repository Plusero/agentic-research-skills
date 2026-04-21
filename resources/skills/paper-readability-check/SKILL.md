---
name: paper-readability-check
description: Check the readability of an academic paper draft and report concrete sentence-level and paragraph-level issues using a fixed readability strategy checklist.
---

# Paper Readability Check

Use this skill when the user asks to evaluate or improve readability for a paper draft, manuscript section, or paragraph.

## Readability Strategy Checklist

Apply every check below to the provided text:

1. Keep information functional.
2. Keep each sentence to no more than two distinct ideas.
3. Emphasize information that needs emphasis.
4. Present old information before new information.
5. Move from general to specific when presenting information.
6. Emphasize important points and de-emphasize minor supporting points.
7. Keep focus on the key message with clear paragraph structure.
8. Avoid top-heavy sentence structures; keep the main subject close to its verb and near the start of the sentence.
9. Repeat key words and phrases where repetition improves clarity.
10. Use this, these, and those with a summary noun phrase when referring to an idea in a previous sentence.
11. Avoid empty it subjects; make sure pronoun references are explicit.
12. Use linking and transition devices to keep logical connections clear between ideas.
13. Use as few words as possible and as many as necessary.
14. Prefer active voice where suitable in context.
15. Use parallel structure where suitable.
16. Use a controlled variety of simple, compound, and complex sentences to communicate relationships clearly.

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

Use exactly this structure:

```markdown
## Readability Issues

1. [Severity: High] <location>
   - Checklist item: <number>
   - Problem: <why this hurts readability>
   - Suggestion: <concise rewrite guidance>

2. [Severity: Medium] <location>
   - Checklist item: <number>
   - Problem: <why this hurts readability>
   - Suggestion: <concise rewrite guidance>

## Strengths

- <clear readability strength tied to checklist>
- <clear readability strength tied to checklist>

## Priority Revisions

1. <highest-impact readability fix>
2. <second highest-impact readability fix>
3. <third highest-impact readability fix>
```

## Rules

- Do not change technical claims or introduce new content.
- Do not provide grammar-only nitpicks unless they affect readability.
- Do not provide vague feedback; every issue must be localized.
- Keep output concise, specific, and directly actionable.
