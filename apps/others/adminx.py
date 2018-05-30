import xadmin
from .models import News, SiteInfo, RelatedSite


class NewsAdmin(object):
    list_display = ['id', 'title', "resource", 'display', 'is_hot', 'add_time']
    list_editable = ['title', "resource", 'display', 'is_hot', 'add_time']
    style_fields = {"content": "ueditor"}


xadmin.site.register(News, NewsAdmin)


class SiteInfoAdmin(object):
    list_display = ['id', 'title', "content",  'add_time']
    list_editable = ['id', 'title', "content",  'add_time']


xadmin.site.register(SiteInfo, SiteInfoAdmin)


class RelatedSiteAdmin(object):
    list_display = ['index', 'name', "link", 'display',  'add_time']
    list_editable = ['index', 'name', "link",  'display', 'add_time']


xadmin.site.register(RelatedSite, RelatedSiteAdmin)

