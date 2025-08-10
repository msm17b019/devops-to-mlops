# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------
project = 'My MLOps Journey'
author = 'Your Name'
release = '0.1'

# -- General configuration ---------------------------------------------------
extensions = ["myst_parser"]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

templates_path = ["_templates"]
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = "alabaster"  # You can change to 'sphinx_rtd_theme' if you prefer
html_static_path = ["_static"]
