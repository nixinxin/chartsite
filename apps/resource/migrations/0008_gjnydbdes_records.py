# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-05-31 18:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resource', '0007_auto_20180421_2001'),
    ]

    operations = [
        migrations.AddField(
            model_name='gjnydbdes',
            name='records',
            field=models.IntegerField(blank=True, db_column='记录数', default=0, null=True, verbose_name='记录数'),
        ),
    ]
