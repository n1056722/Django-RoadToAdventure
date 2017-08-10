# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from authority.models import *

# Create your models here.
class UserAccount(models.Model):
    UserID = models.CharField(primary_key=True,max_length=20)
    UserName = models.CharField(max_length=50)
    #UserPicture = models.CharField(max_length=300,default="")
    #UserRole = models.ForeignKey(UserRole,on_delete=models.PROTECT, related_name='UserAccount_UserRole')
    EMail = models.CharField(max_length=200,unique=True)
    Password = models.CharField(max_length=50)
    #LastPassword = models.CharField(max_length=50)
    #LastLoginTime = models.DateTimeField()
    #IsEnabled = models.CharField(max_length=1)
    #IsVerification = models.CharField(max_length=1)

    def __str__(self):
        return self.UserName

class Chat(models.Model):
    ChatID = models.AutoField(primary_key=True)
    CreateUser = models.ForeignKey(UserAccount,on_delete=models.PROTECT, related_name='Chat_CreateUser')
    FriendUser = models.ForeignKey(UserAccount,on_delete=models.PROTECT, related_name='Chat_FriendUser')
    Content = models.TextField()
    CreateDate = models.DateTimeField()

    def __str__(self):
        return self.CreateUser.UserName + '-' + self.FriendUser.UserName +'-'+ self.Content

class UserFriend(models.Model):
    UserFriendID = models.AutoField(primary_key=True)
    CreateUser = models.ForeignKey(UserAccount, on_delete=models.PROTECT, related_name='UserFriend_CreateUser')
    FriendUser = models.ForeignKey(UserAccount, on_delete=models.PROTECT, related_name='UserFriend_FriendUser')
    CreateDate = models.DateTimeField()

    def __str__(self):
        return self.CreateUser.UserName + '-' + self.FriendUser.UserName
        
