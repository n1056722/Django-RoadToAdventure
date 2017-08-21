# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from users.models import *

# Create your models here.

class PersonalJourney(models.Model):
    STATUS_CHOICES = (
        ('0', 'planning'),
        ('1', 'riding'),
        ('2', 'finish'),
    )

    IS_OPEN_CHOICES = (
        ('0', 'private'),
        ('1', 'public'),
    )

    PersonalJourneyID = models.AutoField(primary_key=True)
    PersonalJourneyName = models.CharField(max_length=50)
    PersonalJourneyContent = models.TextField()
    Points = models.TextField()
    Status = models.CharField(max_length=1)
    IsOpen = models.CharField(max_length=1)
    StartTime = models.DateTimeField()
    EndTime = models.DateTimeField()
    CreateUser = models.ForeignKey(UserAccount, on_delete=models.PROTECT, related_name='PersonalJourney_CreateUser')
    CreateDate = models.DateTimeField()
    ModifyDate = models.DateTimeField()
   
    def __str__(self):
        return self.PersonalJourneyName


class PersonalJourneyComment(models.Model):
    PersonalJourneyCommentID = models.AutoField(primary_key=True)
    PersonalJourney = models.ForeignKey(PersonalJourney, on_delete=models.PROTECT, related_name='PersonalJourneyComment_personalJourney')
    Comment = models.TextField()
    CreateUser = models.ForeignKey(UserAccount, on_delete=models.PROTECT, related_name='PersonalJourneyComment_CreateUser')
    CreateDate = models.DateTimeField()

    def __str__(self):
        return self.Comment

class PersonalJourneyDetail(models.Model):
    PersonalJourneyDetailID = models.AutoField(primary_key=True)
    PersonalJourney = models.ForeignKey(PersonalJourney, on_delete=models.PROTECT, related_name='PersonalJourneyDetail_personalJourney')
    Latitude = models.CharField(max_length=30)
    Longitude = models.CharField(max_length=30)
    CreateDate = models.DateTimeField()

    def __str__(self):
        return self.Latitude + '-' + self.Longitude