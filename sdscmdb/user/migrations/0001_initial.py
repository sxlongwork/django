# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-06 17:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Prifile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_cn', models.CharField(max_length=20, verbose_name='中文名')),
                ('wechat', models.CharField(max_length=30, verbose_name='微信号')),
                ('phone', models.CharField(max_length=11, verbose_name='手机号码')),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
