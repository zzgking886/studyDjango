from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

class UserTableAdmin(admin.ModelAdmin):
    list_display = ('userName','userNickName','userSex')

admin.site.register(Article)
admin.site.register(Book)
admin.site.register(User)
admin.site.register(UserTable,UserTableAdmin)
