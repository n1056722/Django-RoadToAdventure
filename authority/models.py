# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
"""
class Authority(models.Model):
    AuthorityID = models.CharField(primary_key=True,max_length=20)
    AuthorityName = models.CharField(max_length=50)
    Memo = models.CharField(max_length=50)

    def __str__(self):
        return self.AuthorityName

class UserRole(models.Model):
    UserRoleID = models.AutoField(primary_key=True)
    UserRoleName = models.CharField(max_length=50)

    def __str__(self):
        return self.UserRoleName

class UserRoleDefaultAuthority(models.Model):
    Authority = models.ForeignKey(Authority, primary_key=True, on_delete=models.PROTECT, related_name='UserAccount_UserRole')
    UserRole = models.ForeignKey(UserRole, primary_key=True, on_delete=models.PROTECT, related_name='UserAccount_UserRole')

    def __str__(self):
        return self.Authority


class GroupRoleDefaultAuthority(models.Model):
    Authority = models.ForeignKey(Authority,on_delete=models.PROTECT,primary_key=True,max_length=20)
    GroupRole = models.ForeignKey(UserRole,on_delete=models.PROTECT,primary_key=True,max_length=20)

    def __str__(self):
        return self.Authority

 class GroupRolePersonalAuthority(models.Model):
     Authority = models.ForeignKey(Authority,on_delete=models.PROTECT,primary_key=True,max_length=20)
     Group = models.ForeignKey(Group,primary_key=True,on_delete=models.PROTECT)
     User = models.ForeignKey(UserAccount,primary_key=True,on_delete=models.PROTECT,max_length=20)

     def __str__(self):
         return self.User
"""
