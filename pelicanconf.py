#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Enrique Rendon Fuentes'
SITENAME = "iTrendOn's Site"
# SITEURL = 'https://enriquerendon.github.io'
# SITEURL = 'http://www.enriquerendon.com'

PATH = 'content'
STATIC_PATHS = ['images', 'docs']

TIMEZONE = 'Europe/Madrid'

DEFAULT_LANG = 'en'

# THEME = 'pelican-themes/clean-blog'
# THEME = 'pelican-themes/buruma'
THEME = 'pelican-themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'flatly'
PYGMENTS_STYLE = 'friendly'


JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
PLUGIN_PATHS = ['pelican-plugins']

PLUGINS = ['i18n_subsites', 'render_math']

I18N_TEMPLATES_LANG = 'en'



# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('freeCodeCamp', 'https://www.freecodecamp.org/'),
         ('SAP Developers', 'https://developers.sap.com/'),
         ('openSAP', 'https://open.sap.com/'),)

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/erendon/'),
          ('twitter', 'https://twitter.com/iTrendOn'),
          ('github', 'https://github.com/enriquerendon'),
          ('gitlab', 'https://gitlab.com/enrique.rendon'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
