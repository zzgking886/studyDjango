"""zzgSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from zzgSystemServer.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import staticfiles
import xadmin
from zzgSystemServer.views import LoginView

urlpatterns = [
    url(r'^usertablelist', userTableList),
    url(r'^userlogin', csrf_exempt(LoginView.as_view())),
    url(r'^vrtablelist', vrTableList),
    url(r'^checkbundleid', checkBundleId),
    url(r'^testwebview/', testWebView),
    url(r'^testindex01', testindex01),
    url(r'^testindex02', testindex02),
    url(r'^testcanvas', testcanvas),
    url(r'^testcanvastwo', testcanvastwo),
    url(r'^testvideoPage', testvideoPage),
    url(r'^testformCommit', testformCommit),
    url(r'^testLocalStorege', testLocalStorege),
    url(r'^testReponseDesign', testReponseDesign),
    url(r'^checkcntv', cntvInterFaceCheck),
    url(r'^testLiveReturn', testLiveReturn),
    url(r'^testiosplayer', testiosplay),
    url(r'^testiosaudioplay', testiosaudioplay),
    url(r'^checkInterface', checkInterface),
    url(r'', xadmin.site.urls),
    url(r'^checkpublic',checkPublic),
]
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()
# urlpatterns += static('/htmlPage/',document_root = '/Users/zzg/PycharmProjects/zzgSystem/htmlPage/')
# urlpatterns += static('','','/Users/zzg/PycharmProjects/zzgSystem/htmlPage/image')
