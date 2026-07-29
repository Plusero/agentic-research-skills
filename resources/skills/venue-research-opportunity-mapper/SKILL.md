---
name: venue-research-opportunity-mapper
description: "Find and critically synthesize papers from a specified conference or journal against a user's general research question. Use when the user provides a target venue and wants a venue-bounded literature map containing relevant papers, per-paper relevance and limitations, cross-paper gaps, concrete research opportunities, and a staged research plan. Do not use for a single-paper summary or a venue-agnostic systematic review."
metadata:
  short-description: "Map papers from a target venue to a research question and derive a research agenda"
---

# Venue Research Opportunity Mapper

Use this skill to answer two linked questions:

1. **Which papers in the target conference or journal are genuinely relevant to the user's research question?**
2. **What defensible research agenda follows from reading those papers together?**

The result must be more than a bibliography or a collection of abstract summaries. It should connect paper-level evidence to task-specific limitations, synthesize gaps across the selected corpus, and convert those gaps into a prioritized, executable research sequence.

## Required Inputs

The user supplies:

1. **Target conference or journal**
   - Examples: `PSCC 2026`, `IEEE Transactions on Smart Grid`, `NeurIPS 2025`.
2. **General research question**
   - Examples: `real-time LV distribution-system state estimation under sparse smart-meter measurements`, `uncertainty-aware medical image segmentation`, `efficient long-context retrieval for scientific agents`.

Do not require additional inputs. Infer sensible defaults, state material assumptions, and proceed.

## Scope Defaults

Apply these defaults unless the user specifies otherwise:

- **Named conference edition:** analyze that exact edition.
- **Recurring conference without a year:** use the most recent completed edition with published proceedings; state the exact edition and dates.
- **Journal without a date range:** search the current year to date plus the previous three complete calendar years. Expand backward, up to five years, only when fewer than five relevant papers are found.
- **Number of deeply analyzed papers:** usually 5–10; allow 3–12 when the venue contains unusually few or many strong matches.
- **Relevance threshold:** include direct, enabling, and strongly adjacent work; do not pad the list with merely keyword-adjacent papers.
- **Output depth:** technical and decision-oriented, with equations or implementation detail only when they clarify the research opportunity.

If a venue's proceedings are not yet final, label the corpus **provisional** and distinguish accepted-paper listings, preprints, and final proceedings.

## When to Use This Skill

Use it when the user asks to:

- find papers from a particular conference or journal relevant to their research;
- compare venue papers against a research problem;
- identify limitations, gaps, and future-work opportunities from a bounded paper set;
- turn a conference session, proceedings repository, journal issue, or venue search into a research plan;
- understand how recent venue papers affect their own planned contribution.

Do not use it as the primary workflow for:

- summarizing one supplied paper;
- conducting a formal systematic review or meta-analysis across the entire literature;
- producing only citation metadata;
- recommending venues for submission;
- peer-reviewing a manuscript without a venue-corpus discovery task.

## Operating Principles

### 1. Venue-bounded, question-led

Start from the official target venue corpus, but screen papers against the user's research question rather than relying only on session names or exact keywords.

### 2. Full-text first

Do not present abstract-level speculation as a paper-level finding. Read the full text of every paper that materially supports the final synthesis whenever accessible.

For each paper, record one evidence status:

- `final full text read`;
- `author manuscript/preprint read`;
- `extended abstract only`;
- `abstract only`.

When only an abstract is accessible, limit claims accordingly and say so in the output.

### 3. Separate evidence from inference

Distinguish:

- **Author-stated limitations:** explicitly acknowledged by the paper.
- **Task-specific limitations:** inferred by comparing the paper's assumptions, data, outputs, or evaluation with the user's research question.

Use phrases such as `The authors state...` and `For the user's task, an additional limitation is...`.

### 4. Do not overclaim novelty

The selected venue is not the whole literature. Phrase synthesis as:

- `not addressed by this paper set`;
- `underexplored in the selected venue corpus`;
- `a plausible opportunity suggested by these papers`.

Before calling an idea globally novel, run a lightweight sanity check in recent primary literature outside the venue. If that check is not performed or is inconclusive, do not claim global novelty.

### 5. Make opportunities executable

Avoid generic proposals such as `use a GNN`, `add uncertainty`, or `test on real data`. Each opportunity must specify:

- the gap it addresses;
- the proposed technical contribution;
- the intended evaluation;
- important dependencies or risks;
- why it matters for the user's research question.

### 6. Negative findings are useful

If a method does not appear suitable, say why. A paper can be relevant because it provides a warning, baseline, failed assumption, or boundary condition.

## Research Workflow

### Step 1 — Operationalize the user's research question

Rewrite the user's broad question internally as a structured problem map:

- **system/domain:** what object or environment is studied;
- **task:** prediction, estimation, control, identification, design, diagnosis, etc.;
- **inputs/measurements:** available, missing, delayed, noisy, or private data;
- **outputs/states:** what must be estimated or decided;
- **constraints:** physics, topology, computation, latency, safety, regulation, privacy;
- **uncertainties:** measurement, model, topology, data shift, aleatoric, epistemic;
- **evaluation goals:** accuracy, calibration, robustness, scalability, operational risk;
- **deployment regime:** offline/online, centralized/distributed, simulation/real system.

Create a compact concept map containing:

1. direct task terms;
2. domain synonyms and abbreviations;
3. enabling subproblems;
4. adjacent methods that could transfer;
5. likely failure modes.

For example, a search for `LV state estimation` should also consider measurement placement, pseudo-measurements, topology/phase identification, state forecasting, robust estimation, bad-data detection, asynchronous sensing, uncertainty quantification, and graph-temporal learning.

### Step 2 — Establish the authoritative venue corpus

Prefer sources in this order:

1. official proceedings or journal site;
2. official program/session pages;
3. publisher metadata or DOI records;
4. author-hosted accepted manuscript or preprint;
5. scholarly indexes for discovery only.

Verify for every selected paper:

- exact title;
- authors;
- venue and year;
- paper identifier, DOI, or official proceedings link where available;
- whether the source is final or preprint.

Deduplicate final papers, accepted manuscripts, and preprints. Treat title changes as possible duplicates and verify by authors/abstract/DOI.

### Step 3 — Enumerate and screen candidates

Screen the complete conference edition or the bounded journal window using title, abstract, keywords, session, and full-text search where possible.

Use three relevance classes:

- **Core:** directly addresses the user's task or principal technical bottleneck.
- **Enabling:** addresses a necessary component, such as sensing, priors, topology, robustness, calibration, or computation.
- **Adjacent:** studies a different application but provides a clearly transferable method or warning.

Score candidate relevance from 0 to 3 on each dimension:

| Dimension | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Problem overlap | unrelated | same broad domain | same subproblem | same core task |
| Method transferability | none | weak analogy | plausible transfer | directly reusable |
| Setting overlap | incompatible | partial | similar | closely matched |
| Research-opportunity value | little insight | minor | useful gap/baseline | central to agenda |

Use the weighted screening score:

\[
S = 0.35P + 0.25M + 0.20D + 0.20O.
\]

Normally deep-read papers with `S >= 1.75`, while retaining lower-scoring papers only when they supply a crucial negative result, benchmark, or complementary perspective.

If more than 12 strong papers remain, prioritize:

1. directness to the task;
2. methodological diversity;
3. evidence quality;
4. coverage of distinct bottlenecks;
5. potential to change the user's research plan.

If fewer than three papers qualify, broaden within the venue to enabling subproblems. Do not include weak papers merely to reach a target count.

### Step 4 — Retrieve and read the papers

For each selected paper, inspect at minimum:

- abstract;
- introduction and claimed contributions;
- problem formulation and assumptions;
- method/architecture/algorithm;
- data, test systems, or experimental setup;
- baselines and ablations;
- quantitative and qualitative results;
- limitations, discussion, and conclusion;
- appendices or supplementary material when necessary for assumptions or implementation.

When the paper is a PDF, inspect relevant figures, diagrams, tables, and equations rather than relying only on extracted text. Use page screenshots when a figure or table carries an important claim.

Do not use a scholarly discovery tool's generated summary as the sole evidence for a method, result, or limitation.

### Step 5 — Build an evidence card for each paper

Use the internal template in `references/paper-evidence-card.md`.

Capture:

- bibliographic identity and evidence status;
- problem and motivation;
- method and main components;
- assumptions and measurement/data regime;
- outputs and uncertainty representation;
- datasets/test systems and realism;
- baselines, metrics, and principal results;
- author-stated limitations;
- task-specific limitations inferred for the user;
- transferable ideas;
- candidate research opportunities;
- confidence in each claim.

Do not write the final report until evidence cards exist for all selected papers.

### Step 6 — Analyze each paper against the user's task

For each paper, answer six questions:

1. **What does the paper actually do?**
2. **Why is it relevant to the user's research question?**
3. **Which components, assumptions, baselines, or evaluation ideas are worth borrowing?**
4. **What limitations matter for the user's intended task?**
5. **What new research question follows from those limitations?**
6. **What role should the paper play in the user's project: foundation, baseline, module, warning, or comparator?**

The discussion must be task-specific. Do not repeat the abstract and then append a generic `future work` sentence.

### Step 7 — Synthesize cross-paper gaps

After paper-level analysis, create a gap matrix with papers as columns and the following candidate dimensions as rows:

- problem formulation and scope;
- measurement realism and observability;
- data availability and data shift;
- model assumptions and physical consistency;
- spatial, temporal, or cross-modal dependencies;
- uncertainty representation and calibration;
- topology, phase, or parameter uncertainty;
- missing data, delays, and asynchronous measurements;
- bad data, cyber resilience, and anomaly attribution;
- simulation-to-real and cross-system generalization;
- operational metrics and decision usefulness;
- computational cost, latency, and scalability;
- privacy, communication, and governance;
- reproducibility, ablations, and benchmark quality.

Only report gaps supported by at least one of the following:

- several papers share the omission;
- one highly relevant paper exposes a critical limitation;
- two papers make incompatible assumptions that reveal an unresolved tradeoff;
- the venue corpus addresses components separately but not jointly.

For every cross-paper gap, state:

1. what the papers cover;
2. what remains unresolved;
3. why the unresolved issue matters for the user's task;
4. which papers provide the evidence.

Do not label the absence of an irrelevant feature as a gap.

### Step 8 — Generate and prioritize research opportunities

Derive each opportunity from an explicit chain:

\[
\text{paper evidence} \rightarrow \text{task-specific gap} \rightarrow
\text{proposed contribution} \rightarrow \text{evaluation plan}.
\]

For each opportunity, define:

- **research question or hypothesis**;
- **evidence base:** which papers motivate it;
- **technical contribution:** model, estimator, dataset, theory, benchmark, or system;
- **evaluation design:** datasets/test systems, baselines, metrics, stress tests, ablations;
- **expected value:** scientific and practical significance;
- **dependencies:** data, simulator, labels, hardware, partner access;
- **risks:** identifiability, computation, confounding, unavailable ground truth, weak novelty;
- **scope:** standalone paper, thesis chapter, or longer-term program.

Rank opportunities from 1 to 5 using:

| Criterion | Weight |
|---|---:|
| Fit to the user's research question | 30% |
| Strength of evidence from the paper set | 20% |
| Potential contribution clarity | 20% |
| Feasibility with likely data/resources | 20% |
| Differentiation from the selected papers | 10% |

Use the ranking to distinguish:

- **best near-term paper**;
- **highest-upside research direction**;
- **enabling infrastructure work**;
- **longer-term/high-risk extension**.

### Step 9 — Build the recommended research sequence

Order the work by dependency and risk, not by how exciting the ideas sound.

A typical sequence is:

1. **Problem definition and defensible baseline**
2. **Data/measurement realism and evaluation protocol**
3. **One isolated methodological contribution**
4. **Integrated model or estimator**
5. **Robustness, generalization, and uncertainty validation**
6. **Real-system or operational validation**

Tailor the sequence to the user's question. For every stage, provide:

- objective;
- concrete deliverable;
- required inputs or dependencies;
- minimum baselines;
- primary evaluation criteria;
- stop/go condition;
- likely publication or thesis value.

Prefer a sequence in which each stage yields a useful artifact or publishable result even if later stages fail.

### Step 10 — Run a contradiction and overclaim check

Before drafting, verify:

- papers are genuinely from the target venue and scope;
- no final/preprint duplicates remain;
- numerical claims match the paper;
- forecasting, estimation, identification, and control are not conflated;
- paper-stated and inferred limitations are separated;
- inaccessible full texts are clearly marked;
- opportunities follow from evidence rather than fashion;
- `novel`, `first`, and `unexplored` are not used without broader verification;
- the recommended sequence is technically dependent and practically feasible.

### Step 11 — Write the final answer

Use the exact reader-facing structure in `references/output-template.md` unless the user requests a different format.

Open with a concise overall assessment that states:

- how many papers were screened and selected;
- which papers or themes are most relevant;
- the central conclusion for the user's research plan;
- important evidence-access limitations.

Then provide the required five outputs:

1. relevant-paper list;
2. per-paper discussion with introduction, limitations, and opportunities;
3. cross-paper gaps;
4. prioritized research opportunities;
5. recommended research sequence.

## Citation and Evidence Rules

- Cite every paper-specific factual claim near the claim.
- Prefer official proceedings, publisher pages, or the paper itself.
- When using a preprint for full-text analysis, identify it as a preprint or accepted manuscript.
- Use secondary scholarly databases for discovery and metadata cross-checking, not as the sole source of substantive claims.
- Avoid long verbatim quotations; paraphrase accurately.
- For a numerical result, record the metric, test setting, and comparator needed to interpret it.
- If versions disagree, prioritize the final published version and note meaningful version differences.
- If the user supplied papers or a repository, inspect those sources before searching more broadly.

## Progress Updates for Long Runs

For a substantial corpus, keep the user informed without exposing low-level tool operations:

1. After corpus screening, report the number of papers found, shortlisted, and excluded.
2. After deep reading, share one or two emerging themes or warnings.
3. Before final synthesis, mention any material access limitation or scope adjustment.

Do not promise future/background delivery. Complete the best available analysis in the current run.

## Output Standards

### Relevant-paper list

Use a compact table with:

- paper title;
- authors/year;
- relevance class (`Core`, `Enabling`, `Adjacent`);
- reason for inclusion;
- evidence status.

Order by relevance to the user's task, not program order or citation count.

### Paper-by-paper discussion

For every paper, use this structure:

1. **What the paper does**
2. **Why it matters for the user's task**
3. **What to borrow**
4. **Limitations**
   - author-stated, when available;
   - task-specific/inferred;
5. **Research opportunity**
6. **Role in the user's project**

The research opportunity should usually be one focused paragraph, not a list of unrelated ideas.

### Cross-paper gaps

Group gaps into 3–7 themes. Use insight-bearing headings such as:

- `Probabilistic outputs are not yet demonstrably calibrated`
- `Topology uncertainty is separated from state uncertainty`
- `Sensor placement and estimator design are optimized independently`

For each gap, cite the papers that establish it and explain the consequence for the user's task.

### Research opportunities

Provide 3–6 opportunities. For each, include:

- concise name;
- research question;
- proposed contribution;
- evaluation plan;
- main risk;
- priority classification.

Prefer a mix of near-term, high-upside, and enabling opportunities.

### Recommended research sequence

Provide 4–6 ordered stages. Explain why each stage precedes the next. Include tangible deliverables and decision gates.

### Optional closing synthesis

When useful, end with one proposed central research question that unifies the strongest opportunity. Label it as a proposed framing, not as a proven novelty claim.

## Failure Modes to Avoid

Do not:

- return only titles and abstracts;
- treat every keyword match as relevant;
- summarize papers without relating them to the user's question;
- invent limitations that are not supported by the method or experiments;
- report an inferred limitation as though the authors acknowledged it;
- call an idea novel based only on one conference or journal;
- use generic research opportunities detached from measurable experiments;
- propose an integrated end-to-end system before establishing baselines and data validity;
- hide that a paper was assessed from its abstract only;
- confuse better point accuracy with calibrated uncertainty;
- equate synthetic benchmark performance with deployment readiness;
- produce a research sequence without dependencies, baselines, or stop/go criteria.

## Quality Bar

Before handoff, confirm all of the following:

- [ ] The target venue and exact time/edition scope are explicit.
- [ ] Every selected paper belongs to the scoped venue corpus.
- [ ] Final versions and preprints are deduplicated.
- [ ] The paper list is ranked by relevance to the user's question.
- [ ] Every paper has an introduction, task-specific relevance discussion, limitations, and at least one grounded opportunity.
- [ ] Evidence status is disclosed for every paper.
- [ ] Paper-stated and inferred limitations are clearly separated.
- [ ] Cross-paper gaps are evidence-backed and material to the user's task.
- [ ] Research opportunities specify a contribution and evaluation path.
- [ ] Global novelty is not claimed without a broader literature check.
- [ ] The recommended sequence follows technical dependencies and yields intermediate deliverables.
- [ ] Citations support the substantive claims.
- [ ] The answer directly reflects the user's research question rather than using a generic literature-review template.

## Supporting Files

- `references/paper-evidence-card.md` — internal extraction template for each selected paper.
- `references/output-template.md` — required reader-facing report structure.
- `examples/example-request.md` — example invocation and scope interpretation.
