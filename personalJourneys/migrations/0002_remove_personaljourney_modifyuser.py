# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-21 03:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personalJourneys', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personaljourney',
            name='ModifyUser',
        ),
    ]
