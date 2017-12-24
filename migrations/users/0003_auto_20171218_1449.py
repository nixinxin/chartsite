# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-18 14:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_emailcode_imagecode_phonecode'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailcode',
            name='send_type',
            field=models.CharField(choices=[('register', '注册'), ('forget', '找回密码'), ('update_email', '修改邮箱')], default='register', max_length=30, verbose_name='验证码类型'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='users/image/default.png', upload_to='users/image/%Y/%m'),
        ),
    ]