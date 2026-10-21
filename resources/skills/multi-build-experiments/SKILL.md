---
name: multi-build-experiments
description: 'Use when setting up, running, resuming or organizing scientific experiments that compare several builds or compile-time variants of one project (methods, schemes, flags, solvers): source/worktree/branch layout, one isolated build and environment per variant, one-command campaign and export scripts, run IDs, results folder contract (runs, derived, retained, archives, scratch), provenance, caching and commit rules.'
---

# Multi-build scientific experiments

Compare several builds of one code base (variants chosen by a build option) on frozen
inputs. Adapt names; keep the rules. A project's own experiment plan wins where it is
more specific.

## Repositories, branches and worktrees

| Role | Where | Rules |
|---|---|---|
| Development | Project repo, branch `dev` / `feature/*`. | Everyday work. Never measured, never reset for an experiment. |
| Measured source | Project repo, tag `measured/<campaign>`, one **detached** worktree. | Clean, never edited, never `git clean`ed (it holds the builds). One `build/<variant>/` and `environments/<variant>/` per variant. |
| Experiment repo | A **separate** Git repository (own history), not a branch or worktree of the project. | Configs, scripts, docs, results. `main` plus short-lived `topic/*`. |

- All variants of a campaign build from the same tag; never one branch or worktree per variant.
- Freeze sources with tags, not moving branches. A source change means a new tag and a new
  measured worktree; remove the old one only after its tag and binaries are archived.
- Variants share nothing mutable: separate build dirs and non-editable environments, a
  mapping file (variant → build, interpreter, library), and a hash check in every worker.
- Launch campaigns from a committed experiment-repo state; the run records that commit.
- To measure: tag the tested commit, then
  `git -C solver worktree add --detach ../solver-measured measured/<campaign>`.

**Example branches and tags** for a project `solver` with variants `a`, `b`, `c`, and the
worktree each one is checked out in:

```text
solver repo                                   solver-experiments repo (separate)
  dev                     -> solver/            main
  feature/new-variant     -> solver/            topic/<name>
  tag measured/comparison -> solver-measured/
```

**Example folder tree** for the same project: two worktrees of the solver repo and the
separate experiment repo side by side.

```text
<workspace>/
  solver/                      # solver repo, branch dev
  solver-measured/             # solver repo, detached at measured/comparison
    build/{a,b,c}/
    environments/{a,b,c}/      # ignored
  solver-experiments/          # SEPARATE repo (own .git), never solver source
    configs/experiment-<campaign>.json   # variants, inputs, settings, tag + commit
    configs/variants.<run-id>.local.json # variant -> build mapping (ignored)
    inputs/                    # frozen, hash-verified
    src/<pkg>/layout.py        # all result paths from the run ID
    run_campaign.py  export_results.py  run_all.py  check_results_layout.py
    results/
      runs/<run-id>/           # immutable measurements
      derived/<run-id>/{analysis,exports,logs}/
      retained/<id>/           # tracked publications
      archives/  scratch/
```

## Commands

Provide these entry points (or use the project's existing ones):

| Command | Does |
|---|---|
| `run_campaign.py` | Build every variant, run untimed smoke checks, accuracy runs, audit, timing. |
| `export_results.py --run <run>` | Tables and figures from a finished run; never measures. |
| `run_all.py` | Both. |

- `--dry-run` prints the plan; measurements start only with `--yes`, and agents pass
  `--yes` only when the user asked for the campaign.
- Rerunning the same command resumes: finished steps are skipped, stages are cached by
  input/code identity.
- Fail closed: a failed step stops and names its log; never relax checks, overwrite an
  unfinished attempt, or measure from analysis/export.
- Timing: serial, one thread, idle machine, warmup plus repeats, validation outside the clock.
- Show progress (live bar, plus `progress.json` for other shells). No inline `#` comments
  in documented commands (zsh passes them as arguments).

## Results contract

Everything keyed by one run ID, `<project>-<campaign>-<date>`.

| `results/` | Holds | Rules |
|---|---|---|
| `runs/<run-id>/` | Config, frozen inputs, raw results, timing, manifest with hashes. | Immutable; Git-ignored. |
| `derived/<run-id>/` | `analysis/`, `exports/`, `logs/`. | Analysis and exports regenerable; Git-ignored. |
| `retained/<id>/` | Compact report, tables, figures, hashes. | Tracked, read only, in `catalog.json`. |
| `archives/` | Tarballs, bundles, checksums. | Git-ignored. |
| `scratch/` | Probes, failed attempts. | Disposable. |

A check script enforces this (no unknown folders, nothing derived inside `runs/`, no
tracked ignored files). Never rewrite manifests or move evidence something refers to.

## Commits

Run tests, linter and the layout check per checkpoint; stage explicit paths; run
`git diff --cached --check`. Respect signing unless the user waives it. Never commit
`runs/`, `derived/`, `archives/`, `scratch/`, builds, environments or local mappings.
