# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pnmdb', '0002_auto_20151220_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='position',
            field=models.CharField(max_length=2, choices=[(b'Goalkeeper', b'Goalkeeper'), (b'Defender', b'Defender'), (b'Midfielder', b'Midfielder'), (b'Forward', b'Forward')]),
        ),
    ]
