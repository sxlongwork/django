from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
import paramiko
import psutil

# Create your views here.
def login(request):
    if request.method == 'GET':
        return render(request,'login2.html')
    elif request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'admin' and password == '123':
            return HttpResponse("login success")
        else:
            return HttpResponse('username or password is wrong')


class MyView(View):
    def get(self, request):
        return render(request, 'login2.html')
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'admin' and password == '123':
            return HttpResponse('Login Success')
        else:
            return HttpResponse('username or password is wrong')


class HostInfo(View):
    def get(self, request):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        ssh.connect(hostname='152.136.89.241', port=22, username='root',password='Huawei123_')
        stdin, stdout, dtderr = ssh.exec_command('df -h')

        context = stdout.read()
        print(context.decode())
        print(type(context.decode()))
        ssh.close()
        return HttpResponse('hostinfo')


class TemView(View):
    def get(self, request):
        name = '<h3>tom</h1>'
        list = ['python', 'java', 'golang','shell']
        cpuinfo = psutil.cpu_times()
        dict = {'name': 'xianqian', 'age': 20, 'sex': 'woman'}
        age = 21
        return render(request, 'tem.html', locals())






















