#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = "xin nix"

from rest_framework.validators import UniqueTogetherValidator
from operation.models import UserFav, FeedBack
from rest_framework import serializers
from chart.serializers import ChartSerializer


class UserFavDetailSerializer(serializers.Serializer):
    chart = ChartSerializer()

    class Meta:
        model = UserFav
        fields = ("user", 'chart', 'id')


class UserFavSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = UserFav

        validators = [
            UniqueTogetherValidator(
                queryset=UserFav.objects.all(),
                fields=("user", 'chart'),
                message="已经收藏"  # 不在指出具体字段的错误
            )
        ]

        fields = ("user", 'chart', 'id')


class FeedBackSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

    class Meta:
        model = FeedBack
        fields = "__all__"


