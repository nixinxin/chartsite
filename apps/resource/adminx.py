#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: liyao
@license: Apache Licence
@contact: yli@posbao.net
@site: http://www.piowind.com/
@software: PyCharm
@file: adminx.py
@time: 2017/7/4 17:04
"""
import xadmin
from .models import *


# 国外引进作物种质资源数据库
class GwyjzwzzzyDbAdmin(object):

    list_display = ['id', "name", "copes_category", 'copes_type', "category_name", "source", "distribution_unit", 'import_time']
    search_fields = ['id', "name", "copes_category", 'copes_type', "category_name", "distribution_unit", ]
    list_filter = ['id', "name", "copes_category", 'copes_type', "category_name", "distribution_unit", ]
    ordering = ['id']


xadmin.site.register(GwyjzwzzzyDb, GwyjzwzzzyDbAdmin)


# 行政区划清单
class XzqhListAdmin(object):
    list_display = ["id", 'province', "city", 'district', "provincecode", "citycode", "districtcode", 'alias']
    search_fields = ["id", 'province', "city", 'district', "provincecode", "citycode", "districtcode", 'alias']
    list_filter = ["id", "provincecode", "citycode", "districtcode", ]
    ordering = ['id']


xadmin.site.register(XzqhList, XzqhListAdmin)


# 农产品价格行情数据库
class NcpjgDbAdmin(object):
    list_display = ["category", "product", "price", "market", "datetime"]
    search_fields = ["category", "product", "price", "market", "datetime"]
    list_filter = ["category", "price", "market", "datetime"]
    ordering = ['id']


xadmin.site.register(NcpjgDb, NcpjgDbAdmin)


# 农产品价格行情字段编码
class NcpjgHqzdcodeAdmin(object):
    list_display = ["code", "product", "category", ]
    search_fields = ["code", "product", "category", ]
    list_filter = ["code", "product", "category", ]


xadmin.site.register(NcpjgHqzdcode, NcpjgHqzdcodeAdmin)


# 农业统计指标
class AgriIndexAdmin(object):
    list_display = ["index", "values", "location", "year"]
    search_fields = ["index", "values", "location", "year"]
    list_filter = ["index", "location", "year"]


xadmin.site.register(AgriIndex, AgriIndexAdmin)


# 农作物名、优、特新品种数据库
class MytxDbAdmin(object):
    list_display = ["name", "category", "brands", "raiser", 'brands_category', "get_day"]
    search_fields = ["name", "category", "brands", "desc", "feature", "raiser", "location_T", 'brands_category', "examine", "get_day"]
    list_filter = ["name", "category", 'brands_category',]
    ordering = ['id']


xadmin.site.register(MytxDb, MytxDbAdmin)


# 中国农业天敌昆虫数据库
class ZgnytdkcDbAdmin(object):
    list_display = ["id", "zhname", 'function_class', "gang", 'mu', 'ke']
    search_fields = ["id", "zhname", 'function_class', "gang", 'mu', 'ke', 'jizhu_insect', 'feature']
    list_filter = ["zhname", 'function_class', 'mu']
    ordering = ['id']


xadmin.site.register(ZgnytdkcDb, ZgnytdkcDbAdmin)


# 中国农业有害生物数据库_图片
class ZgnyyhswDbTpAdmin(object):
    list_display = ["name", 'species', 'link']
    search_fields = ["name", 'species', 'link']
    ordering = ['id']


xadmin.site.register(ZgnyyhswDbTp, ZgnyyhswDbTpAdmin)


# 中国农田天敌蜘蛛数据库
class ZgnttdzzDbAdmin(object):
    list_display = ["id", 'zhname', 'function_class', 'gang', 'mu', 'ke']
    search_fields = ["id", 'zhname', 'function_class', 'gang', 'mu', 'ke', 'jizhu_insect', 'jizhu_hazard', 'feature']
    list_filter = ['function_class', 'mu', 'ke']
    ordering = ['id']


xadmin.site.register(ZgnttdzzDb, ZgnttdzzDbAdmin)


# 中国农田害鼠数据库
class ZgnthsDbAdmin(object):
    list_display = ["id", "zhname", 'alias', 'enemy', 'gang', 'mu', 'ke']
    search_fields = ["id", "zhname", 'alias', 'enemy', 'gang', 'mu', 'ke', 'major_hazard', 'hazard_feature', 'feature', 'xuename']
    list_filter = ['mu', 'ke']
    ordering = ['id']


xadmin.site.register(ZgnthsDb, ZgnthsDbAdmin)


# 中国叶菜类蔬菜害虫数据库
class ZgyclschcDbAdmin(object):
    list_display = ["id", "zhname", 'gang', 'mu', 'ke']
    search_fields = ["id", "zhname", 'enemy', 'mu', 'ke', 'major_hazard', 'hazard_feature', 'feature', 'xuename']
    list_filter = ['mu']
    ordering = ['id']


xadmin.site.register(ZgyclschcDb, ZgyclschcDbAdmin)


# 中国外来入侵微生物数据库
class ZgwlrqwswDbAdmin(object):
    list_display = ["id", "zhname", 'source', 'mu', 'ke', 'shu']
    search_fields = ["id", "zhname", 'source', 'ke', 'mu', 'ke', 'major_hazard', 'hazard_feature', 'xuename']
    list_filter = ['mu', ]
    ordering = ['id']


xadmin.site.register(ZgwlrqwswDb, ZgwlrqwswDbAdmin)


# 中国外来入侵昆虫数据库
class ZgwlrqkcDbAdmin(object):
    list_display = ["id", "zhname", 'source', 'mu', 'ke', 'shu']
    search_fields = ["id", "zhname", 'source', 'ke', 'mu', 'ke', 'major_hazard', 'hazard_feature', 'xuename']
    list_filter = ['mu', ]
    ordering = ['id']


xadmin.site.register(ZgwlrqkcDb, ZgwlrqkcDbAdmin)


# 中国外来入侵植物数据库
class ZgwlrqzwDbAdmin(object):
    list_display = ["id", "zhname", 'source', 'men', 'mu', 'ke', 'shu']
    search_fields = ["id", "zhname", 'source', 'men', 'ke', 'mu', 'ke', 'hazard_feature', 'xuename']
    ordering = ['id']


xadmin.site.register(ZgwlrqzwDb, ZgwlrqzwDbAdmin)


# 中国旱地杂草数据库
class ZghdzcDbAdmin(object):
    list_display = ["id", "zhname",  'mu', 'ke', 'shu']
    search_fields = ["id", "zhname", 'ke', 'mu', 'ke', 'xuename']
    ordering = ['id']


xadmin.site.register(ZghdzcDb, ZghdzcDbAdmin)


# 中国旱粮作物害虫数据库
class ZghlzwhcDbAdmin(object):
    list_display = ["id", "zhname", 'mu', 'ke']
    search_fields = ["id", "zhname", 'ke', 'mu', 'ke', 'xuename']
    ordering = ['id']


xadmin.site.register(ZghlzwhcDb, ZghlzwhcDbAdmin)


# 中国果菜类蔬菜害虫数据库
class ZggslschcDbAdmin(object):
    list_display = ["id", "zhname", "gang", 'mu', 'ke']
    search_fields = ["id", "zhname", "gang", 'ke', 'mu', 'ke', 'xuename']
    ordering = ['id']


xadmin.site.register(ZggslschcDb, ZggslschcDbAdmin)


# 中国柑桔害虫数据库
class ZggjhcDbAdmin(object):
    list_display = ["id", "zhname", "gang", 'mu', 'ke']
    search_fields = ["id", "zhname", "gang", 'ke', 'mu', 'ke', 'xuename']
    ordering = ['id']


xadmin.site.register(ZggjhcDb, ZggjhcDbAdmin)


# 中国棉花害虫数据库
class ZgmhhcDbAdmin(object):
    list_display = ["id", "zhname", "gang", 'mu', 'ke']
    search_fields = ["id", "zhname", "gang", 'ke', 'mu', 'ke', 'xuename']
    ordering = ['id']


xadmin.site.register(ZgmhhcDb, ZgmhhcDbAdmin)


# 中国水田杂草数据库
class ZgstzcDbAdmin(object):
    list_display = ["id", "zhname", "gang", 'mu', 'ke']
    search_fields = ["id", "zhname", "gang", 'ke', 'mu', 'ke', 'xuename']
    ordering = ['id']


xadmin.site.register(ZgstzcDb, ZgstzcDbAdmin)


# 中国水稻害虫数据库
class ZgsdhcDbAdmin(object):
    list_display = ["id", "zhname", "gang", 'mu', 'ke']
    search_fields = ["id", "zhname", "gang", 'ke', 'mu', 'ke', 'xuename']
    ordering = ['id']


xadmin.site.register(ZgsdhcDb, ZgsdhcDbAdmin)


# 中国特色农产品
class ZgtsNcpAdmin(object):
    list_display = ['id', "title", "location", "feature", 'brands']
    search_fields = ['id', "title", "location", "feature", 'brands']
    list_filter = ["title", 'location', "feature", 'brands']
    ordering = ['id']


xadmin.site.register(ZgtsNcp, ZgtsNcpAdmin)


# 中国粮食作物病毒病害数据库
class ZglszwbdbhDbAdmin(object):
    list_display = ['id', "zhname", "byzhname", "major_hazard", 'disease_type']
    search_fields = ['id', "zhname", "byzhname", "byxuename", 'symptom', 'disease_type', "major_hazard", "hazard_buwei"]
    ordering = ['id']


xadmin.site.register(ZglszwbdbhDb, ZglszwbdbhDbAdmin)


# 中国粮食作物真菌病害数据库
class ZglszwzjbhDbAdmin(object):
    list_display = ['id', "zhname", "byzhname", "major_hazard", 'disease_type']
    search_fields = ['id', "zhname", "byzhname", "byxuename", 'disease_type', "major_hazard", "hazard_buwei"]
    ordering = ['id']


xadmin.site.register(ZglszwzjbhDb, ZglszwzjbhDbAdmin)


# 中国粮食作物细菌病害数据库
class ZglszwxjbhDbAdmin(object):
    list_display = ['id', "zhname", "byzhname", "major_hazard", 'disease_type']
    search_fields = ['id', "zhname", "byzhname", "byxuename", 'disease_type', "major_hazard", "hazard_buwei"]
    ordering = ['id']


xadmin.site.register(ZglszwxjbhDb, ZglszwxjbhDbAdmin)


# 中国经济作物病毒病害数据库
class ZgjjzwbdbhDbAdmin(object):
    list_display = ['id', "zhname", "byzhname", "major_hazard", 'disease_type']
    search_fields = ['id', "zhname", "byzhname", "byxuename", 'disease_type', "major_hazard", "hazard_buwei"]
    ordering = ['id']


xadmin.site.register(ZgjjzwbdbhDb, ZgjjzwbdbhDbAdmin)


# 中国经济作物真菌病害数据库
class ZgjjzwzjbhDbAdmin(object):
    list_display = ['id', "zhname", "byzhname", "major_hazard", 'disease_type']
    search_fields = ['id', "zhname", "byzhname", "byxuename", 'disease_type', "major_hazard", "hazard_buwei"]
    ordering = ['id']


xadmin.site.register(ZgjjzwzjbhDb, ZgjjzwzjbhDbAdmin)


# 中国经济作物细菌病害数据库
class ZgjjzwxjbhDbAdmin(object):
    list_display = ['id', "zhname", "byzhname", "major_hazard", 'disease_type']
    search_fields = ['id', "zhname", "byzhname", "byxuename", 'disease_type', "major_hazard", "hazard_buwei"]
    ordering = ['id']


xadmin.site.register(ZgjjzwxjbhDb, ZgjjzwxjbhDbAdmin)


# 中国苹果桃梨害虫数据库
class ZgpgtlhcDbAdmin(object):
    list_display = ['id', "zhname", "gang", 'mu', 'ke']
    search_fields = ['id', "zhname", "enemy", "gang", 'mu', 'ke']
    ordering = ['id']


xadmin.site.register(ZgpgtlhcDb, ZgpgtlhcDbAdmin)


# 中国行政区划数据库
class ZgxzqhDbAdmin(object):
    list_display = ['citycode', "adcode", "name", 'center', 'level']
    search_fields = ['citycode', "adcode", "name", 'center', 'level']
    list_filter = ['level']
    ordering = ['citycode']


xadmin.site.register(ZgxzqhDb, ZgxzqhDbAdmin)


# 中国重要农业文化遗产
class ZgzynywhYcAdmin(object):
    list_display = ['title', "pici", 'source', 'datetime']
    search_fields = ['title', "pici", "link", 'source', 'clicks', 'datetime', 'content']
    list_filter = ['pici', ]
    ordering = ['title']

    # class ImagesInline(object):
    #     model = ZgzynywhycTp
    #     # exclude = ["image_num", 'pici',]
    #     extra = 1
    #     style = 'tab'
    #
    # inlines = [ImagesInline]
    #


xadmin.site.register(ZgzynywhYc, ZgzynywhYcAdmin)


# 中国重要农业文化遗产_图片
class ZgzynywhycTpAdmin(object):
    list_display = ['title', "image_num", "pici", 'path']
    search_fields = ['title', "image_num", "pici", 'path']
    list_filter = ['pici', ]
    ordering = ['title']


xadmin.site.register(ZgzynywhycTp, ZgzynywhycTpAdmin)


# 作物物种分布数据库
class ZwwzfbDbAdmin(object):
    list_display = ['title', "category", 'path']
    search_fields = ['title', "category", 'path']
    ordering = ['title', ]


xadmin.site.register(ZwwzfbDb, ZwwzfbDbAdmin)


# 小麦种质资源核心种质数据库
class XmzzzzhxzzDbAdmin(object):
    list_display = ['id', "name", 'xipu', 'source', 'unit', 'province']
    search_fields = ['id', "name", 'xipu', 'source', 'unit', 'province']
    list_filter = ['province', ]
    ordering = ['id', ]


xadmin.site.register(XmzzzzhxzzDb, XmzzzzhxzzDbAdmin)


# 小麦育成品种及其系谱数据库
class XmxcpzjqxpDbAdmin(object):
    list_display = ['id', "name", 'translated_name', 'source', 'unit', "ke", 'shu']
    search_fields = ['id', "name", 'translated_name', 'source', 'unit', "ke", 'shu']
    ordering = ['id', ]


xadmin.site.register(XmxcpzjqxpDb, XmxcpzjqxpDbAdmin)


# 水稻种质资源核心种质数据库
class SdzzzzhxzzDbAdmin(object):
    list_display = ['total_id', "name", 'source', 'save_unit']
    search_fields = ['total_id', "name", 'source', 'save_unit']
    ordering = ['total_id', ]


xadmin.site.register(SdzzzzhxzzDb, SdzzzzhxzzDbAdmin)


# 水稻育成品种及其系谱数据库
class SdycpzjqpxDbAdmin(object):
    list_display = ['totalcode', "name", 'xuanyu_unit', 'xuename', 'province']
    search_fields = ['totalcode', "name", 'xuanyu_unit', 'xuename', 'province']
    list_filter = ['province', ]
    ordering = ['totalcode', ]


xadmin.site.register(SdycpzjqpxDb, SdycpzjqpxDbAdmin)


# 玉米新品种保护数据库
class YmxpzbhDbAdmin(object):
    list_display = ['id', "name", 'daibiao_breed', 'source']
    search_fields = ['id', "name", 'daibiao_breed', 'source']
    ordering = ['id', ]


xadmin.site.register(YmxpzbhDb, YmxpzbhDbAdmin)


# 玉米种质资源核心种质数据库
class YmzzzzhxzzDbAdmin(object):
    list_display = ['total_id', "name", 'qingbenyuan', 'unit', 'source', 'bozhongqi']
    search_fields = ['total_id', "name", 'unit', 'source', "qingbenyuan", 'bozhongqi']
    ordering = ['total_id', ]


xadmin.site.register(YmzzzzhxzzDb, YmzzzzhxzzDbAdmin)


# 现代农业示范区
class XdnysfqAdmin(object):
    list_display = ['title', "href"]
    search_fields = ['title', "href"]
    ordering = ['title', ]


xadmin.site.register(Xdnysfq, XdnysfqAdmin)


# 作物优异资源种质数据库
class ZwyyzyzzDbAdmin(object):
    list_display = ['id', 'name', "xiaolei", 'dalei', 'type', 'unit']
    search_fields = ['id', 'name', "xiaolei", 'dalei', 'type', 'unit']
    list_filter = ['dalei', 'type']
    ordering = ['id', ]


xadmin.site.register(ZwyyzyzzDb, ZwyyzyzzDbAdmin)

