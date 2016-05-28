# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-28 07:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testDjango', '0003_article'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.CharField(max_length=256, verbose_name='\u7528\u6237id')),
                ('userName', models.CharField(max_length=256, verbose_name='\u7528\u6237\u540d')),
                ('userNickName', models.CharField(max_length=256, verbose_name='\u7528\u6237\u6635\u79f0')),
                ('userSex', models.CharField(max_length=4, verbose_name='\u6027\u522b')),
            ],
        ),
    ]