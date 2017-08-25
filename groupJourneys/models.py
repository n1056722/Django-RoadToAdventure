# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from groups.models import *
from users.models import *
# Create your models here.

class GroupJourney(models.Model):
    GroupJourneyID = models.IntegerField(primary_key=True)
    Group = models.ForeignKey(Group,primary_key=True,on_delete=models.PROTECT)
    GroupJourneyName = models.CharField(max_length=50)
    GroupJourneyContent = models.TextField()
    CreateUser = models.ForeignKey(UserAccount, related_name='GroupJourney_CreateUser')
    CreateDate = models.DateTimeField()
    ModifyUser = models.ForeignKey(UserAccount, related_name='GroupJourney_ModifyUser')
    ModifyDate = models.DateTimeField()

    def __str__(self):
        return self.GroupJourneyName

