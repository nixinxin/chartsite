# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-21 14:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chart',
            name='jsfile',
            field=models.FileField(db_column='js文件', default='chart1.js', upload_to='chart/js', verbose_name='js文件'),
        ),
    ]