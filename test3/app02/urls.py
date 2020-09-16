from django.conf.urls import url
from app02.views import *

urlpatterns = [
    # url(r'^login/', views.login, name='login'),
    url(r'^login/', MyView.as_view(), name='login'),
    url(r'^hostinfo/', HostInfo.as_view(), name='hostinfo'),
    url(r'^tem/', TemView.as_view(), name='tem')

]
