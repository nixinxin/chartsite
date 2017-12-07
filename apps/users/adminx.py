#!/usr/bin/env python
# encoding: utf-8

import xadmin
from xadmin import views
from .models import PhoneCode, EmailCode


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "农业统计数据可视化平台"
    site_footer = "chartsite"
    # menu_style = "accordion"


class PhoneCodeAdmin(object):
    list_display = ['code', 'mobile', "add_time"]


class EmailCodeAdmin(object):
    list_display = ['code', 'email', "add_time"]


xadmin.site.register(PhoneCode, PhoneCodeAdmin)
xadmin.site.register(EmailCode, EmailCodeAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
