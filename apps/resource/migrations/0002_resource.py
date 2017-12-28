# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-28 14:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resource', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_column='标题', max_length=30, null=True, verbose_name='标题')),
                ('type', models.CharField(choices=[(1, '农业'), (2, '林业'), (3, '牧业'), (4, '渔业'), (5, '农村'), (6, '农民'), (7, '植物'), (7, '动物')], db_column='类别', max_length=30, verbose_name='类别')),
                ('desc', models.TextField(default='', help_text='数据描述', verbose_name='数据描述')),
                ('image', models.ImageField(db_column='数据封面', upload_to='chartsite/resource', verbose_name='数据封面')),
                ('click_num', models.IntegerField(default=0, verbose_name='点击数')),
                ('fav_num', models.IntegerField(default=0, verbose_name='收藏数')),
                ('is_tab', models.BooleanField(db_column='是否导航', default=False, verbose_name='是否导航')),
                ('is_new', models.BooleanField(db_column='是否最新', default=False, verbose_name='是否最新')),
                ('is_hot', models.BooleanField(db_column='是否热门', default=False, verbose_name='是否热门')),
                ('add_time', models.DateTimeField(db_column='添加时间', default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '资源列表',
                'db_table': '资源列表',
                'verbose_name_plural': '资源列表',
            },
        ),
    ]