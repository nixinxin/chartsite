# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-31 19:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resource', '0008_yearbooks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yearbooks',
            name='caj',
            field=models.IntegerField(blank=True, db_column='CAJ', default=0, null=True, verbose_name='CAJ'),
        ),
        migrations.AlterField(
            model_name='yearbooks',
            name='excel',
            field=models.IntegerField(blank=True, db_column='EXCEL', default=0, null=True, verbose_name='EXCEL'),
        ),
        migrations.AlterField(
            model_name='yearbooks',
            name='pdf',
            field=models.IntegerField(blank=True, db_column='PDF', default=0, null=True, verbose_name='PDF'),
        ),
    ]