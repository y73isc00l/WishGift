# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-22 16:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0015_auto_20170122_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
    ]