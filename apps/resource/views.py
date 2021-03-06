import os
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.views import View

from rest_framework.response import Response
from rest_framework import mixins, status
from rest_framework import filters
from rest_framework import viewsets
from rest_framework_extensions.cache.mixins import CacheResponseMixin
from rest_framework.pagination import PageNumberPagination

from pure_pagination import Paginator
from django_filters.rest_framework import DjangoFilterBackend

from chartsite.settings import BASE_DIR, MEDIA_URL
from .serializers import *
from .models import *


class CsvHtmlView(View):

    def get(self, request):
        title = request.GET.get("title", '')
        if title:
            return render_to_response('csvhtml.html', context={"title": title})
        items = CsvHtmls.objects.filter(category=3)
        page = request.GET.get('page', 0)
        counts = items.count()
        items = Paginator(items, 20, request=request)
        items = items.page(page)
        return render_to_response("csvmain.html",
                                  context={
                                      "items": items,
                                      "counts": counts,
                                  })


class CustomPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 20


class TpPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 300


class ResourceListPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 12


class ResourceListViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                          viewsets.GenericViewSet):
    """
    list:
        数据资源列表列表数据,该注释直接会在docs文档中生成相关说明
    """
    queryset = ResourceList.objects.all().order_by('id')
    pagination_class = ResourceListPagination
    serializer_class = Resourceserializer

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)

    search_fields = ('title',)
    ordering_fields = ('id',)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.click_num += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class GwyjzwzzzyDbListViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                              viewsets.GenericViewSet):
    """
    list:
        国外引进作物种质资源数据库列表数据,该注释直接会在docs文档中生成相关说明
    """

    queryset = GwyjzwzzzyDb.objects.all().order_by('id')
    serializer_class = GwyjzwzzzyDbserializer
    pagination_class = CustomPagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)

    search_fields = ('id', "total_id", "name", "copes_category", 'copes_type', "category_name", "source",
                     "distribution_unit", 'import_time',)
    ordering_fields = ('id', 'total_id')


class NcpjgDbListViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
       农产品价格行情数据库列表数据,该注释直接会在docs文档中生成相关说明
    """
    queryset = NcpjgDb.objects.all().order_by('datetime')
    serializer_class = NcpjgDbserializer
    pagination_class = CustomPagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)

    search_fields = ("category", 'product', 'market', 'datetime')
    ordering_fields = ('datetime',)


class AgriIndexViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
       农业统计指标列表数据,该注释直接会在docs文档中生成相关说明
    """
    queryset = AgriIndex.objects.all().order_by('id')
    serializer_class = AgriIndexserializer
    pagination_class = CustomPagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)

    search_fields = ("index", 'values', 'location', 'year')
    ordering_fields = ('year',)


class MytxDbViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
       农作物名优特新品种数据库列表数据,该注释直接会在docs文档中生成相关说明
    """
    queryset = MytxDb.objects.all().order_by('code')
    serializer_class = MytxDbserializer
    pagination_class = CustomPagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('name',)
    ordering_fields = ('code',)


class ZgnytdkcDbViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
       中国农业天敌昆虫数据库列表数据,该注释直接会在docs文档中生成相关说明
    """
    queryset = ZgnytdkcDb.objects.all().order_by('id')
    serializer_class = ZgnytdkcDbserializer
    pagination_class = CustomPagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    search_fields = ("zhname",)
    ordering_fields = ('id',)


class ZgnyyhswDbTpViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                          viewsets.GenericViewSet):
    """
    list:
       中国农业有害生物图片数据库列表数据,该注释直接会在docs文档中生成相关说明
    """
    queryset = ZgnyyhswDbTp.objects.all().order_by('id')
    serializer_class = ZgnyyhswDbTpserializer
    pagination_class = CustomPagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)


class ZgnttdzzDbViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
       中国农田天敌蜘蛛数据库列表数据,该注释直接会在docs文档中生成相关说明
    """
    queryset = ZgnttdzzDb.objects.all().order_by('report_id')
    serializer_class = ZgnttdzzDbserializer
    pagination_class = CustomPagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)

    ordering_fields = ('report_id',)


class ZgnthsDbViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
       中国农田害鼠数据库列表数据,该注释直接会在docs文档中生成相关说明
    """
    queryset = ZgnthsDb.objects.all().order_by('id')
    serializer_class = ZgnthsDbserializer
    pagination_class = CustomPagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)

    ordering_fields = ('id',)


class ZgyclschcDbViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
       中国叶菜类蔬菜害虫数据库列表数据,该注释直接会在docs文档中生成相关说明
    """
    queryset = ZgyclschcDb.objects.all().order_by('id')
    serializer_class = ZgyclschcDbserializer
    pagination_class = CustomPagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)

    ordering_fields = ('id',)


class WlyhwswDbViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
       中国外来入侵微生物数据库列表数据,该注释直接会在docs文档中生成相关说明
    """
    queryset = WlyhwswDb.objects.all().order_by('id')
    serializer_class = WlyhwswDbserializer
    pagination_class = CustomPagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)

    ordering_fields = ('id',)


class WlyhkcDbViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
       中国外来入侵昆虫数据库列表数据,该注释直接会在docs文档中生成相关说明
    """
    queryset = WlyhkcDb.objects.all().order_by('id')
    serializer_class = WlyhkcDbserializer
    pagination_class = CustomPagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)

    ordering_fields = ('id',)


class WlyhzwDbViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
       中国外来入侵植物数据库列表数据,该注释直接会在docs文档中生成相关说明
    """
    queryset = WlyhzwDb.objects.all().order_by('id')
    serializer_class = WlyhzwDbserializer
    pagination_class = CustomPagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)

    ordering_fields = ('id',)


class ZghdzcDbViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
       中国旱地杂草数据库列表数据,该注释直接会在docs文档中生成相关说明
    """
    queryset = ZghdzcDb.objects.all().order_by('id')
    serializer_class = ZghdzcDbserializer
    pagination_class = CustomPagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)

    ordering_fields = ('id',)


class ZghlzwhcDbViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
       中国旱粮作物害虫数据库列表数据,该注释直接会在docs文档中生成相关说明
    """
    queryset = ZghlzwhcDb.objects.all().order_by('id')
    serializer_class = ZghlzwhcDbserializer
    pagination_class = CustomPagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)

    ordering_fields = ('id',)


class ZggslschcDbViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
       中国果菜类蔬菜害虫数据库列表数据,该注释直接会在docs文档中生成相关说明
    """
    queryset = ZggslschcDb.objects.all().order_by('id')
    serializer_class = ZggslschcDbserializer
    pagination_class = CustomPagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)

    ordering_fields = ('id',)


class ZggjhcDbViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
       中国柑桔害虫数据库列表数据,该注释直接会在docs文档中生成相关说明
    """
    queryset = ZggjhcDb.objects.all().order_by('id')
    serializer_class = ZggjhcDbserializer
    pagination_class = CustomPagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)

    ordering_fields = ('id',)


class ZgmhhcDbViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
       中国棉花害虫数据库列表数据,该注释直接会在docs文档中生成相关说明
    """
    queryset = ZgmhhcDb.objects.all().order_by('id')
    serializer_class = ZgmhhcDbserializer
    pagination_class = CustomPagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)

    ordering_fields = ('id',)


class ZgstzcDbViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
       中国水田杂草数据库列表数据,该注释直接会在docs文档中生成相关说明
    """
    queryset = ZgstzcDb.objects.all().order_by('id')
    serializer_class = ZgstzcDbserializer
    pagination_class = CustomPagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)

    ordering_fields = ('id',)


class ZgsdhcDbViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
       中国水稻害虫数据库列表数据,该注释直接会在docs文档中生成相关说明
    """
    queryset = ZgsdhcDb.objects.all().order_by('id')
    serializer_class = ZgsdhcDbserializer
    pagination_class = CustomPagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)

    ordering_fields = ('id',)


class ZgtsNcpViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
       中国特色农产品列表数据,该注释直接会在docs文档中生成相关说明
    """
    queryset = ZgtsNcp.objects.all().order_by('id')
    serializer_class = ZgtsNcpserializer
    pagination_class = CustomPagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)

    ordering_fields = ('id',)


class ZglszwbdbhDbViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                          viewsets.GenericViewSet):
    """
    list:
       中国粮食作物病毒病害数据库列表数据,该注释直接会在docs文档中生成相关说明
    """
    queryset = ZglszwbdbhDb.objects.all().order_by('id')
    serializer_class = ZglszwbdbhDbserializer
    pagination_class = CustomPagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)

    ordering_fields = ('id',)


class ZglszwzjbhDbViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                          viewsets.GenericViewSet):
    """
    list:
       中国粮食作物真菌病害数据库列表数据,该注释直接会在docs文档中生成相关说明
    """
    queryset = ZglszwzjbhDb.objects.all().order_by('id')
    serializer_class = ZglszwzjbhDbserializer
    pagination_class = CustomPagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)

    ordering_fields = ('id',)


class ZglszwxjbhDbViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                          viewsets.GenericViewSet):
    """
    list:
       中国粮食作物细菌病害数据库列表数据,该注释直接会在docs文档中生成相关说明
    """
    queryset = ZglszwxjbhDb.objects.all().order_by('id')
    serializer_class = ZglszwxjbhDbserializer
    pagination_class = CustomPagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)

    ordering_fields = ('id',)


class ZgjjzwbdbhDbViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                          viewsets.GenericViewSet):
    """
    list:
       中国经济作物病毒病害数据库列表数据,该注释直接会在docs文档中生成相关说明
    """
    queryset = ZgjjzwbdbhDb.objects.all().order_by('id')
    serializer_class = ZgjjzwbdbhDbserializer
    pagination_class = CustomPagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)

    ordering_fields = ('id',)


class ZgjjzwzjbhDbViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                          viewsets.GenericViewSet):
    """
    list:
       中国经济作物真菌病害数据库列表数据,该注释直接会在docs文档中生成相关说明
    """
    queryset = ZgjjzwzjbhDb.objects.all().order_by('id')
    serializer_class = ZgjjzwzjbhDbserializer
    pagination_class = CustomPagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)

    ordering_fields = ('id',)


class ZgjjzwxjbhDbViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                          viewsets.GenericViewSet):
    """
    list:
       中国经济作物细菌病害数据库列表数据,该注释直接会在docs文档中生成相关说明
    """
    queryset = ZgjjzwxjbhDb.objects.all().order_by('id')
    serializer_class = ZgjjzwxjbhDbserializer
    pagination_class = CustomPagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)

    ordering_fields = ('id',)


class ZgpgtlhcDbViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
       中国苹果桃梨害虫数据库列表数据,该注释直接会在docs文档中生成相关说明
    """
    queryset = ZgpgtlhcDb.objects.all().order_by('id')
    serializer_class = ZgpgtlhcDbserializer
    pagination_class = CustomPagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)

    ordering_fields = ('id',)


class ZgxzqhDbViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
       中国行政区划数据库列表数据,该注释直接会在docs文档中生成相关说明
    """
    queryset = ZgxzqhDb.objects.all().order_by('citycode')
    serializer_class = ZgxzqhDbserializer
    pagination_class = CustomPagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)

    ordering_fields = ('citycode',)


class ZgzynywhYcViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
       中国重要农业文化遗产列表数据,该注释直接会在docs文档中生成相关说明
    """
    queryset = ZgzynywhYc.objects.all().order_by('id')
    serializer_class = ZgzynywhYcserializer
    pagination_class = CustomPagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)


class ZgzynywhycTpViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                          viewsets.GenericViewSet):
    """
    list:
       中国重要农业文化遗产图片列表数据,该注释直接会在docs文档中生成相关说明
    """
    queryset = ZgzynywhycTp.objects.all().order_by('id')
    serializer_class = ZgzynywhycTpserializer
    pagination_class = CustomPagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)


class ZwwzfbDbViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
       作物物种分布数据库列表数据,该注释直接会在docs文档中生成相关说明
    """
    queryset = ZwwzfbDb.objects.all().order_by('title')
    serializer_class = ZwwzfbDbserializer
    pagination_class = CustomPagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)


class XmzzzzhxzzDbViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                          viewsets.GenericViewSet):
    """
    list:
       小麦种质资源核心种质数据库列表数据,该注释直接会在docs文档中生成相关说明
    """
    queryset = XmzzzzhxzzDb.objects.all().order_by('id')
    serializer_class = XmzzzzhxzzDbserializer
    pagination_class = CustomPagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)


class XmxpDbViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
       小麦系谱数据库列表数据,该注释直接会在docs文档中生成相关说明
    """
    queryset = XmxpDb.objects.all().order_by('id')
    serializer_class = XmxpDbserializer
    pagination_class = CustomPagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    ordering_fields = ('id',)


class XmxcpzjqxpDbViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                          viewsets.GenericViewSet):
    """
    list:
       小麦育成品种及其系谱数据库列表数据,该注释直接会在docs文档中生成相关说明
    """
    queryset = XmxcpzjqxpDb.objects.all().order_by('total_id')
    serializer_class = XmxcpzjqxpDbserializer
    pagination_class = CustomPagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    ordering_fields = ('total_id',)


class SdzzzzhxzzDbViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                          viewsets.GenericViewSet):
    """
    list:
       水稻种质资源核心种质数据库列表数据,该注释直接会在docs文档中生成相关说明
    """
    queryset = SdzzzzhxzzDb.objects.all().order_by('total_id')
    serializer_class = SdzzzzhxzzDbserializer
    pagination_class = CustomPagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    ordering_fields = ('total_id',)


class SdycpzjqpxDbViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                          viewsets.GenericViewSet):
    """
    list:
       水稻育成品种及其系谱数据库列表数据,该注释直接会在docs文档中生成相关说明
    """
    queryset = SdycpzjqpxDb.objects.all().order_by('total_id')
    serializer_class = SdycpzjqpxDbserializer
    pagination_class = CustomPagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    ordering_fields = ('total_id',)


class YmxpzbhDbViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
       玉米新品种保护数据库列表数据,该注释直接会在docs文档中生成相关说明
    """
    queryset = YmxpzbhDb.objects.all().order_by('id')
    serializer_class = YmxpzbhDbserializer
    pagination_class = CustomPagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    ordering_fields = ('id',)


class YmzzzzhxzzDbViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                          viewsets.GenericViewSet):
    """
    list:
       玉米种质资源核心种质数据库列表数据,该注释直接会在docs文档中生成相关说明
    """
    queryset = YmzzzzhxzzDb.objects.all().order_by('total_id')
    serializer_class = YmzzzzhxzzDbserializer
    pagination_class = CustomPagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    ordering_fields = ('total_id',)


class XdnysfqViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
       现代农业示范区列表数据,该注释直接会在docs文档中生成相关说明
    """
    queryset = Xdnysfq.objects.all().order_by('title')
    serializer_class = Xdnysfqserializer
    pagination_class = CustomPagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)


class ZwyyzyzzDbViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
       作物优异资源种质数据库列表数据,该注释直接会在docs文档中生成相关说明
    """
    queryset = ZwyyzyzzDb.objects.all().order_by('id')
    serializer_class = ZwyyzyzzDbserializer
    pagination_class = CustomPagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)


class YoudamaiViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
       优异资源综合评价数据库_大麦列表数据,该注释直接会在docs文档中生成相关说明
    """
    queryset = Youdamai.objects.all().order_by('id')
    serializer_class = Youdamaiserializer
    pagination_class = CustomPagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    ordering_fields = ('id',)


class YouYuMiViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
       优异资源综合评价数据库_玉米列表数据,该注释直接会在docs文档中生成相关说明
    """
    queryset = YouYuMi.objects.all().order_by('id')
    serializer_class = YouYuMiserializer
    pagination_class = CustomPagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    ordering_fields = ('id',)


class ZwyczytxpjjdDbListViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.CreateModelMixin,
                                viewsets.GenericViewSet):
    """
    list:
       作物遗传资源特性评价鉴定数据库列表 列表数据,该注释直接会在docs文档中生成相关说明
    """
    queryset = ZwyczytxpjjdDbList.objects.all().order_by("id")
    serializer_class = ZwyczytxpjjdDbserializer
    pagination_class = CustomPagination
    ordering_fields = ('id',)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        title = serializer.validated_data['table']
        try:
            with open(os.path.join(BASE_DIR, "media", 'html', "{}.html".format(title)), 'r', encoding='utf-8') as f:
                data = f.read()
        except:
            data = None
        header = {
            "status": status.HTTP_200_OK,
            'content_type': "text/html",
        }
        return HttpResponse(content=data, **header)


class GjnykyhzxmDbViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                          viewsets.GenericViewSet):
    """
    list:
       国际农业科研项目数据库列表数据,该注释直接会在docs文档中生成相关说明
    """
    queryset = GjnykyhzxmDb.objects.all().order_by('code')
    serializer_class = GjnykyhzxmDbserializer
    pagination_class = CustomPagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('title',)
    ordering_fields = ('code',)


class GnnykyhzxmDbViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                          viewsets.GenericViewSet):
    """
    list:
       国内农业科技项目数据库列表数据,该注释直接会在docs文档中生成相关说明
    """
    queryset = GnnykyhzxmDb.objects.all().order_by('code')
    serializer_class = GnnykyhzxmDbserializer
    pagination_class = CustomPagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('title',)
    ordering_fields = ('code',)


class NyhjkjcgDbViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
       农业获奖科技成果数据库列表数据,该注释直接会在docs文档中生成相关说明
    """
    queryset = NyhjkjcgDb.objects.all().order_by('code')
    serializer_class = NyhjkjcgDbserializer
    pagination_class = CustomPagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('title',)
    ordering_fields = ('code',)


class NykjrcDbViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
       农业科技人才数据库列表数据,该注释直接会在docs文档中生成相关说明
    """
    queryset = NykjrcDb.objects.all().order_by('code')
    serializer_class = NykjrcDbserializer
    pagination_class = CustomPagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('name',)
    ordering_fields = ('code',)


class NykjjgDbViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
       农业科技机构数据库列表数据,该注释直接会在docs文档中生成相关说明
    """
    queryset = NykjjgDb.objects.all().order_by('unitid')
    serializer_class = NykjjgDbserializer
    pagination_class = CustomPagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    search_fields = ("unitid", 'gfmc')
    ordering_fields = ('unitid',)


class ZwkjwxDbViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
       中文农业科技文摘数据库列表数据,该注释直接会在docs文档中生成相关说明
    """
    queryset = ZwkjwxDb.objects.all().order_by('code')
    serializer_class = ZwkjwxDbserializer
    pagination_class = CustomPagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)

    search_fields = ('title',)
    ordering_fields = ('code',)


class YjnyDbViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
       有机农业数据库列表数据,该注释直接会在docs文档中生成相关说明
    """
    queryset = YjnyDb.objects.all().order_by('reportid')
    serializer_class = YjnyDbserializer
    pagination_class = CustomPagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)

    search_fields = ("reportid", 'title')
    ordering_fields = ('reportid',)


class NygjDbViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
       农业古籍数据库列表数据,该注释直接会在docs文档中生成相关说明, ?reportid=GJ00001
    """
    queryset = NygjDb.objects.all().order_by('reportid')
    serializer_class = NygjDbserializer
    pagination_class = CustomPagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)

    search_fields = ("reportid", 'title')
    ordering_fields = ('id',)


class NygjtpDbViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
       农业古籍图片数据库列表数据,该注释直接会在docs文档中生成相关说明,
    """
    queryset = NygjtpDb.objects.all().order_by('id')
    serializer_class = NygjtpDbserializer
    search_fields = ("reportid__reportid",)
    ordering_fields = ('id',)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    pagination_class = TpPagination


class NybzhczgfDbViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
       农业标准和操作规范数据库列表数据,该注释直接会在docs文档中生成相关说明
    """
    queryset = NybzhczgfDb.objects.all().order_by('bzid')
    serializer_class = NybzhczgfDbserializer
    pagination_class = CustomPagination

    search_fields = ("bzname",)
    ordering_fields = ('bzid',)

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)


class NykjzcfgDbViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
       农业科技政策法规数据库列表数据,该注释直接会在docs文档中生成相关说明
    """
    queryset = NykjzcfgDb.objects.all().order_by('code')
    serializer_class = NykjzcfgDbserializer
    pagination_class = CustomPagination

    search_fields = ("zcfgmc",)
    ordering_fields = ('code',)

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)


class XqfzffDbViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
       畜禽常见疾病及防治方法数据库列表数据,该注释直接会在docs文档中生成相关说明
    """
    queryset = XqfzffDb.objects.all().order_by('code')
    serializer_class = XqfzffDbserializer
    pagination_class = CustomPagination

    search_fields = ("jbmc",)
    ordering_fields = ('code',)

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)


class YearsDownViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    list:
       统计年鉴下载接口 数据,该注释直接会在docs文档中生成相关说明
    """
    queryset = YearBooks.objects.all().order_by("identify")
    serializer_class = YearBooksserializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        index = serializer.validated_data['index']
        file_type = serializer.validated_data['type']
        queryset = YearBooks.objects.get(identify=index)
        file_url = getattr(queryset, file_type)
        filepath = os.path.join(MEDIA_URL, file_url)
        return HttpResponseRedirect(redirect_to=filepath)


class BookViews(View):

    def get(self, request):
        return render(request, "books.html")


class ResourceView(View):
    techdata = {
        "中文农业科技文摘数据库": ZwkjwxDb,
        "农业古籍数据库": NygjDb,
        "农业标准和操作规范数据库": NybzhczgfDb,
        "农业科技人才数据库": NykjrcDb,
        "农业科技政策法规数据库": NykjzcfgDb,
        "农业科技机构数据库": NykjjgDb,
        "农业获奖科技成果数据库": NyhjkjcgDb,
        "农作物名优特新品种数据库": MytxDb,
        "国内农业科研项目数据库": GnnykyhzxmDb,
        "国际农业科研项目数据库": GjnykyhzxmDb,
        "外文农业科技文摘数据库": WwkjwxDb,
        "有机农业数据库": YjnyDb,
        "畜禽常见疾病及防治方法数据库": XqfzffDb,
    }

    pestset = {
        "中国农业害鼠数据库": ZgnthsDb,
        "中国旱地杂草数据库": ZghdzcDb,
        "中国柑桔害虫数据库": ZggjhcDb,
        "中国棉花害虫数据库": ZgmhhcDb,
        "中国水田杂草数据库": ZgstzcDb,
        "中国水稻害虫数据库": ZgsdhcDb,
        "外来有害昆虫数据库": WlyhkcDb,
        "外来有害植物数据库": WlyhzwDb,
        "外来有害微生物数据库": WlyhwswDb,
        "中国农业天敌昆虫数据库": ZgnytdkcDb,
        "中国农业天敌蜘蛛数据库": ZgnttdzzDb,
        "中国旱粮作物害虫数据库": ZghlzwhcDb,
        "中国苹果桃梨害虫数据库": ZgpgtlhcDb,
        "中国叶菜类蔬菜害虫数据库": ZgyclschcDb,
        "中国果菜类蔬菜害虫数据库": ZggslschcDb,
        "中国粮食作物病毒病害数据库": ZglszwbdbhDb,
        "中国粮食作物真菌病害数据库": ZglszwzjbhDb,
        "中国粮食作物细菌病害数据库": ZglszwxjbhDb,
        "中国经济作物病毒病害数据库": ZgjjzwbdbhDb,
        "中国经济作物真菌病害数据库": ZgjjzwzjbhDb,
        "中国经济作物细菌病害数据库": ZgjjzwxjbhDb,
    }

    def get(self, request):

        response_type = request.GET.get("type", '')
        if response_type == 'agritech':
            select = request.GET.get('select', 96)
            select = int(select)
            databases = GjnydbDes.objects.filter(category="农业科技资源数据").order_by('index')
            database = GjnydbDes.objects.get(id=select).title
            page = request.GET.get('page', 1)
            index = request.GET.get('index', "")
            display_fields = AgriTechContent.objects.filter(title=database, display=1).order_by("index")
            if index:
                detail_fields = AgriTechContent.objects.filter(title=database).order_by("index")
                detailkey = ["id"]
                for key in detail_fields:
                    detailkey.append(key.content)
                items = self.techdata[database].objects.filter(id=index).values_list()
                detail = []
                for num in range(0, len(detailkey)):
                    detail.append({"key": detailkey[num], 'value': items[0][num]})
                return render_to_response('techdetail.html', {
                    "items": items,
                    "select": select,
                    "databases": databases,
                    "detail": detail,
                })
            content_fields = display_fields.values_list('english')
            contents = ['id', ]
            for i in content_fields:
                contents.append(i[0])
            items = self.techdata[database].objects.all().values_list(*contents)
            items_num = items.count()
            items = Paginator(items, 20, request=request)

            items = items.page(page)
            return render_to_response('tech.html', {
                "display_fields": display_fields,
                "items": items,
                "items_num": items_num,
                "select": select,
                "databases": databases,
            })
        elif response_type == 'pest':

            select = request.GET.get('select', 54)
            select = int(select)
            databases = GjnydbDes.objects.filter(category="农业有害生物数据").order_by('index')
            database = GjnydbDes.objects.get(id=select).title

            page = request.GET.get('page', 1)

            index = request.GET.get('index', "")
            display_fields = FieldContent.objects.filter(title=database, display=1).order_by("index")
            if index:
                detail_fields = FieldContent.objects.filter(title=database).order_by("index")
                detailkey = ["id"]
                for key in detail_fields:
                    detailkey.append(key.content)
                items = self.pestset[database].objects.filter(id=index).values_list()
                detail = []
                for num in range(0, len(detailkey)):
                    detail.append({"key": detailkey[num], 'value': items[0][num]})
                return render_to_response('pestdetail.html', {
                    "items": items,
                    "select": select,
                    "databases": databases,
                    "detail": detail,
                })
            content_fields = display_fields.values_list('english')
            contents = ['id', ]
            for i in content_fields:
                contents.append(i[0])
            items = self.pestset[database].objects.all().values_list(*contents)
            items_num = items.count()
            items = Paginator(items, 20, request=request)
            items = items.page(page)
            return render_to_response('pest.html', {
                "display_fields": display_fields,
                "items": items,
                "items_num": items_num,
                "select": select,
                "databases": databases,
            })
        elif response_type == 'years':

            year = request.GET.get('select', "2016")
            yearlist = YearBooksDes.objects.all().order_by('-year')
            yearsinfo = yearlist.get(year=year)

            sunxu = request.GET.get('shunxu', 0)

            page = request.GET.get('page', 0)
            content = YearBooksContent.objects.filter(year=year)
            if sunxu:
                mulu = YearBooksContent.objects.get(year=year, index=sunxu).content
                items = YearBooks.objects.filter(year=year, category=mulu).order_by("id")
            else:
                items = YearBooks.objects.filter(year=year).order_by("id")

            counts = items.count()
            items = Paginator(items, 20, request=request)
            items = items.page(page)
            return render_to_response("years.html",
                                      context={
                                          "yearsinfo": yearsinfo,
                                          "content": content,
                                          "items": items,
                                          "yearlist": yearlist,
                                          "counts": counts,
                                      })
        elif response_type == 'genetic ':
            select = request.GET.get('select', 25)
            if int(select) == 25:
                items = CsvHtmls.objects.all()
                page = request.GET.get('page', 0)
                counts = items.count()
                items = Paginator(items, 20, request=request)
                items = items.page(page)
                return render_to_response("csvmain.html",
                                          context={
                                              "items": items,
                                              "counts": counts,
                                          })
        else:
            yearlist = YearBooksDes.objects.all().order_by('-year')
            agritech = GjnydbDes.objects.filter(category='农业科技资源数据').order_by('index')
            crop = GjnydbDes.objects.filter(category='作物品种品质数据').order_by('index')
            pest = GjnydbDes.objects.filter(category='农业有害生物数据').order_by('index')
            product = GjnydbDes.objects.filter(category='农产品资源数据').order_by('index')
            genetic = GjnydbDes.objects.filter(category='作物遗传资源数据').order_by('index')
            return render_to_response("resource.html",
                                      context={
                                          "yearlist": yearlist,
                                          "agritech": agritech,
                                          "pest": pest,
                                          "crop": crop,
                                          "product": product,
                                          "genetic": genetic,
                                      })


class HeritageView(View):
    pici = {1: "第一批", 2: "第二批", 3: "第三批", 4: "第四批"}

    def get(self, request):
        category = request.GET.get("pici", 1)
        pici = self.pici[category]
        items = ZgzynywhYc.objects.filter(pici=pici)
        cycles = [1, 5, 9, 13, 17]
        return render_to_response('heritage.html', context={"items": items, 'cycles': cycles})
