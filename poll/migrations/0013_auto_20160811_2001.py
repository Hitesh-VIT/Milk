# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0012_auto_20160811_1938'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='miss',
            name='user',
        ),
        migrations.AddField(
            model_name='miss',
            name='username',
            field=models.CharField(default=0, max_length=250),
        ),
        migrations.AlterField(
            model_name='missed',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
