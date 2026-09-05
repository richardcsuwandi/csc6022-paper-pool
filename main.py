import os

DOCS_DIR = os.path.join(os.path.dirname(__file__), "docs")


def define_env(env):
    @env.macro
    def paper_count(category_slug):
        """Count PDFs in docs/papers/<category_slug>/, so category pages
        never need a hardcoded paper count."""
        folder = os.path.join(DOCS_DIR, "papers", category_slug)
        if not os.path.isdir(folder):
            return 0
        return sum(1 for f in os.listdir(folder) if f.lower().endswith(".pdf"))
