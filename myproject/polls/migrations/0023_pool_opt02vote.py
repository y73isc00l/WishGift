# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-04 07:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0022_auto_20170204_1320'),
    ]

    operations = [
        migrations.AddField(
            model_name='pool',
            name='opt02vote',
            field=models.IntegerField(null=True),
        ),
    ]
