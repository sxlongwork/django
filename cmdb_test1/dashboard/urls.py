from django.conf.urls import url
from dashboard.views import *


urlpatterns = [
    url(r'^index/', BaseView.as_view(), name='index'),
    url(r'^$', LoginView.as_view(), name='login'),
    url(r'^logout', LogoutView.as_view(), name='logout')
]
