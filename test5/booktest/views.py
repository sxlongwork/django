from django.shortcuts import render
from django.template import loader,RequestContext
from django.http import  HttpResponse

# Create your views here.


def index(request):

    # # 加载模板文件，获取一个模板对象
    # tem = loader.get_template('booktest/index.html')
    # # 定义模板上下文，就是给模板传递参数
    # context = RequestContext(request, {'name':'xiaoming'})
    # # 渲染模板，产出一个html内容
    # html = tem.render(context)
    # # 返回响应
    # return HttpResponse(html)
    return render(request, 'booktest/index.html', {'name': 'xiaoming'})