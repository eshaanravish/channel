# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-06 14:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mychannel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='created_at',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
