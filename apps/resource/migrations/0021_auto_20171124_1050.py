# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-24 10:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resource', '0020_auto_20171124_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zgnttdzzdb',
            name='function_class',
            field=models.CharField(blank=True, db_column='功能类别', max_length=20, null=True, verbose_name='功能类别'),
        ),
    ]
