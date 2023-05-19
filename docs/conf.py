import os
import sys

sys.path.insert(0, os.path.abspath("../.."))

project = "Your Module Name"
author = "Your Name"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
html_theme = "alabaster"
html_static_path = ["_static"]


def setup(app):
    app.add_css_file("custom.css")
