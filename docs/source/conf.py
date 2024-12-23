# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'TEST_DIRAC'
copyright = '2024, CHANG XU'
author = 'CHANG XU'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    # 'myst_parser',
    'sphinx.ext.viewcode',
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'nbsphinx',
    'nbsphinx_link',
]

nbsphinx_allow_errors = True

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

# -- Options for HTML output

templates_path = ['_templates']

html_theme = 'furo'

html_title = "DIRAC documentation"
html_logo = "../Figs/logo.png"

html_show_sphinx = False

html_theme_options = {
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': True,
    'github_url': 'https://github.com/boxiangliulab/DIRAC',  
}

# -- Options for EPUB output
epub_show_urls = 'footnote' 

# html_static_path = ["../Figs"]

nbsphinx_thumbnails = {
    "notebooks/run_DIRAC_DBit-seq": "../Figs/tutorial_figs/notebooks_run_DIRAC_DBit-seq_22_0.png",
    "notebooks/run_DIRAC_on_DLPFC": "../Figs/tutorial_figs/notebooks_run_DIRAC_on_DLPFC_9_1.png",
    "notebooks/run_DIRAC_mouse_spleen_bin100": "../Figs/tutorial_figs/notebooks_run_DIRAC_mouse_spleen_bin100_33_1.png",
    "notebooks/run_DIRAC_mouse_spleen_cellbin": "../Figs/tutorial_figs/notebooks_run_DIRAC_mouse_spleen_cellbin_26_2.png",
}
