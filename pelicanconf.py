#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Tom Gurion'
SITENAME = 'Tom Gurion'
SITESUBTITLE = 'Music / Tech / Interaction blog'
BIO = 'A blog about interactive music systems, social interaction, code, and everything in between'
SITEURL = ''

PATH = 'content'
THEME = 'hyde'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Sidebar links
SOCIAL = (
    ('home', 'http://tomgurion.me'),
    ('github', 'https://github.com/Nagasaki45'),
    ('twitter', 'https://twitter.com/tom_gurion'),
    ('envelope', 'mailto:nagasaki45@gmail.com'),
)

DEFAULT_PAGINATION = 10

PLUGINS = ['pelican_youtube']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PROFILE_IMAGE = 'me.jpg'

STATIC_PATHS = [
    'images',
    'extra/favicon.ico',
    'extra/CNAME',
]

EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/CNAME': {'path': 'CNAME'},
}
