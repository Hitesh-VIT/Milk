# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill_milk',
            name='date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='miss',
            name='date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='missed',
            name='date',
            field=models.DateField(blank=True),
        ),
    ]
