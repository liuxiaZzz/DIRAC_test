# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'DIRAC'
copyright = '2024, XU CHANG'
author = 'XU CHANG'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'nbsphinx',
    'sphinx_gallery.gen_gallery',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

sphinx_gallery_conf = {
    'examples_dirs': 'notebooks',  
    'gallery_dirs': 'auto_gallery', 
}

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': True,
    'github_url': 'https://github.com/boxiangliulab/DIRAC',  
}

# -- Options for EPUB output
epub_show_urls = 'footnote'
