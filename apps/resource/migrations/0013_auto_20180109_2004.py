# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-09 20:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resource', '0012_auto_20180109_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nykjjgdblist',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]