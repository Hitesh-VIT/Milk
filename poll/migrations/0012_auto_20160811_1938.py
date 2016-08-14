# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('poll', '0011_remove_miss_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='miss',
            name='user',
        ),
        migrations.AddField(
            model_name='miss',
            name='user',
            field=models.ManyToManyField(default=0, to=settings.AUTH_USER_MODEL),
        ),
    ]
