# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('pnmdb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='team',
            field=models.ForeignKey(related_name=b'players', to='pnmdb.Team'),
        ),
        migrations.AlterField(
            model_name='player',
            name='user',
            field=models.ForeignKey(related_name=b'players', to=settings.AUTH_USER_MODEL),
        ),
    ]
