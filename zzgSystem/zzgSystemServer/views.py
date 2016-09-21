from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from zzgSystemServer.models import UserTable
from zzgSystemServer.models import VRVideoTable
from zzgSystemServer.serializers import UserTableSerializers
from zzgSystemServer.serializers import VRVideoSerializers
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.core.cache import cache
from django.views.decorators.cache import cache_page
import json
from django.template import Template, Context
# Create your views here.

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwagrs):
        content = JSONRenderer().render(data)
        super(JSONResponse, self).__init__(content, **kwagrs)


@csrf_exempt  # POST方法
def userLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pwd']
        if username == 'zzg' and password == 'wushixia1119':
            dicResult = {'code': '200', 'status': 'success'}
            return JSONResponse(dicResult)
        else:
            return JSONResponse({'code': '404', 'status': 'fail'})
    else:
        return JSONResponse({'code': '404', 'status': 'fail'})


def userTableList(request):
    if request.method == 'GET':
        usertablelist = UserTable.objects.all()
        usertable = UserTableSerializers(usertablelist, many=True)
        dicResult = {'code': 200, 'data': usertable.data}
        return JSONResponse(dicResult)


# def vrTableList(request):
# if request.method == 'GET':
#         data = read_from_cache('vrtableList','vrtableList')
#         if data:
#             data = {'code':200,'data':data,'from':'redis'}
#             return JSONResponse(data)
#         else:
#             vrtablelist = VRVideoTable.objects.all()
#             vrtable = VRVideoSerializers(vrtablelist, many=True)
#             dicResult = {'code':200,'data':vrtable.data}
#             # write_to_cache('vrTableList',vrtable.data)
#             return JSONResponse(dicResult)

def vrTableList(request):
    if request.method == 'GET':
        if cache.get('vrtablelist'):
            vrlist = cache.get('vrtablelist')
            vrtable = VRVideoSerializers(vrlist, many=True)
            dicResult = {'code': 200, 'cache': 'true', 'data': vrtable.data}
        else:
            vrtablelist = VRVideoTable.objects.all()
            vrtable = VRVideoSerializers(vrtablelist, many=True)
            dicResult = {'code': 200, 'data': vrtable.data}
            cache.set('vrtablelist', vrtablelist)
        return JSONResponse(dicResult)


def checkBundleId(request):
    if request.method == 'GET':
        dicResult = {}
        bundId = request.GET['id']
        bundIdList = ['cn.cntv.apps.uyntv', 'cn.cntv.apps.uyntvHD',
                      'com.cctv.cmtviphone', 'cn.cntv.apps.kzntvHD',
                      'cn.cntv.apps.kzntv', 'cn.cntv.dianshibaoipad',
                      'cn.cntv.dianshibao', 'com.cctv.livechina', 'com.cntv.sportslive', 'com.cctv.ipad.mobiletv',
                      'cn.vuclip.mobiletv', 'com.cntv.cctvcom', 'com.cntv.yangshiweishi',
                      'cn.cctv.news',
                      'cn.cntv.neulion.5plusVIP',
                      'cn.cntv.iPanda',
                      'cn.cctv.iphone.CntvVideoNews',
                      'cn.cntv.d.F1SaiChe',
                      'cn.cntv.d.JiaoHuanKongJian',
                      'com.cctvcommobile.HuiHuang90NianHD',
                      'com.cntv.hh90year',
                      'cn.cntv.apps.mongolntv',
                      'cntv.weiboreader',
                      'com.cctv.cntv.paike',
                      'cn.cntv.apps.caijingpindao',
                      'com.cntv.cntvlive',
                      'com.cntv.cctvweishi',
                      'com.cctv.cctvnews',
                      'com.cctv.cctvarabic',
                      'com.cctv.cctvrussian',
                      'com.cctv.cctvfrench',
                      'com.cctv.cctvspanish',
                      'com.cctv.cctvnews.ipad',
                      'com.cctv.atchina']
        for oneBundleId in bundIdList:
            print(bundId)
            if oneBundleId == bundId:
                dicResult = {'code':200, 'data':'这是一个有效ID','bundleId':bundId}
        if len(dicResult) == 0:
            dicResult = {'code':999, 'data':'这是一个无效ID','bundleId':bundId}

        return JSONResponse(dicResult)

def testWebView(request):
    web = open('/Users/zzg/PycharmProjects/zzgSystem/templates/secondPage.html')
    t = Template(web.read())
    web.close()
    # c = Context({"person_name": "zzg"})
    c = Context({"": ""})
    html = t.render(c)
    return HttpResponse(html)

def testindex01(request):
    web = open('/Users/zzg/PycharmProjects/zzgSystem/templates/index01.html')
    t = Template(web.read())
    web.close()
    # c = Context({"person_name": "zzg"})
    c = Context({"": ""})
    html = t.render(c)
    return HttpResponse(html)

def testindex02(request):
    web = open('/Users/zzg/PycharmProjects/zzgSystem/templates/index02.html')
    t = Template(web.read())
    web.close()
    c = Context({"": ""})
    html = t.render(c)
    return HttpResponse(html)

def testcanvas(request):
    web = open('/Users/zzg/PycharmProjects/zzgSystem/templates/canvas.html')
    t = Template(web.read())
    web.close()
    c = Context({"": ""})
    html = t.render(c)
    return HttpResponse(html)


