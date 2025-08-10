# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------
project = 'My MLOps Journey'
author = 'Sujeet Kumar'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
extensions = ["myst_parser"]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

templates_path = ["_templates"]
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
