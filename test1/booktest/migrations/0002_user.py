# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=40)),
                ('sex', models.BooleanField(default=False)),
                ('age', models.IntegerField(null=True, default=None)),
                ('birth', models.DateField(null=True)),
                ('phone', models.CharField(max_length=11, blank=True, null=True)),
                ('comment', models.CharField(max_length=100, blank=True, null=True)),
            ],
        ),
    ]
