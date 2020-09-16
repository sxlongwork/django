from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Prifile(models.Model):
    name_cn = models.CharField(max_length=20, verbose_name='中文名')
    wechat = models.CharField(max_length=30, verbose_name='微信号')
    phone = models.CharField(max_length=11, verbose_name='手机号码')
    profile = models.OneToOneField(User)