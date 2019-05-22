# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

from datetime import datetime

from recommonmark.parser import CommonMarkParser

import os

extensions = []
templates_path = ['/home/docs/checkouts/readthedocs.org/readthedocs/templates/sphinx', 'templates', '_templates', '.templates']
source_suffix = ['.rst', '.md']
source_parsers = {
            '.md': CommonMarkParser,
        }
master_doc = 'index'
project = u'gofast-docs'
copyright = str(datetime.now().year)
version = 'latest'
release = 'latest'
exclude_patterns = ['_build']
pygments_style = 'sphinx'
htmlhelp_basename = 'gofast-docs'
html_theme = 'sphinx_rtd_theme'
file_insertion_enabled = False
latex_documents = [
  ('index', 'gofast-docs.tex', u'gofast-docs Documentation',
   u'', 'manual'),
]

language = 'fr'

locale_dirs = [
    'locale/',
]
gettext_compact = False
gettext_uuid = True


#os.system('sphinx-build -b html -D language=en . _build/html/en')

#BASEDIR = os.path.dirname(os.path.abspath(__file__))

#def build_finished(app, exception):
#    os.system('sphinx-build -b html -D language=en . _build/html/en')
#    print('do something here...')

#def setup(app):
 #   app.connect('build-finished', build_finished)
	
#make gettext
#sphinx-intl update -p locale en

