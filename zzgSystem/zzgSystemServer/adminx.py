import xadmin
from .models import *
from xadmin import views


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class UserProfileAdmin(object):
    list_display = ['userId', 'userName', 'userNickName', 'userSex', 'pub_date', 'update_time']


class VRTableAdmin(object):
    list_display = ('videoTitle', 'videoImage', 'videoUrl', 'pub_date', 'update_time')


class GlobalSetting(object):
    site_title = '张振钢de系统'   #设置头标题
    site_footer = '张振钢de系统'  #设置脚标题
    menu_style = 'accordion'


xadmin.site.register(views.CommAdminView, GlobalSetting)
# xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(UserTable, UserProfileAdmin)
xadmin.site.register(VRVideoTable, VRTableAdmin)

