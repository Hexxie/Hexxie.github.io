#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Anastasiia Rusakova'
SITENAME = 'Hexblog'
SITEURL = ''

THEME = 'pelican-sober'
PATH = 'content'

TIMEZONE = 'Europe/Kiev'

DEFAULT_LANG = 'Ru'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (
#        ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/Hexxie'),
          ('LinkedIn', 'https://www.linkedin.com/in/arusakova'),
          ('Facebook', 'https://www.facebook.com/RuNassss'),
          ('Instagram', 'https://www.instagram.com/nastasiia_rusakova'))

#static folders
STATIC_PATHS = ['images', 'css', 'fonts', 'js']

#add plugins
#PLUGIN_PATHS = ['plugins']
#PLUGINS = ['better_figures_and_images']

#plugin for responsive images
RESPONSIVE_IMAGES = True

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#About block in sidebar
PELICAN_SOBER_ABOUT = "My name is Anastasiia.<br>I'm a Software Developer in Automotive industry.<br>My interests are: <ul><li>embedded development for ARM <li>C++ <li>Qt framework</ul>"
PELICAN_SOBER_STICKY_SIDEBAR = True