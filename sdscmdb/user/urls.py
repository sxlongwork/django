from django.conf.urls import url
from user.views import *

urlpatterns = [
    url(r'^userlist/', UserListView.as_view(), name='userlist'),
    # url(r'^addusers/', AddUsersView.as_view()),
    url(r'^useradd/', UserAddView.as_view(), name='useradd'),
    url(r'^userdelete', UserDeleteView.as_view(), name='userdelete'),
    url(r'^userupdate', UserUpdateView.as_view(), name='userupdate'),
    url(r'^userstatus', UserStatusView.as_view(), name='userstatus'),

    url(r'^grouplist/', GroupListView.as_view(), name='grouplist'),
    url(r'^groupadd/', GroupAddView.as_view(), name='groupadd'),
    url(r'^groupdelete', GroupDeleteView.as_view(), name='groupdelete'),
    url(r'^groupupdate', GroupUpdateView.as_view(), name='groupupdate'),
]
