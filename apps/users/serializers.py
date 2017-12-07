#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = "xin nix"

from apps.users.models import PhoneCode, EmailCode, ImageCode

import re
from rest_framework import serializers
from django.contrib.auth import get_user_model
from datetime import datetime, timedelta
from chartsite.settings import REGEX_MOBILE, REGEX_EMAIL
from rest_framework.validators import UniqueValidator

User = get_user_model()


class PhoneSerialier(serializers.Serializer):
    mobile = serializers.CharField(max_length=11, min_length=11)

    def validate_mobile(self, mobile):
        """
        验证手机号码
        :param moobile:
        :return:
        """
        # 手机是否注册
        if User.objects.filter(mobile=mobile).count():
            raise serializers.ValidationError("用户已经存在")

        # 验证手机号码是否合法
        if not re.match(REGEX_MOBILE, mobile):
            raise serializers.ValidationError("手机号码非法")

        # 验证发送频率
        one_mintes_ago = datetime.now() - timedelta(hours=0, minutes=1, seconds=0)
        if PhoneCode.objects.filter(add_time__gt=one_mintes_ago, mobile=mobile):
            raise serializers.ValidationError("距离上一次发送未超过60s")
        return mobile


class EmailSerialier(serializers.Serializer):
    email = serializers.CharField(max_length=20, min_length=4)

    def validate_email(self, email):
        """
        验证邮箱
        :param email:
        :return:
        """
        # 邮箱是否注册
        if User.objects.filter(email=email).count():
            raise serializers.ValidationError("用户已经存在")

        # 验证邮箱是否合法
        if not re.match(REGEX_EMAIL, email):
            raise serializers.ValidationError("邮箱非法")

        # 验证发送频率
        one_mintes_ago = datetime.now() - timedelta(hours=0, minutes=0, seconds=10)
        if EmailCode.objects.filter(add_time__gt=one_mintes_ago, email=email):
            raise serializers.ValidationError("距离上一次发送未超过10s")
        return email


# class ImageCodeSerialier(serializers.Serializer):
#     code = serializers.FloatField()
#
#     def validate_code(self, code):
#         """
#         验证图片验证码
#         :param email:
#         :return:
#         """
#         # 验证图片验证码
#         if not ImageCode.objects.filter(code=code).exists():
#             raise serializers.ValidationError("Not Found")
#         return code


class UserDetailSerializer(serializers.ModelSerializer):
    """
    用户详情序列化类
    """
    class Meta:
        model = User
        # write_only：True只写不序列化返回
        fields = ("name", 'gender', 'birthday', 'mobile', 'email')


class UserRegSerializer(serializers.ModelSerializer):
    code = serializers.CharField(max_length=4,
                                 min_length=4,
                                 required=True,
                                 write_only=True,
                                 error_messages={
                                     "blank": '请输入验证码',
                                     "required": '请输入验证码',
                                     "max_length": "验证码格式错误",
                                     "min_length": "验证码格式错误",
                                 },
                                 label="验证码",
                                 )

    # username = serializers.CharField(required=True, max_length=11, min_length=11, allow_blank=False, help_text="用户名)
    username = serializers.CharField(required=True,
                                     allow_blank=False,
                                     validators=[UniqueValidator(queryset=User.objects.all(), message='用户已存在')],
                                     label="用户名",
                                     )


    # write_only：True只写不序列化返回
    password = serializers.CharField(style={"input_type": 'password'}, label="密码", write_only=True)  # 设置密文style

    # 将密码明文变成密文 也可以使用signal
    def create(self, validated_data):
        user = super(UserRegSerializer, self).create(validated_data=validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def validate_code(self, code):
        verify_records = PhoneCode.objects.filter(mobile=self.initial_data['username']).order_by('add_time')
        if verify_records:
            last_record = verify_records[0]
            five_mintes_ago = datetime.now() - timedelta(hours=0, minutes=100, seconds=0)
            if five_mintes_ago > last_record.add_time:
                raise serializers.ValidationError("验证码过期")
            if last_record.code != code:
                raise serializers.ValidationError("验证码错误")
        else:
            raise serializers.ValidationError("验证码错误")

    # 作用于所有字段之上
    def validate(self, attrs):
        attrs['mobile'] = attrs['username']
        del attrs['code']
        return attrs

    class Meta:
        model = User
        # write_only：True只写不序列化返回
        fields = ("username", 'password', 'code', 'mobile', 'email')


