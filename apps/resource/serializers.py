#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = "xin nix"

from rest_framework import serializers
from .models import *


class Resourceserializer(serializers.ModelSerializer):

    class Meta:
        model = ResourceList
        fields = "__all__"
