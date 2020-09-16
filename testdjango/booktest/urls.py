from django.conf.urls import url
from booktest import views

# 自定义url路由，哪个url应该调用哪个视图处理
urlpatterns = [
    url(r'^$', views.index),
    url(r'^index$', views.index),
    url(r'^books$', views.books),
    url(r'books/(\d+)$', views.detail),
]
