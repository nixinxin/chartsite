# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-08 14:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resource', '0008_auto_20180108_1228'),
    ]

    operations = [
        migrations.CreateModel(
            name='ZwyczytxpjjdDbList',
            fields=[
                ('id', models.IntegerField(auto_created=True, default=1, primary_key=True, serialize=False)),
                ('title', models.CharField(db_column='标题', max_length=20, verbose_name='标题')),
                ('table', models.CharField(db_column='表名', max_length=60, verbose_name='表名')),
                ('model', models.CharField(db_column='模型', max_length=60, verbose_name='模型')),
            ],
            options={
                'verbose_name': '作物遗传资源特性评价鉴定数据库列表',
                'db_table': '作物遗传资源特性评价鉴定数据库列表',
                'verbose_name_plural': '作物遗传资源特性评价鉴定数据库列表',
            },
        ),
    ]
