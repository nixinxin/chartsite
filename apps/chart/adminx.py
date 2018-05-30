import xadmin
from .models import *


class ChartCategoryAdmin(object):
    list_display = ['name', 'desc', "is_tab", "add_time"]
    list_editable = list_display


xadmin.site.register(ChartCategory, ChartCategoryAdmin)


class ChartAdmin(object):
    list_display = ['name', "surface", 'jsfile', "is_new", "is_hot", "add_time"]
    list_filter = ['is_hot', 'is_new']
    list_editable = list_display


xadmin.site.register(Chart, ChartAdmin)


class ChartImageAdmin(object):
    list_display = ['chart', 'image', "link", "add_time"]
    list_editable = list_display


xadmin.site.register(ChartImage, ChartImageAdmin)


class BannerAdmin(object):
    list_display = ['chart', 'image', "index", "add_time"]
    list_editable = list_display


xadmin.site.register(Banner, BannerAdmin)


class HotSearchAdmin(object):
    list_display = ['keywords', 'index', "add_time"]
    list_editable = list_display


xadmin.site.register(HotSearch, HotSearchAdmin)


