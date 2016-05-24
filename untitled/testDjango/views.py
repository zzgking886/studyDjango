from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from testDjango.models import Book
from testDjango.serializers import BookSerializers
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
class JSONResponse(HttpResponse):
    def __init__(self,data,**kwagrs):
        content = JSONRenderer().render(data)
        super(JSONResponse,self).__init__(content,**kwagrs)


def book_list(request,num):
    if request.method == 'GET':
        b = Book.objects.all()
        ser = BookSerializers(b,many=True)
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