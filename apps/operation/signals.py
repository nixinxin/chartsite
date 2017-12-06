#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = "xin nix"
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from operation.models import UserFav


@receiver(post_save, sender=UserFav)
def create_userfav(sender, instance=None, created=False, **kwargs):
    if created:
        chart = instance.chart
        chart.fav_num += 1
        chart.save()


@receiver(post_delete, sender=UserFav)
def delete_userfav(sender, instance=None, created=False, **kwargs):
    chart = instance.chart
    chart.fav_num -= 1
    chart.save()


