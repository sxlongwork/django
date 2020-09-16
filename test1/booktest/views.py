from django.shortcuts import render,redirect
from booktest.models import BookInfo, HeroInfo
from datetime import date
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.


def index(request):
    books = BookInfo.objects.all()

    return render(request, 'booktest/index.html', {'books': books})


def create(request):
    """创建新的图书"""
    # book = BookInfo()
    # book.name = "花千骨"
    # book.pub_date = date(1992, 10, 20)
    # book.read = 300
    # book.comment = 200
    # book.save()
    # return HttpResponse("ok")

    ## 重定向，不返回页面，而是让浏览器继续访问其他页面，http://127.0.0.1:8000/book
    # return HttpResponseRedirect('/book')
    # return  redirect('/book') # 效果与上面一句相同
    return render(request, 'booktest/addbook.html')


def delete(request, bid):
    """删除指定id的图书"""
    # 获取对应id的图书
    book = BookInfo.objects.get(id=bid)
    # 删除图书
    book.delete()
    # return HttpResponseRedirect('/book')
    return redirect('/book')


def addbook(request):
    book = BookInfo()
    book.name = request.POST.get('name', None)
    book.pub_date = request.POST.get('pub_date', None)
    # print(request.POST['pub_date'])
    book.read = int(request.POST.get('read', None))
    book.comment = int(request.POST.get('comment', None))
    book.save()
    return redirect('/book')





