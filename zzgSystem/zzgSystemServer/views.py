from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from zzgSystemServer.models import UserTable
from zzgSystemServer.serializers import UserTableSerializers
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

class JSONResponse(HttpResponse):
    def __init__(self,data,**kwagrs):
        content = JSONRenderer().render(data)
        super(JSONResponse,self).__init__(content,**kwagrs)


@csrf_exempt
def userLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pwd']
        if username == 'zzg' and password == 'wushixia1119':
            dicResult = {'code' : '200', 'status':'success'}
            return  JSONResponse(dicResult)
        else:
            return JSONResponse({'code' : '404', 'status' : 'fail'})

def userTableList(request):
    if request.method == 'GET':
        usertablelist = UserTable.objects.all()
        usertable = UserTableSerializers(usertablelist, many=True)
        dicResult = {'code':200,'data':usertable.data}
        return JSONResponse(dicResult)