# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2018-06-06 18:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zzgSystemServer', '0002_vrvideotable'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usertable',
            options={'verbose_name': '用户信息', 'verbose_name_plural': '用户信息'},
        ),
        migrations.AlterModelOptions(
            name='vrvideotable',
            options={'verbose_name': 'VR视频信息', 'verbose_name_plural': 'VR视频信息'},
        ),
    ]