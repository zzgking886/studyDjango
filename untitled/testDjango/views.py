from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from testDjango.models import Book
from testDjango.models import User
from testDjango.serializers import BookSerializers
from testDjango.serializers import UserSerializers
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
# return json data page

class JSONResponse(HttpResponse):
    def __init__(self,data,**kwagrs):
        content = JSONRenderer().render(data)
        super(JSONResponse,self).__init__(content,**kwagrs)


def book_list(request,num):
    if request.method == 'GET':
        b = Book.objects.all()
        ser = BookSerializers(b,many = True)
        return JSONResponse(ser.data)
    elif request.method == 'POST':
        print 'hello, world'
        classmates = ['Michael', 'Bob', 'Tracy']
        s = json.dumps(classmates)
        return classmates


@csrf_exempt
def post_book_list(request):
    print 'hello, world'
    classmates = ['Michael', 'Bob', 'Tracy']
    s = json.dumps(classmates)
    return JSONResponse(s)

def user_list(request):
    if request.method == 'GET':
        user = User.objects.all()
        ser = UserSerializers(user,many = True)
        return JSONResponse(ser.data)

def addNum(request):
    if request.method == 'GET':
        a = request.GET['a']
        b = request.GET['b']
        c = int(a) + int(b)
        return JSONResponse(c)

@csrf_exempt
def postAddNum(request):
    if request.method == 'POST':
        a = request.POST['a']
        b = request.POST['b']
        c = int(a) + int(b)
        d = 'result = ',c
        return JSONResponse(d)

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

