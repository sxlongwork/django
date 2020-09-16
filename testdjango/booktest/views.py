from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader,RequestContext
from booktest.models import BookInfo

# Create your views here.


def my_render(request, html_path, context_dict={}):
    """# 将使用模板过程封装"""

    # 1.加载模板文件,返回模板对象
    tem = loader.get_template(html_path)
    # 2.定义模板上下文，传递数据
    context = RequestContext(request, context_dict)
    # 3.模板渲染，产生标准的html内容
    res_html = tem.render(context)
    # 4.返回给浏览器
    return HttpResponse(res_html)


def index(request):
    # 请求处理，与M和T交互
    # ...
    # 返回httpresponse对象
    # return HttpResponse("hello ")

    # # 1.加载模板文件,返回模板对象
    # tem = loader.get_template("booktest/index.html")
    # # 2.定义模板上下文，传递数据
    # context = RequestContext(request, {})
    # # 3.模板渲染，产生标准的html内容
    # res_html = tem.render(context)
    # # 4.返回给浏览器
    # return HttpResponse(res_html)

    # return my_render(request, "booktest/index.html") 该函数功能python已经实现好了，不用自己自定义
    return render(request, "booktest/index.html", {"content":'python变量','list':list(range(0,10))})


def books(request):
    """显示图书信息"""
    books = BookInfo.objects.all()
    return render(request,"booktest/books.html",{'books': books})

def detail(request, bid):
    """显示bid对应的英雄信息"""
    book = BookInfo.objects.get(id=bid)

    heros = book.heroinfo_set.all()
    for hero in heros:
        if hero.sex == 1:
            hero.sex = 'man'
        else:
            hero.sex = 'woman'
    return render(request, "booktest/detail.html", {'book':book, 'heros':heros})


