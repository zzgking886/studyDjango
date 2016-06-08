# coding:utf-8
from __future__ import unicode_literals
from django.db import models
from django.contrib import admin

# create model and sync database tables
# Author.objects.get_or_create(name="WeizhongTu", email="tuweizhong@163.com")

class Book(models.Model):
    name = models.CharField(max_length=100)
    userId = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class User(models.Model):
    userId = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)

    def __str__(self):
        return self.nickname

class Article(models.Model):
    title = models.CharField('标题', max_length=256)
    content = models.TextField('内容')

    pub_date = models.DateTimeField('发表时间', auto_now_add=True, editable = True)
    update_time = models.DateTimeField('更新时间',auto_now=True, null=True)

    def __str__(self):
        return self.title

class UserTable(models.Model):
    userId = models.CharField('用户id', max_length=256)
    userName = models.CharField('用户名', max_length=256)
    userNickName = models.CharField('用户昵称', max_length=256)
    userSex = models.CharField('性别', max_length=4)
    pub_date = models.DateTimeField('发表时间', auto_now_add=True, editable = True)
    update_time = models.DateTimeField('更新时间',auto_now=True, null=True)

    def __str__(self):
        return self.userId






