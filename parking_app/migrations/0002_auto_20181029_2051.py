# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-29 23:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='color',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='car',
            name='model',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='own',
            name='address',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='own',
            name='city',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='own',
            name='location',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='own',
            name='slack',
            field=models.CharField(default='', max_length=150),
        ),
    ]
