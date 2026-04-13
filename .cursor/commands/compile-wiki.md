# Compile / maintain the wiki (from `raw/`)

You are maintaining a personal research wiki stored as Markdown under `wiki/`. Source material lives in `raw/` (articles, papers, repo notes, datasets, images, clips, etc.). The wiki is the **compiled layer**: you write and evolve it; the human rarely edits it by hand.

## Goals

1. **Cover everything in `raw/`**   Every substantive item in `raw/` should be represented in the wiki: at least a short summary, provenance (where it came from), and links to the raw path(s).

2. **Incremental compilation**  
   When new material appears under `raw/`, update the wiki in small, coherent edits rather than one-off dumps. Prefer append + refactor over duplicate notes.

3. **Structure**  
   - Use a clear folder layout under `wiki/` (topics, papers, projects—whatever fits the domain).  
   - Maintain **concept** notes: one core idea per note, with links out to sources and related concepts.  
   - Keep **backlinks** in mind: when you create or update a note, add links from related notes so the graph stays navigable.

4. **Indexes**  
   Maintain lightweight index files (e.g. hub pages or `wiki/_index.md`-style maps) so a reader (or you, in a later session) can see what exists and what is still only in `raw/`.

5. **Images**  
   If `raw/` contains images, reference them from wiki pages with relative paths so tools (e.g. Obsidian) can open them. Do not silently drop visual information that matters for understanding.

## Style

- Prefer tight, factual summaries; mark uncertainty explicitly.  
- Use standard Markdown; wiki-style `[[links]]` to other wiki pages where helpful.  
- Include dates or versions when the source material is time-sensitive.

## Constraints

- Do not delete or rewrite `raw/` content as part of wiki maintenance unless the user explicitly asks.  
- If something in `raw/` is unclear, create a stub article that states what is unknown and what would resolve it.
