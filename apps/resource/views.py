from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
# from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics
from rest_framework import filters
from rest_framework import viewsets
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

from django_filters.rest_framework import DjangoFilterBackend
from .models import *

from rest_framework.authentication import TokenAuthentication
from resource.filters import *
from .serializers import *
from rest_framework_extensions.cache.mixins import CacheResponseMixin

# Create your views here.


class ChartdataPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 100


class GwyjzwzzzyDbListViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
        商品列表数据,该注释直接会在docs文档中生成相关说明
    """
    queryset = GwyjzwzzzyDb.objects.all().order_by('id')
    pagination_class = ChartdataPagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)

    search_fields = ('id', "total_id", "name", "copes_category", 'copes_type', "category_name", "source", "distribution_unit", 'import_time', )
    ordering_fields = ('id', 'total_id')

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.click_num += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

