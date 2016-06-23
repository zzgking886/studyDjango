from django.db import models

# Create your models here.
class UserTable(models.Model):
    userId = models.CharField('用户id', max_length=256)
    userName = models.CharField('用户名', max_length=256)
    userNickName = models.CharField('用户昵称', max_length=256)
    userSex = models.CharField('性别', max_length=4)
    pub_date = models.DateTimeField('发表时间', auto_now_add=True, editable = True)
    update_time = models.DateTimeField('更新时间',auto_now=True, null=True)

    def __str__(self):
        return self.userId

class VRVideoTable(models.Model):
    videoImage = models.CharField('VR视频缩略图地址', max_length=256)
    videoUrl = models.CharField('VR视频地址', max_length=256)
    videoTitle = models.CharField('VR视频标题', max_length=256)
    pub_date = models.DateTimeField('发表时间', auto_now_add=True, editable = True)
    update_time = models.DateTimeField('更新时间', auto_now=True, null=True)

    def __str__(self):
        return  self.videoTitle