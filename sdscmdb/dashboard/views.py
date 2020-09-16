from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class BaseView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'base.html')


# class IndexView(View):
#     def get(self, request):
#         return render(request, 'index.html')


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['name'] = 'index.html'
        return context


class LoginView(TemplateView):
    template_name = 'login.html'

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            res = {'status': 0, 'msg': 'Login success'}
        else:
            res = {'status': 1, 'msg': 'username or password is wrong'}
        return JsonResponse(res)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('login'))
