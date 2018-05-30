import xadmin
from .models import *


class UserFavAdmin(object):
    list_display = ['user', 'chart', "add_time"]
    search_fields = ['user', 'chart', "add_time"]


xadmin.site.register(UserFav, UserFavAdmin)


class FeedBackAdmin(object):
    list_display = ['user', 'message_type', "subject", 'add_time']
    search_fields = ['user', 'message_type', "subject", 'add_time']
    list_filter = ["message_type", ]


xadmin.site.register(FeedBack, FeedBackAdmin)


class DataShareAdmin(object):
    list_display = ['title', "user", 'type', 'add_time']
    search_fields = ['id', 'title', "title",  'add_time']


xadmin.site.register(DataShare, DataShareAdmin)