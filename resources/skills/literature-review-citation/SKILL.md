---
name: literature-review-citation
description: "Read an academic paper PDF and a supplied literature-review theme, then draft exactly two sentences for citing the paper within that theme: its main idea or contribution, then a limitation, followed by supporting original sentences with pinpoint source locations. Use when the user wants a concise contribution-and-limitation citation passage rather than a full paper summary."
---

# Literature Review Citation

Turn one supplied paper PDF and a literature-review theme into a concise passage for that review, followed by the original sentences supporting each claim.

## Inputs

Require two inputs:

1. **Paper PDF:** supplied as an attachment, local path, or accessible link.
2. **Literature-review theme:** the subject around which the review is organized, such as **Uncertainty Quantification**, **State Estimation**, or **Power Flow Calculations**. A broad theme is sufficient; a detailed research question is not required.

Use a theme already established in the conversation. If none is supplied or established, ask for it before drafting the two sentences; the PDF can be read while awaiting the answer. Use a surrounding paragraph, citation key, or preferred language if provided; these remain optional.

If the PDF is missing or unreadable, request a readable copy instead of drafting from the title or memory.

## Workflow

1. Read the PDF with page boundaries preserved. Check the abstract, introduction, method and assumptions, evaluation, discussion, and conclusion, including relevant appendices. Inspect page images when extraction or OCR leaves the wording, equations, or reading order uncertain.
2. Identify the main idea or contribution most relevant to the supplied theme: what the paper proposes, establishes, or demonstrates, and for which problem. Let the theme guide the emphasis while keeping the setting and any claimed result within the paper's evidence; do not invent thematic relevance or repeat unsupported novelty or superiority claims.
3. Select one substantive limitation that matters for the theme and qualifies the selected contribution's scope, applicability, evidence, or computational feasibility. Prefer a limitation explicitly stated by the authors. Otherwise, infer a narrow limitation from concrete assumptions, evaluation conditions, or results and label it as inferred in the supporting evidence. An untested setting supports a statement that applicability there is unverified, not that the method cannot work there. Silence or a future-work suggestion alone does not establish a defect.
4. Collect the shortest complete original sentence or sentences that support each proposed review sentence. Check the surrounding text for qualifications and contrary evidence. Every substantive clause in the review passage must be supported by these quotations or by an inference explicitly explained beneath them.
5. Draft and verify the output below. Return it directly in the conversation unless the user requests a file.

## Output

Start with one paragraph containing **exactly two review sentences**:

- **Sentence 1:** Describe the main idea or contribution relevant to the theme in clear academic prose, attributing it to the paper.
- **Sentence 2:** Highlight the selected limitation in the context of that theme and its relevant consequence, if that consequence is supported.

Use the user's citation format and supplied citation key when available; otherwise use author and year verified from the PDF. Do not invent a bibliography key or missing metadata. Keep each sentence focused on one main point, and paraphrase rather than copying the evidence into the review passage.

After that paragraph, show supporting original sentences separately for the contribution and the limitation:

```markdown
<Author/year or supplied citation> <main idea or contribution relevant to the theme>. However, <specific supported limitation relevant to the theme>.

**Supporting sentences from the paper**

1. **Contribution — PDF p. <N>, Section <number/title>, <paragraph or other locator>**

   > <Exact original sentence supporting sentence 1.>

2. **Limitation — Author-stated / Inferred; PDF p. <N>, Section <number/title>, <paragraph or other locator>**

   > <Exact original sentence supporting sentence 2 or establishing the basis for the inference.>

   <For an inferred limitation only: briefly explain how the quoted evidence supports the bounded claim.>
```

Replace placeholders and choose the applicable limitation label. Add another quotation and its locator only when necessary to support a claim fully. Preserve the paper's language in quotations even when the review passage is written in another language.

## Evidence and Final Checks

- Quote verbatim, allowing only normalization of layout whitespace and line-break hyphenation. Verify ambiguous OCR against the page image. Do not silently correct, translate, splice, or present a paraphrase as an original sentence.
- Count PDF pages from 1, including cover pages. When printed page numbers differ, include both, such as `PDF p. 5 (printed p. 123)`. Verify each quotation and locator in the supplied PDF version.
- A quotation must support the specific claim, not merely mention the same topic. Distinguish the paper's own contribution from prior work it describes.
- Verify that the theme guides both the contribution and limitation, without attributing a problem, capability, or result to the paper merely because it would fit the review.
- Keep author-stated limitations distinct from your interpretation. Do not turn an assumption into a universal failure claim or describe untested performance as poor performance.
- If no defensible limitation relevant to the theme can be established, make sentence 2 say that such a limitation could not be established from the available text. In its evidence entry, explain the evidence gap instead of fabricating a limitation or quotation.
- Confirm that the opening paragraph has exactly two sentences, in contribution-then-limitation order, followed by traceable supporting sentences. Do not expand the response into a full paper review.
