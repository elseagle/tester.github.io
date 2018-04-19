#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Oluwasogo Ogundowole'
SITENAME = 'Data Age'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Africa/Lagos'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Medium', 'http://medium.com/@oluwasogooluwafemiogundowole'),
	 ('Github', 'http://github.com/elseagle'),
         ('Python.org', 'http://python.org/'))

# Social widget
SOCIAL = (('Twitter', 'http://twitter.com/elseagle'),
          ('LinkedIn', 'http://linkedin.com/elseagle'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')

PLUGIN_PATH = './plugins'
PLUGINS = ['ipynb.markup']
