from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.views.generic import View, TemplateView
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class BaseView(LoginRequiredMixin,TemplateView):
    template_name = 'index.html'


class LoginView(TemplateView, View):
    template_name = 'login.html'

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            res = {'status': 0, 'msg': 'login success'}
        else:
            res = {'status': 1, 'msg': 'username or password is wrong'}
        return JsonResponse(res)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('login'))