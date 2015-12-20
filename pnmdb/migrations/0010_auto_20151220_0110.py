# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pnmdb', '0009_remove_player_club'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='team',
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ManyToManyField(related_name='players', to='pnmdb.Team'),
        ),
    ]
