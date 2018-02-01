# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-01 16:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resource', '0018_yearbookscover'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='yearbookscover',
            name='id',
        ),
        migrations.AlterField(
            model_name='yearbookscover',
            name='index',
            field=models.CharField(db_column='编号', max_length=20, primary_key=True, serialize=False, verbose_name='编号'),
        ),
    ]