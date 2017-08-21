# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from users.models import *
# Create your models here.

class Group(models.Model):
    GroupID = models.AutoField(primary_key = True)
    GroupName = models.CharField(max_length = 50)
    GroupPicture = models.CharField(max_length = 100, blank = True)
    CreateUser = models.ForeignKey(UserAccount, on_delete = models.PROTECT, related_name = 'Group_CreateUser')
    CreateDate = models.DateTimeField()
    ModifyUser = models.ForeignKey(UserAccount, on_delete = models.PROTECT, related_name = 'Group_ModifyUser')
    ModifyDate = models.DateTimeField()

    def __str__(self):
        return self.GroupName

class GroupRole(models.Model):
    GroupRoleID = models.CharField(primary_key = True, max_length = 20)
    GroupRoleName = models.CharField(max_length = 50)

    def __str__(self):
        return self.GroupRoleName

class UserInGroup(models.Model):
    UserInGroupID = models.AutoField(primary_key = True)
    User = models.ForeignKey(UserAccount, on_delete = models.PROTECT, related_name = 'UserInGroup_User')
    Group = models.ForeignKey(Group, on_delete = models.PROTECT, related_name = 'UserInGroup_Group')
    GroupRole = models.ForeignKey(GroupRole, on_delete = models.PROTECT, related_name = 'UserInGroup_GroupRole')

    def __str__(self):
        return self.Group.GroupName + '-' + self.User.UserID + '-' + self.GroupRole.GroupRoleName

class GroupChat(models.Model):
    GroupChatID = models.AutoField(primary_key = True)
    Group = models.ForeignKey(Group, on_delete = models.PROTECT, related_name = 'GroupChat_Group')
    User = models.ForeignKey(UserAccount, on_delete = models.PROTECT, related_name = 'GroupChat_User')
    Content = models.CharField(max_length = 50, blank = True)
    CreateDate = models.DateTimeField()

    def __str__(self):
        return self.Group.GroupName + '-' + self.User.UserID + '-' + self.Content

