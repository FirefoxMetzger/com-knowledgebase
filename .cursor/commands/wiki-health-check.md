# Wiki health check (lint, gaps, opportunities)

You are auditing and improving the integrity of the Markdown wiki under `wiki/` against the contents of `raw/`. This is a **maintenance pass**, not new research unless needed to fix clear gaps.

## What to check

1. **Coverage**  
   List important items in `raw/` that lack a wiki summary or link. Propose concrete new stubs or sections.

2. **Consistency**  
   Flag contradictory claims across articles, duplicate concept pages, mixed terminology for the same idea, or outdated statements that conflict with newer `raw/` material.

3. **Graph quality**  
   Find orphan notes (few or no inbound links), broken wiki links, and missing “see also” connections between obviously related pages.

4. **Indexes**  
   Check whether hub/index pages still reflect the true shape of the wiki; suggest updates.

5. **Follow-ups**  
   Propose high-value questions to explore next, new concept articles, or merges/splits of existing pages.

## Output

- Write a dated Markdown report under `outputs/` (e.g. `outputs/health-checks/`) listing findings in priority order.  
- Apply **small, safe fixes** directly in `wiki/` when they are unambiguous (typos, obvious link repairs, adding missing backlinks).  
- For anything uncertain or substantive, describe the change in the report and wait for explicit confirmation if the user prefers gated edits.

## Optional: external fill-in

If the user enables web search, you may suggest or draft imputed facts for obvious gaps, clearly labeled as **needs verification** until confirmed.
