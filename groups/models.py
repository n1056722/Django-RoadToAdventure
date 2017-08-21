# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from users.models import *
# Create your models here.
"""
class Group(models.Model):
    GroupID = models.IntegerField(primary_key=True)
    GroupName = models.CharField(max_length=50)
    GroupPicture = models.TextField()
    CreateUser = models.ForeignKey(UserAccount, related_name='Group_CreateUser')
    CreateDate = models.DateTimeField()
    ModifyUser = models.ForeignKey(UserAccount, related_name='Group_ModifyUser')
    ModifyDate = models.DateTimeField()

    def __str__(self):
        return self.GroupName

class GroupRole(models.Model):
    GroupRoleID = models.CharField(primary_key=True,max_length=20)
    GroupRoleName = models.CharField(primary_key=True,max_length=50)

    def __str__(self):
        return self.GroupRoleName

class UserInGroup(models.Model):
    User = models.ForeignKey(UserAccount,primary_key=True,on_delete=models.PROTECT,max_length=20)
    Group = models.ForeignKey(Group,primary_key=True,on_delete=models.PROTECT,max_length=20)
    GroupRole = models.ForeignKey(GroupRole,primary_key=True,on_delete=models.PROTECT,max_length=20)

    def __str__(self):
        return self.GroupRole

class GroupChat(models.Model):
    GroupChat = models.IntegerField(primary_key=True)
    Group = models.ForeignKey(Group,primary_key=True,on_delete=models.PROTECT)
    User = models.ForeignKey(UserAccount,primary_key=True,on_delete=models.PROTECT,max_length=20)
    Content = models.TextField
    CreateDate = models.DateTimeField()

    def __str__(self):
        return self.Content
"""
