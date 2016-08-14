# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0002_auto_20160807_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='miss',
            name='date',
            field=models.DateField(),
        ),
    ]
