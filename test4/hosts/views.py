from django.shortcuts import render,HttpResponse
from django.views.generic import View
from datetime import date

# Create your views here.


class MyView(View):
    """test class view"""
    def get(self, request):
        return HttpResponse("get method")

    def post(self, request):
        return HttpResponse('post method')


class MyLogin(View):
    def get(self, request):
        return render(request, 'login.html')
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == "admin" and password == "123":
            return HttpResponse("Loin success")
        else:
            return HttpResponse("username or password is wrong")


class Template(View):
    def get(self, request):
        # name = 'xianqian'
        age = 13
        sex ='girl'
        habby = 'long'
        list = ["one", "two"]
        dict = {"book": "python 进阶", "view": "三生三世"}
        date_time = date.today()

        # return render(request, 'tem.html', {'name': name, 'age': age, 'sex': sex})
        return render(request, 'tem.html', locals())    # locals()方法可以传输所有变量
