# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-09 23:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0024_auto_20170709_1734'),
    ]

    operations = [
        migrations.AddField(
            model_name='code',
            name='infinite',
            field=models.BooleanField(default=False),
        ),
    ]
