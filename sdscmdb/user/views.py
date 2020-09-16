from django.shortcuts import render, HttpResponse
from django.views.generic import View, TemplateView, ListView
from django.contrib.auth.models import User, Group, Permission
from user.models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.hashers import make_password
from django.http.response import JsonResponse


# Create your views here.

# class UserListView(TemplateView):
#     template_name = 'user_list.html'
#
#     def get_context_data(self, **kwargs):
#         context = super(UserListView, self).get_context_data(**kwargs)
#         context['userlist'] = User.objects.all()
#         return context


class UserListView(LoginRequiredMixin, ListView):
    template_name = 'user_list.html'
    model = User  # 使用ListView定义模型model名称，数据会自动查询并且组合，前端使用object_List可以遍历所有model对象
    ordering = 'id'

    # def get_context_data(self, **kwargs):
    #     context = super(UserListView, self).get_context_data(**kwargs)
    #     context['userlist'] = User.objects.all()
    #     return context

    # def get_context_data(self, **kwargs):
    #     page = int(self.request.GET.get('page'))
    #     start = (page-1)*8
    #     end = start + 8
    #     context = super(UserListView, self).get_context_data(**kwargs)
    #     context['object_list'] = User.objects.all()[start:end]
    #     return context
    paginate_by = 7


class AddUsersView(View):
    def get(self, request):
        for i in range(1, 100):
            user = User()
            profile = Prifile()
            user.username = 'develop{}'.format(i)
            user.password = '123456'
            user.email = 'develop{}.@163.com'.format(i)
            user.save()
            profile.name_cn = '开发{}'.format(i)
            profile.wechat = 'vxid_1000{}'.format(i)
            profile.phone = '18709871001'
            profile.profile_id = user.id
            profile.save()
        return HttpResponse('测试数据添加成功')


class UserAddView(TemplateView):
    template_name = 'user_add.html'

    def post(self, request):
        user = User()
        profile = Prifile()
        data = request.POST
        try:
            user.username = data.get('username')
            user.password = make_password(data.get('password'))
            user.email = data.get('email')
            user.save()
            profile.name_cn = data.get('name_cn')
            profile.wechat = data.get('wechat')
            profile.phone = data.get('phone')
            profile.profile_id = user.id
            profile.save()
        except Exception:
            res = {'status': 1, 'msg': '添加用户失败'}
        else:
            res = {'status': 0, 'msg': '添加用户成功'}
        return JsonResponse(res)


class UserUpdateView(ListView):
    template_name = 'user_update.html'
    model = User

    def get_context_data(self, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        id = self.request.GET.get('id')
        context['user_obj'] = User.objects.get(id=id)
        return context

    def post(self, request):
        data = request.POST
        res = {'status': 0, 'msg': '更新用户成功'}
        try:
            user = User.objects.get(id=data.get('id'))
            user.username = data.get('username')
            user.password = make_password(data.get('password'))
            user.email = data.get('email')
            user.save()
            profile = Prifile.objects.get(profile_id=data.get('id'))
            profile.phone = data.get('phone')
            profile.wechat = data.get('wechat')
            profile.name_cn = data.get('name_cn')
            profile.save()
        except Exception as e:
            print(e)
            res = {'status': 1, 'msg': '更新用户失败'}
        return JsonResponse(res)


class UserDeleteView(View):
    def get(self, request):
        try:
            id = request.GET.get('id')
            print(id)
            User.objects.get(id=id).delete()
        except Exception as e:
            res = {'status': 1, 'msg': '删除用户失败'}
        else:
            res = {'status': 0, 'msg': '删除用户成功'}
        return JsonResponse(res)


class UserStatusView(View):
    def get(self, request):
        try:
            user = User.objects.get(id=request.GET.get('id'))
            if user.is_active:
                user.is_active = 0
                res = {'status': 0, 'msg': '禁用用户成功'}
            else:
                user.is_active = 1
                res = {'status': 0, 'msg': '启用用户成功'}
            user.save()
        except Exception as e:
            res = {'status': 1, 'msg': '用户状态更新失败'}
        return JsonResponse(res)


class GroupListView(ListView):
    template_name = 'group_list.html'
    model = Group
    ordering = 'id'
    paginate_by = 7


class GroupAddView(ListView):
    template_name = 'group_add.html'
    model = User

    def post(self, request):
        group = Group()
        res = {'status': 0, 'msg': '添加用户组成功'}
        try:
            group.name = request.POST.get('name')
            group.save()
            for id in request.POST.getlist('group_user'):
                group.user_set.add(User.objects.get(id=id))
        except Exception as e:
            res = {'status': 1, 'msg': '添加用户组失败'}
        return JsonResponse(res)


class GroupDeleteView(View):
    def get(self, request):
        group = Group.objects.get(id=request.GET.get('id'))
        if len(group.user_set.all()) == 0:
            group.delete()
            res = {'status': 0, 'msg': '删除用户组成功'}
        else:
            res = {'status': 1, 'msg': '该用户组下有用户，请先删除该组下的用户再删除该组'}
        return JsonResponse(res)


class GroupUpdateView(TemplateView):
    template_name = 'group_update.html'

    def get_context_data(self, **kwargs):
        context = super(GroupUpdateView, self).get_context_data(**kwargs)
        context['group_obj'] = Group.objects.get(id=self.request.GET.get('id'))
        context['user_list'] = User.objects.all()
        return context

    def post(self, request):
        res = {'status': 0, 'msg': '更新用户组成功'}
        try:
            group = Group.objects.get(id=request.POST.get('id'))
            group.name = request.POST.get('name')
            group.save()
            group.user_set.clear()
            for id in request.POST.getlist('group_user'):
                group.user_set.add(User.objects.get(id=id))
        except Exception as e:
            print(e)
            res = {'status': 1, 'msg': '更新用户组失败'}
        return JsonResponse(res)
