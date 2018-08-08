from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from zzgSystemServer.models import UserTable
from zzgSystemServer.models import VRVideoTable
from zzgSystemServer.serializers import UserTableSerializers
from zzgSystemServer.serializers import VRVideoSerializers
from django.views.decorators.csrf import csrf_exempt
# from django.core.context_processors import csrf
from django.template.context_processors import csrf
from django.conf import settings
from django.core.cache import cache
from django.views.decorators.cache import cache_page
import json
from django.template import Template, Context
import socket
from django.http.response import StreamingHttpResponse
import scrapy
import urllib.request
import http, time

from django.contrib.auth import authenticate
from django.views.generic.base import View

# Create your views here.
# _pageTemplates = ''
# if socket.gethostname() == 'iZ2ze7xv8tix4ws606m907Z':
#     _pageTemplates = '/root/myfirstproject/zzgSystem/templates/'
# else:
#     _pageTemplates = '/Users/zzg/PycharmProjects/zzgSystem/templates/'

_pageTemplates = '/Users/zzg/PycharmProjects/zzgSystem/templates/'
resoursePath = '/Users/zzg/PycharmProjects/zzgSystem/static/htmlImg'


class JSONResponse(HttpResponse):
    def __init__(self, data, **kwagrs):
        content = JSONRenderer().render(data)
        super(JSONResponse, self).__init__(content, **kwagrs)


@csrf_exempt  # POST方法
def userLogin(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        pass_word = request.POST.get('password')
        users = authenticate(username='zzgking886', password='wushixia1119')
        if users is not None:
            dicResult = {'code': '200', 'status': 'success'}
            return JSONResponse(dicResult)
        else:
            return JSONResponse({'code': '0', 'status': 'user is not exist'})
    else:
        return JSONResponse({'code': '404', 'status': 'no post'})


class LoginView(View):
    def get(self,request):
        return JSONResponse({'code': '404', 'status': 'no post'})
    def post(self,request):
        user_name = request.POST['username']
        pass_word = request.POST.get('password')
        users = authenticate(username='zzgking886', password='wushixia1119')
        if users is not None:
            dicResult = {'code': '200', 'status': 'success'}
            return JSONResponse(dicResult)
        else:
            return JSONResponse({'code': '0', 'status': 'user is not exist'})


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
        # if cache.get('vrtablelist'):
        #     vrlist = cache.get('vrtablelist')
        #     vrtable = VRVideoSerializers(vrlist, many=True)
        #     dicResult = {'title': 200, 'cache': 'true', 'data': vrtable.data}
        # else:
        checkTitle = request.GET.get('title');
        if checkTitle:
            vrtablelist = VRVideoTable.objects.filter(videoTitle__regex=checkTitle)
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
                dicResult = {'code': 200, 'data': '这是一个有效ID', 'bundleId': bundId}
        if len(dicResult) == 0:
            dicResult = {'code': 999, 'data': '这是一个无效ID', 'bundleId': bundId}

        return JSONResponse(dicResult)


def testWebView(request):
    web = open('/Users/zzg/PycharmProjects/zzgSystem/templates/firstPage.html')
    t = Template(web.read())
    web.close()
    c = Context({"person_name": "zzg","person_sex":"男"})
    # c = Context({"": ""})
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


def testcanvastwo(request):
    web = open('/Users/zzg/PycharmProjects/zzgSystem/templates/canvas02.html')
    t = Template(web.read())
    web.close()
    c = Context({"": ""})
    html = t.render(c)
    return HttpResponse(html)


def testvideoPage(request):
    web = open(_pageTemplates + 'videoPage.html')
    t = Template(web.read())
    web.close()
    c = Context({"": ""})
    html = t.render(c)
    return HttpResponse(html)


def testformCommit(request):
    web = open(_pageTemplates + 'formPage.html')
    t = Template(web.read())
    web.close()
    c = Context({"": ""})
    html = t.render(c)
    return HttpResponse(html)


def testLocalStorege(request):
    web = open(_pageTemplates + 'localStorege.html')
    t = Template(web.read())
    web.close()
    c = Context({"": ""})
    html = t.render(c)
    return HttpResponse(html)


def testReponseDesign(request):
    web = open(_pageTemplates + 'ReponseDesign.html')
    t = Template(web.read())
    web.close()
    c = Context({"": ""})
    html = t.render(c)
    return HttpResponse(html)


def cntvInterFaceCheck(request):
    web = open(_pageTemplates + 'InterFaceCheck.html')
    t = Template(web.read())
    web.close()
    c = Context({"": ""})
    html = t.render(c)
    return HttpResponse(html)


def testLiveReturn(request):
    web = open(_pageTemplates + 'testLiveReturn.html')
    t = Template(web.read())
    web.close()
    c = Context({"": ""})
    html = t.render(c)
    return HttpResponse(html)


def testiosplay(request):
    # do something...
    videopath = resoursePath + "basketball.mp4"
    response = StreamingHttpResponse(videopath, status=200, content_type='video/mpeg4')
    response['Cache-Control'] = 'no-cache'
    return response


def testiosaudioplay(request):
    videopath = resoursePath + "demo.mp3"
    response = StreamingHttpResponse(videopath, status=200, content_type='audio/mp3')
    response['Cache-Control'] = 'no-cache'
    return response


def testInterFaceTime(name, url):
    timestamp = ""
    start = time.time()
    returndata = urllib.request.urlopen(url).read()
    dataobj = json.loads(returndata.decode("utf-8"))
    end = ""
    if len(dataobj) > 0:
        end = time.time()
    else:
        end = "time out"

    if end == "time out":
        timestamp = "time out"
    else:
        timestamp = ('Task runs %0.2f seconds.' % (end - start))

    return [name, url, timestamp]


def checkInterface(request):
    configtest = testInterFaceTime('主配置', 'http://serv.cbox.cntv.cn/json/cbox6/yidongzhupeizhi/index.json')
    return JSONResponse(configtest)
    # http://serv.cbox.cntv.cn/json/cbox6/yidongzhupeizhi/index.json

    # http://127.0.0.1:8000/static/htmlImg/outfit_f/384.png

def checkPublic(request):
    starttime = 1528967758
    url = "http://vdn.live.cntv.cn/api2/liveTimeshift.do?channel=pa://cctv_p2p_hdcctv5&client=iosapp&starttime="
    number = 1000
    dataobj = ""
    while number <= 1000000:
        finalurl = url + str(starttime)
        print(finalurl)
        returndata = urllib.request.urlopen(finalurl).read()
        dataobj = json.loads(returndata.decode("utf-8"))
        return JSONResponse(dataobj)

