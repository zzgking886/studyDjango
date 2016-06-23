# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-21 08:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zzgSystemServer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VRVideoTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('videoImage', models.CharField(max_length=256, verbose_name='VR视频缩略图地址')),
                ('videoUrl', models.CharField(max_length=256, verbose_name='VR视频地址')),
                ('videoTitle', models.CharField(max_length=256, verbose_name='VR视频标题')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='发表时间')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
            ],
        ),
    ]