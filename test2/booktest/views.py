from django.shortcuts import render, redirect
from django.http import JsonResponse

# Create your views here.


def index(request):
    """首页文件"""
    return render(request, 'booktest/index.html')


def login(request):
    """登录页面"""
    return render(request, 'booktest/login.html')


def login_check(request):
    """登录检查"""
    # 1.获取登录参数
    username = request.POST.get('username')
    password = request.POST.get('password')
    print(username, password,sep=':')
    # 2.校验登录参数
    if username == 'admin' and password == '123':
        return redirect('/index')
    else:
        return redirect('/login')


def test_ajax(request):
    return render(request, 'booktest/test_ajax.html')


def ajax_check(request):
    return JsonResponse({'res': 'success'})


def login_ajax(request):
    if request.session.has_key('is_login'):
        return redirect('/index')
    else:
        if 'username' in request.COOKIES:
            username = request.COOKIES.get('username')
        else:
            username = ''
        return render(request, 'booktest/login_ajax.html', {'username': username})


def login_check_ajax(request):
    # 获取ajax请求参数
    username = request.POST.get('username')
    password = request.POST.get('password')
    remember = request.POST.get('remember')
    print(remember)

    # 校验用户名和密码
    if username == 'admin' and password == '123':
        response = JsonResponse({'res': 1})
        if remember == "on":
            response.set_cookie('username', username, max_age=7*24*3600)
        request.session['is_login'] = True
        return response
    else:
        return JsonResponse({'res': 0})

