from django.conf.urls import url
from dashboard.views import *

urlpatterns = [
    url(r'^base/', BaseView.as_view(), name='base'),
    url(r'^$', IndexView.as_view(), name='index'),
]
