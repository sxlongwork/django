# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-04 13:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app03', '0003_auto_20190804_2033'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='作者名字')),
                ('job', models.CharField(max_length=20, verbose_name='作者职业')),
            ],
            options={
                'verbose_name': '作者信息',
                'db_table': 'author',
            },
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(to='app03.Author'),
        ),
    ]