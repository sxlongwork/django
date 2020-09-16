# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=20)),
                ('pub_date', models.DateField()),
                ('read', models.IntegerField(default=0)),
                ('comment', models.IntegerField(default=0)),
                ('is_delete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='HeroInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=20)),
                ('sex', models.BooleanField(default=False)),
                ('comment', models.CharField(max_length=50)),
                ('book', models.ForeignKey(to='booktest.BookInfo')),
            ],
        ),
    ]
