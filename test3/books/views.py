from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader,RequestContext  #模板 loader
from django.db import models
from books.models import bookInfo, HeroInfo, fengying, Fengjsonobj
import json
from django.core import serializers
from django.forms.models import model_to_dict

#1.
#http://127.0.0.1:8000/indexm

def my_render(request, template_path, context_dict={}):

   #1.加载模板文件，模板
    temp = loader.get_template(template_path)
   #2 定义模板上下文：给模板传递数据

    context = RequestContext(request,context_dict)
   #3.模板渲染：产生标准的HTML内容
    reshtml = temp.render(context)
   #4返回给浏览器
    return HttpResponse(reshtml)

def index(request):
    #进行处理。M和T进行交互
   # return HttpResponse('hello')

   #使用模板文件
   #1.加载模板文件，模板
   # temp = loader.get_template('books/index.html')
   #2 定义模板上下文：给模板传递数据
   # context = RequestContext(request,{})
   #3.模板渲染：产生标准的HTML内容
   # reshtml = temp.render(context)
   #4返回给浏览器
   # return HttpResponse(reshtml)
   #return my_render(request,'books/index.html')
   return render(request,'books/index.html',{'content':'hello word','list':list(range(1,10))})

def  show_books(reuest):

    #显示图书信息
    #1通过M查找图
    books = bookInfo.objects.all()


    booklist = []

    for book in books:
        booklist.append(book.btitle)

    return render(reuest,'books/show_books.html',{'booklist':json.dumps(booklist)})


def feng123(reuest):
    # 显示图书信息
    # 1通过M查找图
  #  feng = fengying.objects.all()

    feng = fengying.objects.get(id = 1)

    serialized_obj = serializers.serialize('json', [feng, ])

    return HttpResponse(json.dumps(serialized_obj),content_type="application/json")


def detail(request, bid):
    '''查找英雄类关联的信息'''
    # 根据 bid查找图书信息

    book = bookInfo.objects.get(id=bid)
    heros = book.heroinfo_set.all()
    return render(request,'books/detail.html',{'book':book,'heros':heros})


#http://127.0.0.1:8000/index2
def index2(requdst):
    return  HttpResponse('hello python')
