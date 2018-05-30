# from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views import View

from rest_framework.pagination import PageNumberPagination
from rest_framework import mixins
from rest_framework import filters
from rest_framework import viewsets
from rest_framework_extensions.cache.mixins import CacheResponseMixin
from pure_pagination import Paginator, PageNotAnInteger
from django_filters.rest_framework import DjangoFilterBackend

from .models import Chart, ChartCategory, Banner, HotSearch
from .serializers import ChartSerializer, CategorySerializer, BannerSerializer, HotWordsSerializer
from chartsite.settings import VISUAL_CONTENT_NUM

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
    ordering_fields = ('add_time',)


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


class VisualView(View):
    def get(self, request, content_num=VISUAL_CONTENT_NUM):
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        try:
            nums = request.GET.get('nums', 0)
        except PageNotAnInteger:
            nums = 0
        content_num += int(nums)
        chart = Chart.objects.all()
        chart_page = Paginator(chart, content_num, request=request)
        result = chart_page.page(page)
        return render_to_response("visual.html",
                                  context={
                                      'chart': result,
                                  }
                                  )


import math

from django.http import HttpResponse
from django.template import loader
from pyecharts import Line3D


def index(request):
    template = loader.get_template('echarts.html')
    l3d = line3d()
    context = dict(
        myechart=l3d.render_embed(),
        host="127.0.0.1",
        script_list=l3d.get_js_dependencies()
    )
    return HttpResponse(template.render(context, request))


def line3d():
    _data = []
    for t in range(0, 25000):
        _t = t / 1000
        x = (1 + 0.25 * math.cos(75 * _t)) * math.cos(_t)
        y = (1 + 0.25 * math.cos(75 * _t)) * math.sin(_t)
        z = _t + 2.0 * math.sin(75 * _t)
        _data.append([x, y, z])
    range_color = [
        '#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
        '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
    line3d = Line3D("3D line plot demo", width=1200, height=600)
    line3d.add("", _data, is_visualmap=True,
               visual_range_color=range_color, visual_range=[0, 30],
               is_grid3D_rotate=True, grid3D_rotate_speed=180)
    return line3d