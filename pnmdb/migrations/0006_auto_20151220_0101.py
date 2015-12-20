# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pnmdb', '0005_auto_20151220_0058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='user',
        ),
        migrations.RemoveField(
            model_name='team',
            name='user',
        ),
        migrations.AddField(
            model_name='player',
            name='club',
            field=models.ForeignKey(related_name='players', to='pnmdb.Club', null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='club',
            field=models.ForeignKey(related_name='teams', to='pnmdb.Club', null=True),
        ),
    ]
