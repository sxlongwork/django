"""test3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from app01 import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^index/', views.index),
    # url(r'^test_get/', views.test_get),
    # url(r'^test_post/', views.test_post),
    url(r'^ads/', views.ads),
    # url(r'^hostlist', views.hostlist),
    # url(r'^year/(\d{4})/(\d{2})/$', views.testUrl),
    # url(r'^testUrl/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/$', views.testUrl)
    url(r'^app01/', include('app01.urls')),
    url(r'^app02/', include('app02.urls')),
    url(r'^app03/', include('app03.urls')),
]
