#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "Owen Lamont"
SITENAME = "Owen Lamont"
SITEURL = ""

PATH = "content"

TIMEZONE = "Australia/Perth"

DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# Blogroll
#LINKS = (("Pelican", "http://getpelican.com/"), ("Python.org", "http://python.org/"))

# Social widget
SOCIAL = (
    ("GitHub", "https://github.com/owenlamont"),
    ("LinkedIn", "https://www.linkedin.com/in/owen-lamont"),
    ("Twitter", "https://twitter.com/owenrlamont"),
    ("YouTube", "https://www.youtube.com/channel/UCYoZjpdGVH2X1MBgRD71lHw")
)

SOCIAL_WIDGET_NAME = "Follow"

STATIC_PATHS = [
    "images",
    'extra',
]
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
}

DEFAULT_PAGINATION = 10

THEME = "notmyidea"
#THEME = "Flex"
#THEME = "pelican-blueidea"

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

