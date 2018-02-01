# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-31 19:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resource', '0007_auto_20180129_1445'),
    ]

    operations = [
        migrations.CreateModel(
            name='YearBooks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_column='标题', max_length=60, verbose_name='标题')),
                ('category', models.CharField(db_column='类别', max_length=60, verbose_name='类别')),
                ('page', models.CharField(db_column='年鉴页码', max_length=20, verbose_name='年鉴页码')),
                ('identify', models.CharField(db_column='唯一编号', max_length=20, verbose_name='唯一编号')),
                ('year', models.CharField(db_column='年份', max_length=4, verbose_name='年份')),
                ('caj', models.IntegerField(db_column='CAJ', default=0, verbose_name='CAJ')),
                ('pdf', models.IntegerField(db_column='PDF', default=0, verbose_name='PDF')),
                ('excel', models.IntegerField(db_column='EXCEL', default=0, verbose_name='EXCEL')),
            ],
            options={
                'verbose_name_plural': '农业统计年鉴',
                'verbose_name': '农业统计年鉴',
                'db_table': '农业统计年鉴',
            },
        ),
    ]