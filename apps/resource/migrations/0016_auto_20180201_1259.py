# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-01 12:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resource', '0015_auto_20180201_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yearbooks',
            name='caj',
            field=models.ImageField(blank=True, db_column='CAJ', null=True, upload_to='', verbose_name='CAJ'),
        ),
        migrations.AlterField(
            model_name='yearbooks',
            name='excel',
            field=models.ImageField(blank=True, db_column='EXCEL', null=True, upload_to='', verbose_name='EXCEL'),
        ),
        migrations.AlterField(
            model_name='yearbooks',
            name='pdf',
            field=models.ImageField(blank=True, db_column='PDF', null=True, upload_to='', verbose_name='PDF'),
        ),
    ]
