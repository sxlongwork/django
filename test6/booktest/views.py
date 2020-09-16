from django.shortcuts import render, HttpResponse
from booktest.models import *
from django.views.generic import View
import hashlib

# Create your views here.
# 创建MD5对象
hl = hashlib.md5()

def index(request):
    return render(request, 'booktest/login.html')


def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    print(username, password)
    # flag = UserInfo.objects.get(username=username)
    if UserInfo.objects.all() is None:
        print('hheh')
    # print(flag)
    # if flag is None:
    #     return HttpResponse("you need register first")
    #
    # hl.update(password.encode(encoding='utf-8'))
    # en_password =hl.hexdigest()
    # if flag.passwd == en_password:
    #     return render(request, 'booktest/hostlist.html')
    # else:
    #     return render(request, 'booktest/login.html',{})
    return HttpResponse('ok')


class Register(View):
    def get(self, request):
        return render(request, 'booktest/register.html')

    def post(self, request):

        user = UserInfo()
        user.username = request.POST.get('username')
        hl.update(request.POST.get('password').encode(encoding='utf-8'))
        user.password = hl.hexdigest()
        user.sex = int(request.POST.get('sex'))
        user.birth = request.POST.get('birth')
        user.save()
        return render(request, 'booktest/register_success.html',{'message': 'register success'})


