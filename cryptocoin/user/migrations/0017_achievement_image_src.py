# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-16 23:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0016_achievement'),
    ]

    operations = [
        migrations.AddField(
            model_name='achievement',
            name='image_src',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
