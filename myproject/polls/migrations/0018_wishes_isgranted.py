# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-22 18:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0017_auto_20170122_2319'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishes',
            name='isgranted',
            field=models.BooleanField(default=False),
        ),
    ]
