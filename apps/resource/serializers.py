#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = "xin nix"

from rest_framework import serializers
from .models import *


class Resourceserializer(serializers.ModelSerializer):
    """
    数据资源列表
    """
    class Meta:
        model = ResourceList
        fields = "__all__"


class GwyjzwzzzyDbserializer(serializers.ModelSerializer):
    """
    国外引进作物种质资源数据库
    """
    class Meta:
        model = GwyjzwzzzyDb
        fields = "__all__"


class NcpjgDbserializer(serializers.ModelSerializer):
    """
    农产品价格行情数据库
    """
    class Meta:
        model = NcpjgDb
        fields = "__all__"


class NcpjgHqzdcodeserializer(serializers.ModelSerializer):
    """
    农产品价格行情字段编码
    """
    class Meta:
        model = NcpjgDb
        fields = "__all__"


class AgriIndexserializer(serializers.ModelSerializer):
    """
    农业统计指标
    """
    class Meta:
        model = AgriIndex
        fields = "__all__"


class MytxDbserializer(serializers.ModelSerializer):
    """
    农作物名优特新品种数据库
    """
    class Meta:
        model = MytxDb
        fields = "__all__"


class ZgnytdkcDbserializer(serializers.ModelSerializer):
    """
    中国农业天敌昆虫数据库
    """
    class Meta:
        model = ZgnytdkcDb
        fields = "__all__"


class ZgnyyhswDbTpserializer(serializers.ModelSerializer):
    """
    中国农业有害生物图片数据库
    """
    class Meta:
        model = ZgnyyhswDbTp
        fields = "__all__"


class ZgnttdzzDbserializer(serializers.ModelSerializer):
    """
    中国农田天敌蜘蛛数据库
    """
    class Meta:
        model = ZgnttdzzDb
        fields = "__all__"


class ZgnthsDbserializer(serializers.ModelSerializer):
    """
    中国农田害鼠数据库
    """
    class Meta:
        model = ZgnthsDb
        fields = "__all__"


class ZgyclschcDbserializer(serializers.ModelSerializer):
    """
    中国叶菜类蔬菜害虫数据库
    """
    class Meta:
        model = ZgyclschcDb
        fields = "__all__"


class ZgwlrqwswDbserializer(serializers.ModelSerializer):
    """
    中国外来入侵微生物数据库
    """
    class Meta:
        model = ZgwlrqwswDb
        fields = "__all__"


class ZgwlrqkcDbserializer(serializers.ModelSerializer):
    """
    中国外来入侵昆虫数据库
    """
    class Meta:
        model = ZgwlrqkcDb
        fields = "__all__"


class ZgwlrqzwDbserializer(serializers.ModelSerializer):
    """
    中国外来入侵植物数据库
    """
    class Meta:
        model = ZgwlrqzwDb
        fields = "__all__"


class ZghdzcDbserializer(serializers.ModelSerializer):
    """
    中国旱地杂草数据库
    """
    class Meta:
        model = ZghdzcDb
        fields = "__all__"


class ZghlzwhcDbserializer(serializers.ModelSerializer):
    """
    中国旱粮作物害虫数据库
    """
    class Meta:
        model = ZghlzwhcDb
        fields = "__all__"


class ZggslschcDbserializer(serializers.ModelSerializer):
    """
    中国果菜类蔬菜害虫数据库
    """
    class Meta:
        model = ZggslschcDb
        fields = "__all__"


class ZggjhcDbserializer(serializers.ModelSerializer):
    """
    中国柑桔害虫数据库
    """
    class Meta:
        model = ZggjhcDb
        fields = "__all__"


class ZgmhhcDbserializer(serializers.ModelSerializer):
    """
    中国棉花害虫数据库
    """
    class Meta:
        model = ZgmhhcDb
        fields = "__all__"


class ZgstzcDbserializer(serializers.ModelSerializer):
    """
    中国水田杂草数据库
    """
    class Meta:
        model = ZgstzcDb
        fields = "__all__"


class ZgsdhcDbserializer(serializers.ModelSerializer):
    """
    中国水稻害虫数据库
    """
    class Meta:
        model = ZgsdhcDb
        fields = "__all__"


class ZgtsNcpserializer(serializers.ModelSerializer):
    """
    中国特色农产品
    """
    class Meta:
        model = ZgtsNcp
        fields = "__all__"


class ZglszwbdbhDbserializer(serializers.ModelSerializer):
    """
    中国粮食作物病毒病害数据库
    """
    class Meta:
        model = ZglszwbdbhDb
        fields = "__all__"


class ZglszwzjbhDbserializer(serializers.ModelSerializer):
    """
    中国粮食作物真菌病害数据库
    """
    class Meta:
        model = ZglszwzjbhDb
        fields = "__all__"


class ZglszwxjbhDbserializer(serializers.ModelSerializer):
    """
    中国粮食作物细菌病害数据库
    """
    class Meta:
        model = ZglszwxjbhDb
        fields = "__all__"


class ZgjjzwbdbhDbserializer(serializers.ModelSerializer):
    """
    中国经济作物病毒病害数据库
    """
    class Meta:
        model = ZgjjzwbdbhDb
        fields = "__all__"


class ZgjjzwzjbhDbserializer(serializers.ModelSerializer):
    """
    中国经济作物真菌病害数据库
    """
    class Meta:
        model = ZgjjzwzjbhDb
        fields = "__all__"


class ZgjjzwxjbhDbserializer(serializers.ModelSerializer):
    """
    中国经济作物细菌病害数据库
    """
    class Meta:
        model = ZgjjzwxjbhDb
        fields = "__all__"


class ZgpgtlhcDbserializer(serializers.ModelSerializer):
    """
    中国苹果桃梨害虫数据库
    """
    class Meta:
        model = ZgpgtlhcDb
        fields = "__all__"


class ZgxzqhDbserializer(serializers.ModelSerializer):
    """
    中国行政区划数据库
    """
    class Meta:
        model = ZgxzqhDb
        fields = "__all__"


class ZgzynywhYcserializer(serializers.ModelSerializer):
    """
    中国重要农业文化遗产
    """
    class Meta:
        model = ZgzynywhYc
        fields = "__all__"


class ZgzynywhycTpserializer(serializers.ModelSerializer):
    """
    中国重要农业文化遗产_图片
    """
    class Meta:
        model = ZgzynywhycTp
        fields = "__all__"


class ZwwzfbDbserializer(serializers.ModelSerializer):
    """
    作物物种分布数据库
    """
    class Meta:
        model = ZwwzfbDb
        fields = "__all__"


class XmzzzzhxzzDbserializer(serializers.ModelSerializer):
    """
    小麦种质资源核心种质数据库
    """
    class Meta:
        model = XmzzzzhxzzDb
        fields = "__all__"


class XmxpDbserializer(serializers.ModelSerializer):
    """
    小麦系谱数据库
    """
    class Meta:
        model = XmxpDb
        fields = "__all__"


class XmxcpzjqxpDbserializer(serializers.ModelSerializer):
    """
    小麦育成品种及其系谱数据库
    """
    class Meta:
        model = XmxcpzjqxpDb
        fields = "__all__"


class SdzzzzhxzzDbserializer(serializers.ModelSerializer):
    """
    水稻种质资源核心种质数据库
    """
    class Meta:
        model = SdzzzzhxzzDb
        fields = "__all__"


class SdycpzjqpxDbserializer(serializers.ModelSerializer):
    """
    水稻育成品种及其系谱数据库
    """
    class Meta:
        model = SdycpzjqpxDb
        fields = "__all__"


class YmxpzbhDbserializer(serializers.ModelSerializer):
    """
    玉米新品种保护数据库
    """
    class Meta:
        model = YmxpzbhDb
        fields = "__all__"


class YmzzzzhxzzDbserializer(serializers.ModelSerializer):
    """
    玉米种质资源核心种质数据库
    """
    class Meta:
        model = YmzzzzhxzzDb
        fields = "__all__"


class Xdnysfqserializer(serializers.ModelSerializer):
    """
    现代农业示范区
    """
    class Meta:
        model = Xdnysfq
        fields = "__all__"


class ZwyyzyzzDbserializer(serializers.ModelSerializer):
    """
    作物优异资源种质数据库
    """
    class Meta:
        model = ZwyyzyzzDb
        fields = "__all__"


class Youdamaiserializer(serializers.ModelSerializer):
    """
    优异资源综合评价数据库_大麦
    """
    class Meta:
        model = Youdamai
        fields = "__all__"


class YouYuMiserializer(serializers.ModelSerializer):
    """
    优异资源综合评价数据库_玉米
    """
    class Meta:
        model = YouYuMi
        fields = "__all__"


class ZwyczytxpjjdDbserializer(serializers.ModelSerializer):
    """
    作物遗传资源特性评价鉴定数据库_**
    """
    title = serializers.CharField(max_length=20, min_length=1, allow_blank=False, required=True)

    def validate_title(self, title):
        exists = ZwyczytxpjjdDbList.objects.filter(title=title)
        if not exists:
            return serializers.ValidationError("查询内容不存在")
        return title

    class Meta:
        model = ZwyczytxpjjdDbList
        fields = ("title", )


class GjnykyhzxmDbserializer(serializers.ModelSerializer):
    """
    国际农业科研项目数据库
    """
    class Meta:
        model = GjnykyhzxmDb
        fields = "__all__"


class GnnykyhzxmDbserializer(serializers.ModelSerializer):
    """
    国内农业科技项目数据库
    """
    class Meta:
        model = GnnykyhzxmDb
        fields = "__all__"


class NyhjkjcgDbserializer(serializers.ModelSerializer):
    """
    农业获奖科技成果数据库
    """
    class Meta:
        model = NyhjkjcgDb
        fields = "__all__"


class NykjrcDbserializer(serializers.ModelSerializer):
    """
    农业科技人才数据库
    """
    class Meta:
        model = NykjrcDb
        fields = "__all__"


class NykjjgDbserializer(serializers.ModelSerializer):
    """
    农业科技机构数据库
    """
    class Meta:
        model = NykjjgDb
        fields = "__all__"


class ZwkjwxDbserializer(serializers.ModelSerializer):
    """
    中文农业科技文摘数据库
    """
    class Meta:
        model = ZwkjwxDb
        fields = "__all__"


class YjnyDbserializer(serializers.ModelSerializer):
    """
    有机农业数据库
    """
    class Meta:
        model = YjnyDb
        fields = "__all__"


class NygjDbserializer(serializers.ModelSerializer):
    """
    有机农业数据库
    """
    class Meta:
        model = NygjDb
        fields = "__all__"


class NybzhczgfDbserializer(serializers.ModelSerializer):
    """
    农业标准和操作规范数据库
    """
    class Meta:
        model = NybzhczgfDb
        fields = "__all__"