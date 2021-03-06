# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-22 03:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('ChatID', models.AutoField(primary_key=True, serialize=False)),
                ('Content', models.TextField()),
                ('CreateDate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('UserID', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('UserName', models.CharField(max_length=50)),
                ('UserPicture', models.CharField(blank=True, max_length=100)),
                ('EMail', models.CharField(max_length=200, unique=True)),
                ('Password', models.CharField(max_length=50)),
                ('CreateDate', models.DateTimeField()),
                ('ModifyDate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='UserFriend',
            fields=[
                ('UserFriendID', models.AutoField(primary_key=True, serialize=False)),
                ('CreateDate', models.DateTimeField()),
                ('CreateUser', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='UserFriend_CreateUser', to='users.UserAccount')),
                ('FriendUser', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='UserFriend_FriendUser', to='users.UserAccount')),
            ],
        ),
        migrations.AddField(
            model_name='chat',
            name='CreateUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Chat_CreateUser', to='users.UserAccount'),
        ),
        migrations.AddField(
            model_name='chat',
            name='FriendUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Chat_FriendUser', to='users.UserAccount'),
        ),
    ]
