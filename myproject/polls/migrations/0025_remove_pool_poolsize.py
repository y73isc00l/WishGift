# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-04 09:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0024_auto_20170204_1442'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pool',
            name='poolsize',
        ),
    ]