---
name: topic-literature-search
description: Search IEEE Xplore, arXiv, and Google Scholar for papers on a user-specified research topic, score verified candidates, and produce a sourced shortlist of up to ten papers. Use when the user asks for related papers, a literature scan, a paper shortlist, or a research summary for a topic.
---

# Topic Literature Search

## Workflow

1. Record up to four topic concepts and any supplied method, application domain, year range, publication-type preference, or exclusion criterion. Record supplied acronyms and synonyms under the corresponding topic concept.
2. Generate three to six queries:
   - one query containing all recorded topic concepts;
   - one query for each recorded acronym or synonym absent from the first query;
   - one query with the lower bound of the requested year range, or the current year minus five when the user asks for recent work without defining a range;
   - one query containing `survey` OR `review` when the user requests an overview, survey, or review.
3. Search IEEE Xplore, arXiv, and Google Scholar. Record any source that could not be queried.
4. Build a pool of at least 15 unique candidates, unless fewer than 15 can be verified. Deduplicate by DOI, then arXiv ID, then case-folded title with punctuation removed.
5. Verify title, author list, year, venue, DOI or arXiv ID, and abstract against an IEEE Xplore record, publisher page, DOI landing page, arXiv record, or Crossref record. Do not use Google Scholar as the final source for a bibliographic field.
6. Exclude a candidate that violates a user-specified year, language, publication type, domain, or method constraint.
7. Score each remaining candidate:
   - topic terms: 0–4 points, one point for each recorded topic concept whose term, acronym, or recorded synonym occurs in the title or abstract;
   - method: 2 points when the requested method is used by the paper, 1 when it appears only as a baseline or comparator, and 0 when absent;
   - application domain: 2 points when experiments use the requested domain, 1 when the domain appears only in motivation or related work, and 0 when absent;
   - publication type: 1 point when it matches the user's requested type, otherwise 0; award 1 point to any type when none was requested;
   - evidence availability: 1 point for accessible full text, 0.5 for an accessible abstract, and 0 for metadata only.
8. Sort by total score, then by the topic-term score, then by publication year descending. Select the first ten. If fewer than ten candidates remain, return all of them and report the count.
9. For each selected paper with an abstract or full text, write two to four sentences covering the stated problem, method, and reported result. For metadata-only records, write one sentence containing only title-derived scope, year, and venue. Mark the evidence basis as `full text`, `abstract`, or `metadata only`.
10. Return Markdown in the section order below.

## Output Format

```markdown
# Literature Search: <topic>

## Search Scope
- Topic: <topic>
- Constraints: <constraints or "None">
- Databases searched: <successfully queried databases>
- Unavailable databases: <databases and failure reason, or "None">
- Search queries: <queries separated by semicolons>
- Verified candidate count: <number>
- Scoring: topic 0–4; method 0–2; domain 0–2; publication type 0–1; evidence 0–1

## Ranked Papers

1. **<paper title>**
   - Authors: <authors>
   - Year: <year>
   - Venue: <venue or "arXiv">
   - Identifier: <DOI or arXiv ID>
   - Verified at: <IEEE Xplore | publisher | DOI | arXiv | Crossref>
   - Link: <verification URL>
   - Score: <total>/10 (topic <n>/4; method <n>/2; domain <n>/2; type <n>/1; evidence <n>/1)
   - Matched criteria: <topic concepts, method, domain, and type that earned points>
   - Summary: <problem, method, and reported result>
   - Evidence basis: <full text | abstract | metadata only>
```

## Checks

- Open every verification URL before delivery.
- Match every output field to the verification record; write `Not reported` instead of guessing.
- For a journal/conference version and its preprint, retain the journal/conference version and link the preprint as an additional full-text source. Retain the preprint instead only when the user requests preprints or it contains a later revision.
- Do not cite a search-results page as the verification URL.
- State each database access failure in `Unavailable databases` with the returned error or access restriction.
