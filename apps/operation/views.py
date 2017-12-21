from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication

from operation.models import UserFav, FeedBack
from operation.serializers import UserFavSerializer, UserFavDetailSerializer, FeedBackSerializer
from utils.permissions import IsOwnerOrReadOnly


# Create your views here.


class UserFavViewset(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin,
                     mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
        获取用户收藏列表
    retrieve:
        判断某个商品是否已经收藏，有则返回收藏商品详情
    create:
        添加商品收藏
    """
    # queryset = UserFav.objects.all()
    # 自定义用户权限
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

    serializer_class = UserFavSerializer

    # JSONWebTokenAuthentication是局部配置,需要配置JSONWebTokenAuthentication之后才能登录并传递token
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    # 默认通过id查找记录，改为
    lookup_field = 'chart_id'

    def get_queryset(self):
        return UserFav.objects.filter(user=self.request.user)

    # 可用信号量
    def perform_create(self, serializer):
        instance = serializer.save()


    def get_serializer_class(self):
        if self.action == 'list':
            return UserFavDetailSerializer
        elif self.action == 'create':
            return UserFavSerializer

        return UserFavSerializer


class FeedBackViewset(mixins.ListModelMixin, mixins.DestroyModelMixin, mixins.CreateModelMixin,
                            viewsets.GenericViewSet):
    """
    list:
        获取用户留言
    create:
        添加留言
    delete:
        删除留言功能
    """

    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = FeedBackSerializer

    def get_queryset(self):
        return FeedBack.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save()


