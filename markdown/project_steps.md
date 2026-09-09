# Optimize Markdown Folder - Project Steps

## Goal
Recursively scan a given folder full of markdown files, extract tags, and re-organize the files into a smarter, easier-to-navigate folder structure.

## Supporting Projects
- **`C:\repos\markdown_tag_update`** - scan markdown files, extract `#tags`, maintain the central tag registry (`docs/tools.json`), and apply tags to files.
- **Local `functions/` folder** - reusable utilities (`ensure_file`, `ensure_folder`, `move_file_to_assets`).

## Step-by-Step Plan

### Step 1 - Scan for Markdown Files
Recursively walk the target folder and collect every `*.md` file.
- Skip system folders (`.git`, `.venv`, `__pycache__`, `.pytest_cache`, `.gitignore`).
- Record each file's relative path from the root.

### Step 2 - Extract Tags
Use the `markdown_tag_update` project:
1. Run `scripts/extract_tags.py --markdown-folder-path <target>` to read all `#tag` patterns and count occurrences.
2. Review the generated `docs/tags.csv` (human-in-the-loop) and approve/adjust suggested sections.

### Step 3 - Update the Tag Registry
Run `scripts/update_tags_json.py` to merge approved tags into `docs/tools.json`.
Sections drive the target folder structure (e.g. `coding_languages`, `applications`, `libraries_or_modules`, `miscellaneous`).

### Step 4 - Apply Tags (optional)
Run `scripts/apply_tags.py` so every file carries its correct `#tags` under a `## Tags` heading. This keeps tags consistent before files are moved.

### Step 5 - Define the Target Folder Structure
Derive folder names from the tag sections in `tools.json`, e.g.:

```
<root>/
├── coding_languages/
├── applications/
├── libraries_or_modules/
├── miscellaneous/
└── uncategorized/        # files without any matching tags
```

Decide rules up front:
- Which section a file belongs to when it has multiple tags (priority order).
- Whether to move files compared to simply generating a report first (dry-run).

### Step 6 - Create the Folder Structure
For each target folder, use `functions/ensure_folder.py` (`ensure_folder`) to create the directories if they do not already exist.

### Step 7 - Assign Files to Folders
For each markdown file:
1. Match its tags against the sections in `tools.json`.
2. Choose the primary section (priority order).
3. Move the file into the matching folder using `ensure_file`/file move logic.
4. Collision handling: if a file with the same name already exists, suffix with a counter (e.g. `name_1.md`, `name_2.md`).

### Step 8 - Move Image Assets
For each markdown file, find image files referenced/located near the article and move them into an `assets/` subfolder beside the article using `functions/move_file_to_assets.py`:
- Ensure `assets/` exists first (via `ensure_folder`).
- Move only actual image files (extension check).
- Update image paths in the markdown content if needed.

### Step 9 - Report and Log
Write a log/report of everything performed:
- Files scanned, moved, renamed, skipped.
- Tags extracted and sections assigned.
- Any files that could not be categorized.

### Step 10 - Verify
Run a final pass:
- Confirm no `*.md` files remain in the root/leftover folders.
- Confirm every file's relative link/image paths still resolve.
- Re-run the tag extractor to confirm tags still match.

## Open Questions / Decisions
- Should we always physically move files, or support a dry-run/report-only mode first?
- Should the folder names follow section names from `tools.json`, or be configurable maps?
- Should the article folder include its `assets/`, or should assets be centralized?
- Are there folders that should not be moved, have articles/assets removed/copied/changed?

## Project Structure Reference (current)
```
optimize_markdown_folder/
├── functions/
│   ├── __init__.py
│   ├── ensure_file.py
│   ├── ensure_folder.py
│   └── move_file_to_assets.py
├── library/
│   └── __init__.py
├── markdown/
│   └── project_steps.md   <- this file
├── scripts/
├── src/optimize_markdown_folder/
│   ├── __init__.py
│   └── __main__.py
└── tests/
```