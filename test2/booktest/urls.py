from django.conf.urls import url
from booktest import views

urlpatterns = [
    url(r'^index$', views.index),
    url(r'^login$',views.login),
    url(r'^login_check$', views.login_check),

    url(r'^test_ajax$', views.test_ajax),
    url(r'^ajax_check$', views.ajax_check),

    url(r'^login_ajax$', views.login_ajax),
    url(r'^login_check_ajax$', views.login_check_ajax),

]
