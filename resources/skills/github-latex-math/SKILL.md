---
name: github-latex-math
description: 'Use whenever LaTeX math is written, reviewed or fixed in Markdown that GitHub will display: a README or docs page read in the file view, a PR or issue description, a review comment, a discussion, a wiki page. Also use when the user reports math that looks wrong on GitHub: raw $...$ text, stray commas, italic runs between formulas, "The following macros are not allowed", "Double subscripts", a formula block split into a bullet list. Covers what GitHub breaks, spellings that also work in Sphinx/MyST, Pandoc and Jupyter, the protected $`...`$ and ```math forms, and a checker script.'
---

# LaTeX math that renders on GitHub

GitHub renders math in two steps. First its Markdown parser reads the text, including everything
between the dollar signs. Then, in the browser, MathJax renders whatever still looks like
`$...$` or `$$...$$`. Almost every failure is the first step changing the formula before the second
step sees it. A formula that is valid LaTeX, and renders in Sphinx or VS Code, can therefore still
break on GitHub.

Use this skill before writing math for GitHub, and when a formula is reported broken there.

## Step 1: choose the form by where the text is read

| The text is read | Use |
| --- | --- |
| Only on GitHub (PR and issue text, comments, discussions, a GitHub-only README) | Protected forms: `` $`...`$ `` inline and a ```` ```math ```` fence for display. GitHub passes their content to MathJax untouched, so only the macro filter (below) applies. |
| On GitHub and by another tool (Sphinx/MyST, Pandoc, Jupyter, VS Code preview) | Plain `$...$` and `$$...$$`, written with the portable spellings below. The protected forms are GitHub-only: other tools show them as code. |

Mixing is fine: one risky inline formula in a PR description can use `` $`...`$ `` while the rest
stays plain.

## Step 2: avoid what the Markdown pass breaks

Each row was observed on GitHub (see [observations](references/observations.md)).

| In `$` or `$$` math | What GitHub does | Write instead |
| --- | --- | --- |
| `\,` `\;` `\:` `\!` | Drops the backslash: `a\,b` shows as "a,b" | `\thinspace` `\thickspace` `\medspace` `\negthinspace`, or `\ ` (backslash space), `\quad` |
| `\{` `\}` | Drops the backslash, the braces vanish | `\lbrace` `\rbrace` |
| Backslash + bar, for norm bars | Becomes a single bar | `\Vert` |
| `\%` `\&` `\#` `\$` | Drops the backslash, the formula errors or stops being math | Reword, or use a protected form |
| `\\` in the middle of a line, or in inline or one-line `$$...$$` math | Becomes a single backslash, the row break is lost | Put every `\\` at the end of a line inside a multi-line `$$` block, so one matrix row per line |
| `_` directly after `}` `)` `]`, with a later `_{` in the same paragraph | Reads the pair as italics: the formula stays raw text, or `&` turns into `&amp;` | Put a letter before the underscore: `\bar X_{i}` instead of `\bar{X}_{i}`, `\lbrack A \rbrack_{x}` instead of `\left(A\right)_{x}` |
| `*` directly before `)` `}` `\right` or the closing `$`, twice in a paragraph | Reads the pair as italics, the stars become underscores ("Double subscripts") | `^\ast` |
| Two `~` in one formula | Strikethrough | `\ ` (backslash space) |
| `<` followed by a letter and a later `>` | Reads an HTML tag. Math stops rendering for the rest of the page | `\lt` `\gt`, or spaces around the signs |
| `[...](...)` | Reads a Markdown link | `\lbrack` `\rbrack` |
| A bar character inside a table cell | Splits the cell, also in the protected form | `\vert` `\Vert` |

Emphasis pairs form across a whole paragraph, so two separate formulas on neighbouring lines can
break each other. A single such `_` or `*` with no partner is harmless, which is why a formula can
render alone and break once a second one is added.

## Step 3: keep display blocks intact

A `$$` block is an ordinary paragraph to the Markdown parser.

- Put `$$` on its own line, with a blank line before the opening and after the closing one.
- No blank line inside the block.
- No math line may start with `-`, `+`, `*`, `#`, `>` or `1.`: it becomes a list, heading or quote
  and the block falls apart. Move a leading sign to the end of the previous line.
- Inside a list item a `$$` block is not rendered. Use a ```` ```math ```` fence there, or move the
  formula out of the list.

## Step 4: place inline delimiters safely

- Before the opening `$`: a space, a line start or `(`. Not a letter, digit, hyphen, slash, `=`,
  `[` or a quote. `rank-$k$` stays raw text; write `rank $k$`.
- After the closing `$`: a space or sentence punctuation. Not a letter, digit, `]` or a quote, and
  not `)` when the formula itself ends in `)`.
- Keep an inline formula on one line, without spaces just inside the dollar signs.
- `\(...\)` and `\[...\]` are not math delimiters on GitHub.

## Step 5: avoid blocked macros

MathJax on GitHub refuses some macros, and one refused macro fails the whole formula with
"The following macros are not allowed: ...". This filter also applies inside the protected forms.
GitHub publishes no list.

| Macro | Status | Write instead |
| --- | --- | --- |
| `\operatorname{Var}` | Blocked (observed) | `\mathop{\mathrm{Var}}`, which keeps operator spacing, or `\mathrm{Var}` |
| `\phantom`, `\newcommand`, `\def` | Reported blocked by other users | Repeat the content; expand the macro by hand |

Treat any macro outside plain symbols, fonts, fractions, delimiters and the `aligned`, `bmatrix`,
`cases` environments as unverified until it is seen rendered.

## Step 6: check

1. Run the checker. It is offline and reports `file:line: [code] message`:

   ```bash
   python3 scripts/check_github_math.py path/to/file.md
   ```

   It covers steps 2 to 4 and the macros listed in step 5. It is a heuristic: read each finding
   before changing the text.
2. If the document may be shared, confirm what GitHub's Markdown pass does by rendering it through
   GitHub's public Markdown API and counting the math elements. This sends the text to GitHub, so
   do it only for content that is already public or that the user agrees to send:

   ```bash
   python3 -c "import json,sys; print(json.dumps({'text': open(sys.argv[1]).read(), 'mode': 'gfm'}))" file.md |
     curl -s -X POST -H "Accept: application/vnd.github+json" --data @- https://api.github.com/markdown |
     grep -o '<math-renderer' | wc -l
   ```

   Every formula should come back wrapped in `<math-renderer>` with its LaTeX unchanged. A formula
   that comes back as bare `$...$` text, or with `<em>` inside, is broken.
3. The macro filter and MathJax itself run only in the browser. The API cannot show them, so say
   that the rendered page still has to be looked at, and ask for a screenshot if something is off.

## Reporting

State which of the three checks were done. "The checker passes" is not "it renders": only a view
of the page on GitHub confirms that. When a fix changes notation the reader will see (for example
parentheses to brackets), say so; spelling changes such as `\thinspace` render the same.
