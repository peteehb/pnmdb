# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pnmdb', '0003_auto_20151220_0041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='position',
            field=models.CharField(max_length=64, choices=[(b'Goalkeeper', b'Goalkeeper'), (b'Defender', b'Defender'), (b'Midfielder', b'Midfielder'), (b'Forward', b'Forward')]),
        ),
    ]
