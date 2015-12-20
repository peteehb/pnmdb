# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pnmdb', '0004_auto_20151220_0042'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='user',
            field=models.OneToOneField(related_name='club', null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='team',
            name='user',
            field=models.ForeignKey(related_name='teams', to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
