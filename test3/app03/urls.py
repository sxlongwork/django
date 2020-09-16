from django.conf.urls import url
from app03.views import *

urlpatterns = [
    url(r'^add/', AddDataView.as_view(), name='add'),
    url(r'^show', ShowDataView.as_view(), name='show'),
    url(r'^update', UpdateView.as_view(), name='update'),
    url(r'^delete', DeleteView.as_view(), name='delete'),
    url(r'^mantoone', ManyToOne.as_view())
]
