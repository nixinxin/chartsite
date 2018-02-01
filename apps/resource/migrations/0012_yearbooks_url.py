# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-01 10:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resource', '0011_yearbooks_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='yearbooks',
            name='url',
            field=models.URLField(blank=True, db_column='下载链接', max_length=100, null=True, verbose_name='下载链接'),
        ),
    ]
