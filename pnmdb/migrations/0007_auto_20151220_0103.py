# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pnmdb', '0006_auto_20151220_0101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='club',
            field=models.ForeignKey(related_name='members', to='pnmdb.Club', null=True),
        ),
    ]
