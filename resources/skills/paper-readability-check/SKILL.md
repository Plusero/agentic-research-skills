---
name: paper-readability-check
description: Check the readability of an academic paper draft and report concrete sentence-level and paragraph-level issues using a fixed readability strategy checklist.
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
