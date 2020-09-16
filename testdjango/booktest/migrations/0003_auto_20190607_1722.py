# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0002_herinfo'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HerInfo',
            new_name='HeroInfo',
        ),
    ]
