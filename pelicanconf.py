#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Tom Gurion'
SITENAME = 'Music / Tech / Interaction'
SITEURL = ''

PATH = 'content'
THEME = 'medius'

TIMEZONE = 'Asia/Jerusalem'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Pelican', 'http://getpelican.com/'),
    ('Python.org', 'http://python.org/'),
)

DEFAULT_PAGINATION = 9

PLUGINS = ['pelican_youtube', 'readtime']

MEDIUS_CATEGORIES = {
    'Projects': {
        'description': "it's showtime!",
        'thumbnail': '/images/thumb_projects.jpg',
    },
    'Thoughts': {
        'description': 'ideas and experimentations',
        'thumbnail': '/images/thumb_thoughts.png',
    },
    'Other': {
        'description': 'evrything else',
        'thumbnail': '/images/thumb_other.jpg',
    },
}

MEDIUS_AUTHORS = {
    'Tom Gurion': {
        'description': 'Musician, interactive music systems researcher, and a pythonista.',
        'cover': 'http://www.tomgurion.me/images/header.jpg',
        'image': '/images/TabaShips.jpg',
        'links': (('home', 'http://www.tomgurion.me/'),
                  ('github', 'https://github.com/Nagasaki45'),
                  ('twitter', 'https://twitter.com/tom_gurion'))
    }
}

MEDIUS_WIDGETS = ['authors', 'categories', 'tags']

DISPLAY_CATEGORIES_ON_MENU = False
