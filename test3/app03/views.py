from django.shortcuts import render, HttpResponse
from django.views import View
from app03.models import *


# Create your views here.

class AddDataView(View):
    def get(self, request):
        # 方法一
        # host = Host(hostname='server01', ip='10.0.0.1', type='1', status='1')
        # host.save()
        # 方法二
        # host = Host()
        # host.hostname = 'server02'
        # host.ip = '10.0.0.2'
        # host.type = 2
        # host.status = 0
        # host.save()
        # 方法三
        # Host.objects.create(hostname='server03', ip='10.0.0.3', type='3', status='1')
        # 方法四
        data = {'hostname': 'server04', 'ip': '10.0.0.4', 'type': 1, 'status': 1}
        Host.objects.create(**data)

        return HttpResponse("add success")


class ShowDataView(View):
    def get(self, request):
        # all()方法返回所有数据
        # data = Host.objects.all()
        # print(data)
        # for one in data:
        #     print(one.hostname, one.ip, one.type, one.status)

        # get()方法只返回一条数据，有多条数据时报错
        # data = Host.objects.get(id = 1)
        # print(data.hostname, data.ip, data.type, data.status)

        # filter()方法可以返回一条、多条或0条数据，结果都是一个查询集，需要遍历才能访问到数据
        # data = Host.objects.filter()
        # for one in data:
        #     print(one.hostname, one.ip, one.type, one.status)

        # 查询不满足条件的数据，返回是一个结果集
        # data = Host.objects.exclude(status='1')
        # for one in data:
        #     print(one.hostname, one.ip, one.type, one.status)

        # data = Host.objects.values('hostname', 'ip')
        # for one in data:
        #     for k, v in one.items():
        #         print(k, v)

        # 内置查询字段
        # data = Host.objects.filter(id__gt=2)      # id>2
        # data = Host.objects.filter(id__lte=2)  # id<=2
        # data = Host.objects.filter(hostname__startswith='server')
        # data = Host.objects.filter(id__range=(1, 2))
        data = Host.objects.filter(id__in=[2, 3])
        for one in data:
            print(one.hostname, one.ip, one.type, one.status)
        return HttpResponse("show success")


class UpdateView(View):
    def get(self, request):
        # 根据对象属性更新数据,只能更新一条
        # host =  Host.objects.get(hostname='server04')
        # host.status = 0
        # host.save()

        # 一次性更新多条数据，推荐使用
        # Host.objects.filter(status=1).update(status=0)
        return HttpResponse('update success')


class DeleteView(View):
    def get(self, request):
        # delete方法删除一条或多条
        # Host.objects.get(id=4).delete()
        return HttpResponse('delete success')


class ManyToOne(View):
    def get(self, request):
        # Publish.objects.create(name='清华大学出版社', address='北京')
        # Publish.objects.create(name='东北大学出版社', address='沈阳')
        # Publish.objects.create(name='东北财经大学出版社', address='大连')

        # Book.objects.create(name='java进阶',price=80.22, publish=Publish.objects.get(name='清华大学出版社'))
        # Book.objects.create(name='python进阶',price=30.24, publish=Publish.objects.get(name='东北大学出版社'))
        # Book.objects.create(name='shell高级编程', price=20.11, publish=Publish.objects.get(name='清华大学出版社'))
        # Book.objects.create(name='python自动化运维', price=60.55, publish=Publish.objects.get(name='东北大学出版社'))
        # Author.objects.create(name='tom', job='devops')
        book = Book.objects.get(name='python自动化运维')
        author = Author.objects.get(name='tom')
        book.author.add(author)


        # 正向查询，查询图书所在的出版社
        # data = Book.objects.get(name='python进阶').publish.name
        # data = Book.objects.all()
        # for one in data:
        #     print(one.publish.name)

        # 反向查询，某个出版社对应的图书有哪些(可能多个，get方法就不能用了)
        # data = Book.objects.filter(publish=Publish.objects.get(name='清华大学出版社'))
        # data = Publish.objects.get(name='清华大学出版社').book_set.all()
        # for one in data:
        #     print(one.name)

        # 删除，django默认的外键级联删除方式，当删除出版社时，出版社下对应的图书也会被删除
        # Publish.objects.get(name='清华大学出版社').delete()

        return HttpResponse('many to one')
