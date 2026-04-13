# Q&A over the wiki (read wiki, write answers as files)

You answer questions using the Markdown wiki under `wiki/` as the primary knowledge base. Treat `raw/` as the archive of primary sources when a wiki article is thin or you need exact wording, figures, or citations.

## How to work

1. **Orient**  
   Start from hub or index pages in `wiki/`, then open the smallest set of articles that plausibly contain the answer.

2. **Research inside the repo**  
   Follow links, search filenames, and pull from `raw/` when the wiki does not yet encode a detail. If the wiki is large, avoid loading everything: narrow progressively.

3. **Answer format**  
   Default to writing an **artifact under `outputs/`** rather than only streaming chat text. Use a descriptive filename and date in the path or front matter when useful.

   Supported output types (pick what fits the question):

   - **Markdown report** — analysis, comparisons, literature-style notes.  
   - **Marp deck** — when the user wants slides or a talk outline (Marp-compatible Markdown).  
   - **Plots** — when a chart clarifies the answer (e.g. save PNG/SVG under `outputs/` and reference it from the Markdown).

4. **Close the loop**  
   When an answer improves or corrects the wiki in a durable way, add or update wiki pages so future queries are cheaper. Optionally link from the wiki to the output file under `outputs/`.

## Honesty

- If evidence is missing from both `wiki/` and `raw/`, say so and suggest what to ingest next—or use web search only if the user allows tools and you label external claims clearly.
