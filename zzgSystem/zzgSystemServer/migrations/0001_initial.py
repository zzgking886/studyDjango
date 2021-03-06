# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-07 07:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.CharField(max_length=256, verbose_name='用户id')),
                ('userName', models.CharField(max_length=256, verbose_name='用户名')),
                ('userNickName', models.CharField(max_length=256, verbose_name='用户昵称')),
                ('userSex', models.CharField(max_length=4, verbose_name='性别')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='发表时间')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
            ],
        ),
    ]
