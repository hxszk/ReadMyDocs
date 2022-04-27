# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'ReadMyDocs'
copyright = '2021, Alex'
author = 'Alex Hao'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# The default language to highlight source code in. The default is 'python'.
# The value should be a valid Pygments lexer name, see Showing code examples for more details.
highlight_language = 'c'

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = ['.rst', '.md']


# The master toctree document.
master_doc = 'index'

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
