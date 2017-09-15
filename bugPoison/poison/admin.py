from django.contrib import admin

# Register your models here.
from .models import *


class UserTableAdmin(admin.ModelAdmin):
    list_display = ('userName', 'userLevel')


admin.site.register(bugUserTable, UserTableAdmin)