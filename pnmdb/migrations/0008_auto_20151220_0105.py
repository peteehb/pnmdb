# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('pnmdb', '0007_auto_20151220_0103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='user',
            field=models.ForeignKey(related_name='club', to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
