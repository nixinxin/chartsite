# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-24 10:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resource', '0025_auto_20171124_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zgpgtlhcdb',
            name='desc',
            field=models.TextField(blank=True, db_column='生物学特性及发生消长规律', null=True, verbose_name='生物学特性及发生消长规律'),
        ),
    ]
