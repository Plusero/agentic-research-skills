---
name: topic-literature-search
description: Search IEEE Xplore, arXiv, and Google Scholar for papers on a user-specified research topic, rank the ten most relevant results, and produce a sourced literature summary. Use when the user asks for related papers, a literature scan, a paper shortlist, or a research summary for a topic.
---

# Topic Literature Search

## Instructions

1. Identify the research topic, plus any constraints the user provides:
   - Subtopic or method
   - Application domain
   - Year range
   - Preference for surveys, seminal papers, or recent papers

2. Convert the request into 3 to 6 search queries:
   - One broad query for the full topic
   - One or more synonym or acronym variants
   - One query for recent work
   - One query for surveys or review papers when useful

3. Search these sources:
   - IEEE Xplore for peer-reviewed engineering and computer science papers
   - arXiv for recent preprints and emerging work
   - Google Scholar for broad coverage, citation signal, and older foundational papers

4. Build a candidate pool of at least 15 verified papers before ranking the final 10.

5. Verify every candidate before including it:
   - Confirm the title, authors, year, and venue from the source page or publisher page
   - Prefer DOI, publisher, or arXiv links over secondary reposts
   - If Google Scholar is used for discovery, verify bibliographic details from an authoritative page before finalizing
   - Do not invent missing metadata

6. Deduplicate results by title, DOI, or arXiv identifier.

7. Rank papers by relevance using these factors:
   - Direct match to the user's topic
   - Methodological match
   - Venue credibility
   - Citation signal or field influence
   - Recency when the topic is fast-moving
   - Survey value if the user needs broad orientation

8. Select the 10 most relevant verified papers.
   - Balance seminal and recent papers when both matter
   - If fewer than 10 verified papers are available, say so explicitly and return the verified set

9. Summarize each selected paper.
   - Use the abstract and full text when available
   - If only metadata or abstract is accessible, say that the summary is based on the abstract
   - Keep summaries grounded in the source and specific to the paper's actual contribution

10. Return the results in Markdown using the exact section order below.

## Output Format

Use this template. Repeat the `Top 10 Papers` item format for each selected paper.

```markdown
# Literature Search: <topic>

## Search Scope
- Topic: <topic>
- Constraints: <constraints or "None">
- Databases searched: IEEE Xplore, arXiv, Google Scholar
- Search queries: <comma-separated queries>
- Notes: <access limitations or "None">

## Top 10 Papers

1. **<paper title>**
   - Authors: <authors>
   - Year: <year>
   - Venue: <venue or "arXiv">
   - Source: <IEEE Xplore | arXiv | Google Scholar + verified source>
   - Link: <url>
   - Why relevant: <one sentence>
   - Summary: <2 to 4 sentences on the paper's problem, method, and key result>
   - Evidence basis: <full text | abstract | metadata plus abstract>
```

## Guardrails

- Verify bibliographic details before presenting them.
- Prefer authoritative links and accessible abstracts over citation-only pages.
- Separate discovery from verification: Google Scholar can help find papers, but final metadata should come from an authoritative source when possible.
- Do not present fabricated citations, authors, years, venues, or claims.
- If multiple papers are near-duplicates, keep the strongest or most complete version.
- If the topic is broad, prefer a mix of surveys and primary papers.
- If the topic is narrow, prefer direct methodological matches over highly cited but tangential papers.
- If access to a source is blocked, state the limitation clearly.
