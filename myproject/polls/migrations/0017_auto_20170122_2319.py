# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-22 17:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0016_auto_20170122_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='friend',
            unique_together=set([('email', 'user')]),
        ),
    ]
