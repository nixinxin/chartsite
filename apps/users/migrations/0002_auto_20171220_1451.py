# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-20 14:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailcode',
            name='code',
            field=models.CharField(max_length=16, verbose_name='验证码'),
        ),
    ]