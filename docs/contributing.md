# Contributing

TAs and instructors can add or update papers directly.

## Adding a paper

1. Drop the PDF into the right category folder under `docs/papers/<category-slug>/`.
2. Add one line to the matching category page (`docs/<category-slug>.md`):
   ```text
   - {Paper Title}(papers/CATEGORY-SLUG/Paper Title.pdf)
   ```
   (using the actual Markdown link syntax `[title](path)`)
3. Commit and push directly to `main` (collaborators), or open a pull request.

   The "N papers" count on each category page is computed automatically from
   the PDFs in its `docs/papers/<slug>/` folder — no need to update it by hand.

Category slugs:

| Category | Folder / page slug |
|---|---|
| ML Classics / Optimization for ML | `ml-classics-optimization` |
| Bayesian ML | `bayesian-ml` |
| Unsupervised Learning / Generative Model | `unsupervised-generative` |
| Sequential Data Modeling / State Space Model | `sequential-ssm` |
| DL Classics | `dl-classics` |
| Information Theory / Complexity and Generalization | `info-theory-generalization` |

## Adding a new category

1. Create `docs/papers/<new-slug>/` and add PDFs there.
2. Create `docs/<new-slug>.md` listing them (copy the format of an existing category page).
3. Add the page to the `nav` section of `mkdocs.yml`.

## Previewing locally

```bash
pip install -r requirements.txt
mkdocs serve
```

Then open http://127.0.0.1:8000.
