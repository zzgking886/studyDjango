__author__ = 'zzg'
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from testDjango.models import Book
from testDjango.models import User
from testDjango.models import UserTable
from testDjango.serializers import BookSerializers
from testDjango.serializers import UserSerializers
from testDjango.serializers import UserTableSerializers
from django.views.decorators.csrf import csrf_exempt
import json

class JSONResponse(HttpResponse):
    def __init__(self,data,**kwagrs):
        content = JSONRenderer().render(data)
        super(JSONResponse,self).__init__(content,**kwagrs)


def secodeUserTableList(request):
    if request.method == 'GET':
        usertablelist = UserTable.objects.all()
        usertable = UserTableSerializers(usertablelist, many=True)
        dicResult = {'code':200,'data':usertable.data}
        return JSONResponse(dicResult)