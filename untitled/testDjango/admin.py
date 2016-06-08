from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

class UserTableAdmin(admin.ModelAdmin):
    list_display = ('userName','userNickName','userSex','pub_date','update_time')

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','content','pub_date','update_time')

admin.site.register(Article,ArticleAdmin)
admin.site.register(Book)
admin.site.register(User)
admin.site.register(UserTable,UserTableAdmin)
