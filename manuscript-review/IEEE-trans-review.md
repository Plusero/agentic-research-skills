---
name: ieee-trans-review
description: This skill gives the agent instructions on how to review a IEEE trans paper.
---

# IEEE Transactions Paper Review Skill

This skill provides detailed instructions for reviewing a paper submitted to an IEEE Transactions journal. Apply every checklist item below systematically and report findings clearly, grouping them by section.

## When to Use

- Use this skill when the user asks you to review, proofread, or provide revision feedback on an IEEE Transactions paper.
- This skill is also helpful when the user wants to self-check a draft before submission or when responding to reviewer comments.

## Instructions

### 1. Citation Style

- Use IEEE numbered citation format: references are cited as bracketed numbers in order of appearance, e.g., [1], [2], [3].
- Every in-text citation must have a corresponding entry in the reference list, and vice versa.
- Reference list entries must follow IEEE style.
- Journal and conference names must use standard IEEE abbreviations (see IEEE Editorial Style Manual).
- Include a DOI for every reference where one is available.
- References must be listed in the order they first appear in the text, not alphabetically.
- Verify that all cited work is real, accessible, and accurately described.

### 2. Abbreviations

- Every abbreviation (acronym) must be defined at its **first appearance in the abstract** and again at its **first appearance in the main text** (body), because the abstract is read independently.
- The capitalization of the full name must be consistent every time it appears. Capitalize only proper nouns and terms whose capitalization is part of the official name (e.g., "Internet of Things" → IoT); generic technical terms use lowercase (e.g., "deep neural network" → DNN, "convolutional neural network" → CNN).
- After the abbreviation is introduced, use only the abbreviation (do not alternate between the full name and the abbreviation).
- Standard, universally recognized abbreviations that do not need definition: IEEE, AC, DC, RF, MIMO, AI, CPU, GPU, RAM. If in doubt, define it.
- Abbreviations that appear fewer than three times in the full paper should be written out in full each time and the abbreviation omitted.
- Do not introduce abbreviations in section headings, figure captions, or table captions without also defining them in the body text.

### 3. Figures

- Every figure must be explicitly referenced and discussed in the main text before or at the point where it appears (e.g., "as shown in Fig. 1," or "Fig. 2 illustrates…"). A figure that is never mentioned in the text must be added to the text or removed.
- Use "Fig." (not "Figure") when referring to a figure in the main text; spell out "Figure" only at the start of a sentence.
- Figures must be vector graphics (PDF, EPS, SVG) whenever possible. Raster images (PNG, TIFF) must be at least 300 DPI for photographs and 600 DPI for line art.
- Axes labels, legends, and annotations must be large enough to be legible after the figure is scaled to a single column (~8.8 cm) or double column (~18.1 cm) width.
- All colors used in figures should remain distinguishable when printed in grayscale (use different line styles or markers in addition to color).
- Multi-part figures must label each sub-figure as (a), (b), (c), etc., and each sub-figure label must be referenced in the caption and in the text.
- Figure captions must be self-contained: a reader should understand what the figure shows without reading the body text. Each caption should end with a period.

### 4. Tables

- Every table must be referenced and discussed in the main text (e.g., "Table I compares…").
- Use Roman numerals for table numbers (Table I, Table II, …).
- Table captions appear **above** the table and should be concise but self-explanatory.
- Column and row headers must clearly specify the quantity and its unit (e.g., "Latency (ms)").
- Align numerical data to decimal points or right-align for readability.

### 5. Mathematical Notation

- All equations that are referenced in the text must be numbered with right-aligned numbers in parentheses, e.g., (1), (2).
- Scalar variables are typeset in italic (e.g., *x*, *N*).
- Vectors are typeset in bold lowercase italic (e.g., **x**); matrices in bold uppercase italic (e.g., **X**) or as specified by the journal's style guide.
- Units must follow SI conventions and must not be italicized.
- Verify dimensional consistency and that every symbol is defined the first time it is used.
- Avoid starting a sentence with a mathematical symbol; rephrase if necessary.

### 6. Paper Structure

Verify that the paper contains the following standard sections in order, and flag any that are missing or out of place:

1. **Title** — concise, specific, and accurately reflecting the contribution.
2. **Abstract** — 150–250 words; must state the problem, proposed method, key results, and significance without citations or undefined abbreviations.
3. **Index Terms** — 3–8 keywords listed alphabetically; follow IEEE taxonomy when applicable.
4. **Introduction** — motivates the problem, reviews related work at a high level, and clearly states the paper's contributions (usually as a bulleted list).
5. **Related Work / Background** — thorough survey of prior art; clearly differentiates the proposed work from existing approaches.
6. **Methodology / Proposed Approach** — detailed enough for a knowledgeable reader to reproduce the work.
7. **Experiments / Results** — includes dataset descriptions, evaluation metrics, baselines, and quantitative comparison.
8. **Discussion** — interprets results, discusses limitations, and suggests future work.
9. **Conclusion** — summarizes contributions and findings; does not introduce new information.
10. **Acknowledgment** *(if applicable)* — funding sources, institutional support.
11. **References** — formatted per Section 1 above.
12. **Appendix** *(if applicable)* — supplementary proofs or derivations.

### 7. Grammar and Writing Style

- Use the **Oxford (serial) comma** before the conjunction in a list of three or more items (e.g., "speed, accuracy, and robustness").
- Prefer the **active voice** where it improves clarity (e.g., "We propose…" rather than "A method is proposed…").
- Avoid contractions (e.g., don't → do not, it's → it is, can't → cannot).
- Use "which" for non-restrictive clauses (preceded by a comma) and "that" for restrictive clauses (no comma).
- Avoid vague hedging language such as "very," "quite," "rather," and "a lot."
- Check subject–verb agreement, especially in long sentences with intervening clauses.
- Ensure consistent verb tense: present tense for established facts and the paper's own contributions; past tense for describing experiments already performed.
- Spell out numbers below ten unless they appear with a unit (e.g., "three methods" but "3 ms").
- Do not begin a sentence with a numeral; rephrase or spell out the number.
- Avoid starting consecutive sentences with the same word or phrase.

### 8. Formatting and Length

- Verify that the paper uses the correct IEEE Transactions template (double-column, 10 pt font for the body, Times New Roman or equivalent).
- Check that page count does not exceed the maximum allowed by the specific Transactions venue; flag if it is close to the limit.
- Section headings: first-level headings are in Roman numerals and small caps (e.g., **I. INTRODUCTION**); second-level headings in italics.
- Ensure there are no orphaned headings (a heading at the very bottom of a column with no body text following it).
- Footnotes should be used sparingly; prefer incorporating information into the main text.

### 9. Ethical and Submission Requirements

- Check that the paper does not appear to be a verbatim or near-verbatim copy of previously published work (self-plagiarism or plagiarism).
- Confirm that human/animal study approvals are mentioned if the research involves human subjects or animals.
- Verify that any use of AI-generated text is disclosed in accordance with IEEE policy.
- Confirm that code, data, or supplementary material availability statements are included where applicable.

### 10. Output Format

When reporting review findings, structure the output as follows:

1. **Summary** — a short paragraph (3–5 sentences) giving an overall impression of the paper's strengths and main weaknesses.
2. **Major Issues** — numbered list of issues that must be fixed before the paper can be accepted (e.g., missing experiments, incorrect methodology, fundamental writing problems).
3. **Minor Issues** — numbered list of smaller issues (e.g., formatting errors, unclear sentences, missing citations for specific claims).
4. **Suggestions** (optional) — recommendations that would improve the paper but are not required.

Provide the specific location (section name, paragraph number, or equation/figure/table number) for every issue reported.

