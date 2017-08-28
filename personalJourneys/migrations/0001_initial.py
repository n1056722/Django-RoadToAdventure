# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-22 03:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalJourney',
            fields=[
                ('PersonalJourneyID', models.AutoField(primary_key=True, serialize=False)),
                ('PersonalJourneyName', models.CharField(max_length=50)),
                ('PersonalJourneyContent', models.TextField()),
                ('Points', models.TextField()),
                ('Status', models.CharField(max_length=1)),
                ('IsOpen', models.CharField(max_length=1)),
                ('StartTime', models.DateTimeField()),
                ('EndTime', models.DateTimeField()),
                ('CreateDate', models.DateTimeField()),
                ('ModifyDate', models.DateTimeField()),
                ('CreateUser', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='PersonalJourney_CreateUser', to='users.UserAccount')),
            ],
        ),
        migrations.CreateModel(
            name='PersonalJourneyComment',
            fields=[
                ('PersonalJourneyCommentID', models.AutoField(primary_key=True, serialize=False)),
                ('Comment', models.TextField()),
                ('CreateDate', models.DateTimeField()),
                ('CreateUser', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='PersonalJourneyComment_CreateUser', to='users.UserAccount')),
                ('PersonalJourney', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='PersonalJourneyComment_personalJourney', to='personalJourneys.PersonalJourney')),
            ],
        ),
        migrations.CreateModel(
            name='PersonalJourneyDetail',
            fields=[
                ('PersonalJourneyDetailID', models.AutoField(primary_key=True, serialize=False)),
                ('Latitude', models.CharField(max_length=30)),
                ('Longitude', models.CharField(max_length=30)),
                ('CreateDate', models.DateTimeField()),
                ('PersonalJourney', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='PersonalJourneyDetail_personalJourney', to='personalJourneys.PersonalJourney')),
            ],
        ),
    ]
