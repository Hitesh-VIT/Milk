# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0003_auto_20160808_1109'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='milk',
            field=models.IntegerField(default=0),
        ),
    ]
