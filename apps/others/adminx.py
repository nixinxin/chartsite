#!/usr/bin/env python
# encoding: utf-8

import xadmin
from xadmin import views
from .models import News, SiteInfo


class NewsAdmin(object):
    list_display = ['id', 'title', "resource", 'display', 'is_hot', 'add_time']
    list_edited = ['title', "resource", 'display', 'is_hot', 'add_time']


xadmin.site.register(News, NewsAdmin)


class SiteInfoAdmin(object):
    list_display = ['id', 'title', "content",  'add_time']
    list_edited = ['id', 'title', "content",  'add_time']


xadmin.site.register(SiteInfo, SiteInfoAdmin)

