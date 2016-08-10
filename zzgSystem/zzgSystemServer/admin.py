from django.contrib import admin

# Register your models here.
from .models import *


class UserTableAdmin(admin.ModelAdmin):
    list_display = ('userName', 'userNickName', 'userSex', 'pub_date', 'update_time')


class VRTableAdmin(admin.ModelAdmin):
    list_display = ('videoTitle', 'videoImage', 'videoUrl', 'pub_date', 'update_time')


admin.site.register(UserTable, UserTableAdmin)
admin.site.register(VRVideoTable, VRTableAdmin)