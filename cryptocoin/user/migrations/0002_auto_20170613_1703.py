# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-13 22:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='honory_coins',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='userdata',
            name='password',
            field=models.CharField(default='hahaha', max_length=100),
        ),
        migrations.AddField(
            model_name='userdata',
            name='permanent_coins',
            field=models.IntegerField(default=0),
        ),
    ]
