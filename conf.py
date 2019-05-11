# -*- coding: utf-8 -*-
import os
import sys

sys.path.insert(0, os.path.abspath('cv/'))

project = u'oalfonso'
copyright = u'2019, Oriol Alfonso'
author = u'Oriol Alfonso'
version = u'Python Developer'
release = u'Python Developer'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
]

source_suffix = '.rst'
master_doc = 'index'
language = None
exclude_patterns = [u'_build', 'Thumbs.db', '.DS_Store']
pygments_style = None

html_theme = 'sphinx_rtd_theme'
html_logo = '_static/careto.jpg'
html_favicon = '_static/icon.png'
html_static_path = ['_static']
templates_path = ['_templates']

html_theme_options = {
    'navigation_depth': -1,
    'collapse_navigation': False,
}

autodoc_default_options = {
    'member-order': 'bysource',
}

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------
# Output file base name for HTML help builder.
htmlhelp_basename = 'oalfonsodoc'


# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'oalfonso.tex', u'Oriol Alfonso',
     u'Oriol Alfonso', 'manual'),
]

# -- Options for manual page output ------------------------------------------
# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'oalfonso', u'Oriol Alfonso',
     [author], 1)
]

# -- Options for Texinfo output ----------------------------------------------
# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'oalfonso', u'Oriol Alfonso',
     author, 'oalfonso', 'This is a bit about me',
     'Miscellaneous'),
]

epub_title = project
epub_exclude_files = ['search.html']

intersphinx_mapping = {'https://docs.python.org/': None}
