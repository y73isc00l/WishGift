# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-01 11:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0018_wishes_isgranted'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poolname', models.CharField(max_length=64)),
                ('recipient', models.CharField(max_length=64)),
                ('occassion', models.CharField(max_length=64, null=True)),
                ('occassion_date', models.DateField(null=True)),
                ('minamt', models.IntegerField()),
                ('maxamt', models.IntegerField()),
                ('giftopt01', models.CharField(default='To Be Decided', max_length=100)),
                ('giftopt02', models.CharField(default='To Be Decided', max_length=100)),
                ('giftopt03', models.CharField(default='To Be Decided', max_length=100)),
            ],
        ),
    ]
