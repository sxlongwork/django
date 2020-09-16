from django.conf.urls import url
from booktest import views

urlpatterns = [
    url(r'^book$', views.index),
    url(r'^create$', views.create),
    # url(r'^delete/(\d+)$', views.delete),   # 捕获url参数：位置参数
    url(r'^delete/(?P<bid>\d+)$', views.delete), # 捕获url参数：关键字参数，bid必须与delete函数接收参数名称一致
    url(r'^addbook$', views.addbook),
]
