from django.db import models

# Create your models here.

class bugUserTable(models.Model):
    userId = models.CharField('用户id', max_length=255, primary_key=True)
    userName = models.CharField('用户名', max_length=255)
    userLevel = models.CharField('用户等级', max_length=4)
    register_time = models.DateTimeField('注册时间', auto_now_add=True, editable=True)

    def __str__(self):
        return self.userName
