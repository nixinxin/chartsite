# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-24 11:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resource', '0029_auto_20171124_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zgzynywhyc',
            name='clicks',
            field=models.CharField(blank=True, db_column='点击次数', max_length=10, null=True, verbose_name='点击次数'),
        ),
    ]
