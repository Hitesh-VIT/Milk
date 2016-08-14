# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0005_auto_20160808_1854'),
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
    ]
