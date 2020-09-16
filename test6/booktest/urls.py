from django.conf.urls import url
from booktest import views

urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^login/', views.login, name='login'),
    url(r'register/', views.Register.as_view(), name='register')

]
