#!/usr/bin/python
# -*- coding:utf-8 -*-
from django.db.models import Q

__author__ = "xin nix"
from rest_framework import serializers
from .models import Chart, ChartCategory, ChartImage, Banner, HotSearch


class CategorySerializer(serializers.ModelSerializer):
    """
    图表类别序列化
    """
    class Meta:
        model = ChartCategory
        fields = "__all__"


class ChartImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChartImage
        fields = "__all__"


class ChartSerializer(serializers.ModelSerializer):

    # 直接省略所有字段和方法
    class Meta:
        model = Chart
        fields = "__all__"


class HotWordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotSearch
        fields = "__all__"


class BannerSerializer(serializers.ModelSerializer):

    chart = ChartSerializer(many=True)

    class Meta:
        model = Banner
        fields = "__all__"


class IndexChartSerializer(serializers.ModelSerializer):

    images = ChartImageSerializer(many=True)  # 一个chart会有多个image

    class Meta:
        model = Chart
        fields = "__all__"


