#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'trvrm'
SITENAME = 'RenaissanceNow'
SITEURL = ''

PATH = 'content'

OUTPUT_PATH = 'docs/'

TIMEZONE = 'EST'

DEFAULT_LANG = 'en'

PYGMENTS_STYLE = 'tango'

THEME = "./pelican-bootstrap3"

BOOTSTRAP_THEME='yeti'
PLUGINS=[]
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/trvrm',),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

DISPLAY_ARTICLE_ON_INDEX=True

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}
