# from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from rest_framework import mixins
from rest_framework import filters
from rest_framework import viewsets

from django_filters.rest_framework import DjangoFilterBackend
from .models import Chart, ChartCategory, Banner, HotSearch

from .serializers import ChartSerializer, CategorySerializer, BannerSerializer, HotWordsSerializer
from rest_framework_extensions.cache.mixins import CacheResponseMixin

# Create your views here.


class ChartPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 100




class ChartListViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
        图表列表数据,该注释直接会在docs文档中生成相关说明
    """
    queryset = Chart.objects.all().order_by('id')
    serializer_class = ChartSerializer
    pagination_class = ChartPagination

    # django不会提醒补齐filter_backends,要记住
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)

    search_fields = ('name', 'brief', 'desc',)
    ordering_fields = ('add_time', )


class GategoryViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
        图表分类列表数据
    retrieve:
        获取图表分类详情
    """
    queryset = ChartCategory.objects.all()
    serializer_class = CategorySerializer


class HotSearchsViewset(CacheResponseMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    获取热搜词列表
    """
    queryset = HotSearch.objects.all().order_by("-index")
    serializer_class = HotWordsSerializer


class BannerViewset(CacheResponseMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    list:
        获取轮播图
    """
    queryset = Banner.objects.all().order_by('index')
    serializer_class = BannerSerializer


