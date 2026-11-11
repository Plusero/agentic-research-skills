# Observations behind the rules

Read this when a rule in `SKILL.md` seems wrong or GitHub's behaviour may have changed: it records
what was tested, so the test can be repeated.

## How it was observed

- **Date:** 11 November 2026.
- **Markdown pass:** about 100 short test cases sent to `POST https://api.github.com/markdown` with
  `"mode": "gfm"`. In the returned HTML a formula that GitHub accepts is wrapped in
  `<math-renderer class="js-inline-math">` or `js-display-math`, with the LaTeX it will hand to
  MathJax. `"mode": "markdown"` returns no math elements at all, so it is not useful here.
- **File view and macro filter:** seen in the GitHub file view of a real documentation page: the
  `\operatorname` error, commas from `\,`, stars turned into underscores, and a display block split
  by a line starting with `-`. These agree with the API results.
- **Not observable through the API:** the macro filter and MathJax errors, which run in the browser.

One test contaminates the rest: an unclosed HTML-like tag (`$a <b> c$`) stops math detection for
everything after it in the same document. Test such cases in a request of their own.

## Results

"Math" means the formula came back as a math element with its LaTeX intact.

### Backslash before punctuation

| Input | Result |
| --- | --- |
| `$a\,b$`, and the same in a multi-line `$$` block | Math, but the content is `a,b` |
| `\;` `\:` `\!` in a `$$` block | Content is `;` `:` `!` |
| `$\{x\}$`, `$\left\{ a \right\}$` | Content is `{x}`, `\left{ a \right}` |
| Norm bars written as backslash + bar | Content is plain bars |
| `$a\%$`, `$a\&b$`, `$a\#$`, `$a\_b$` | Backslash dropped |
| `$\$4$` | Not math |
| `\\` at the end of a line in a multi-line `$$` block, also followed by spaces | Kept |
| `\\` mid-line in a multi-line `$$` block (`\begin{bmatrix} G & Q \\ R & S \end{bmatrix}` on one line) | Becomes `\ ` |
| `\\[4pt]` | Becomes `\[4pt]` |
| `$a \\ b$`, `$$\begin{bmatrix} a \\ b \end{bmatrix}$$` on one line | Becomes `\ ` |
| `\thinspace` `\medspace` `\mkern3mu` `\ ` `~` `\lbrace` `\rbrace` `\lbrack` `\rbrack` `\vert` `\lvert` `\lt` `\ast` `\tag{1}` | Kept |

### Emphasis

| Input | Result |
| --- | --- |
| `$X_{i} = Y_{j}$`, `$x_1 y_1$`, `$x_\mathrm{a} y_\mathrm{b}$`, `$\text{a_b}$` | Math |
| `$\bar{X}_{i} = Y \Phi_{j}^T$` | Not math, `<em>` from the first `_` to the second |
| `$\bar{A}_{x}$ and $C_{y}$`, also when the two are on different lines of one paragraph | Not math |
| `$C_{y}$ and $\bar{A}_{x}$` (the order reversed) | Math |
| `$\bar{A}_{x}$ and $b$` (no partner) | Math |
| `$\hat{y}_i + \hat{z}_i$`, `$\mathbf{a}_i \mathbf{b}_j$` | Math |
| `$\hat{y}_i + z_{k}$` | Not math |
| `$\left(C_{x}\right)_{vv}$ and $C_{y}$`, `$[C_{x,ii}]_{\theta\theta}$ and $[C_{x,ii}]_{vv}$` | Not math |
| `$\lbrack C_{x} \rbrack_{vv}$`, `$\bar X_{i}$` | Math |
| Multi-line `$$` with `\bar{X}_{i} = \left(Y\right)_{j}` | Math, content intact |
| Multi-line `$$` with `aligned`, `\text{Test}_b &= x_1\\` and `q_{y+1} &= q` | Math element, but `&` is double-escaped and blank lines are inserted |
| `$a^* b^*$`, `$a^* b$`, `$$` with `w_i^* + w_s^*` | Math |
| `$(a^*) + (b^*)$`, `$a^{*} b^{*}$`, `$a^*$ and $b^*$` | Not math |
| Multi-line `$$` with `\left(w_i^*\right) \left(w_s^*\right)` | Math element, but each `*` is now `_` |
| `$a^\ast b^\ast$` | Math |
| `$a~b~c$` | Not math, strikethrough |
| `**$a_{i}$**` | Math. `*$b$*` is not |

The rule that fits all rows is CommonMark's: an underscore can open emphasis when it follows
punctuation or a space and precedes a non-space, and can close it when it follows a non-space and
precedes punctuation or a space. An underscore between two letters or digits does neither. A star
needs only the non-space on the relevant side.

### Block structure

| Input | Result |
| --- | --- |
| `$$` lines with a blank line before and after | Math |
| `$$a\,b$$` on one line, and `$$a + b$$` inside a sentence | Math (inline in the sentence) |
| Text line directly before the opening `$$`, or directly after the closing `$$` | Not math |
| Blank line inside the block | Not math |
| A math line starting with `- `, `+ `, `# `, `1. ` or `> ` | Block split into a list, heading or quote |
| A math line starting with `=` | Math |
| `$$` block indented by three spaces, or inside a `>` quote | Math |
| `$$` block inside a list item | Not math |
| ```` ```math ```` fence, also inside a list item, with `\,`, `\{`, `_`, `*`, a leading `-` and `\\` | Math, content intact |

### Inline delimiters and other syntax

| Input | Result |
| --- | --- |
| `($a$)`, `f($a$)`, `$a$-th`, `$a$.`, `$a$,`, `$a$;`, `$a$:`, `$a$!`, `$d$=y` | Math |
| `rank-$k$`, `a/$b$`, `x=$c$`, `~$e$`, `[$a$]`, `'$a$'`, `"$a$"` | Not math |
| `2$a$`, `$b$2`, `n$c$`, `$d$n`, `x$a$y`, `$ a $` | Not math |
| `(see $f(a)$)` | Not math. `(see $b$)` and `( $f(c)$ )` are math |
| `It costs $5 and $10 today.` | Not math, as intended |
| Inline formula split over two lines | Not math (comment rendering, where a newline is a line break) |
| `\(a+b\)`, `\[ ... \]` | Not math |
| `$i<k$`, `$a<b$ and $c>d$`, `$a < b$`, `$$` with `a <b` | Math |
| `$a <b> c$` | Not math, and no math after it in the document |
| `$[a+b](c+d)$` | Not math, a link |
| Table cell with a formula that contains bar characters, plain or protected | Cell split. `$\vert x \vert$` is math |
| `` $`a\,b \{x\} \bar{X}_{i} = Y_{j}^* (z^*) [a](b)`$ `` | Math, content intact |
| `$\mathop{\mathrm{Var}}(x)$`, `$\mathrm{Var}(x)$`, `$\text{Var}(x)$` | Math (the macro filter was not exercised) |

## Other reports

Not reproduced here, listed so they can be checked:

- `\operatorname` stopped rendering in early 2023; `\mathop{\mathrm{...}}` is the usual
  replacement ([github/markup#1688](https://github.com/github/markup/issues/1688)).
- `\phantom` is blocked, and `\operatorname*{x}` can be written `\mathop{\mathrm{x}}\limits`
  ([rohitg00/ai-engineering-from-scratch#599](https://github.com/rohitg00/ai-engineering-from-scratch/pull/599)).
- `\newcommand` worked at launch and was removed
  ([nschloe, 2022](https://nschloe.github.io/2022/05/20/math-on-github.html)).
- A raw `#` inside `\text{...}` fails in a math fence; a bare `<` before a letter can unbalance
  braces ([thiagomata/prime-numbers#65](https://github.com/thiagomata/prime-numbers/pull/65)).
- The protected inline form was introduced in May 2023
  ([GitHub docs](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions),
  [community discussion #36915](https://github.com/orgs/community/discussions/36915)).
