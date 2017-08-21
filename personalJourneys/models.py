# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from users.models import *

# Create your models here.

class PersonalJourney(models.Model):
    PersonalJourneyID = models.AutoField(primary_key=True)
    PersonalJourneyName = models.CharField(max_length=50)
    PersonalJourneyContent = models.TextField()
    Points = models.TextField()
    Status = models.CharField(max_length=1)
    IsOpen = models.CharField(max_length=1)
    StartTime = models.DateTimeField()
    EndTime = models.DateTimeField()
    CreateUser = models.ForeignKey(UserAccount,on_delete=models.PROTECT,related_name='PersonalJourney_CreateUser')
    CreateDate = models.DateTimeField()
   
    def __str__(self):
        return self.PersonalJourneyName
"""
class PersonalJourneyPicture(models.Model):
    PersonalJourneyPictureID = models.IntegerField(primary_key=True)
    PersonalJourney = models.ForeignKey(PersonalJourney,primary_key=True,on_delete=models.PROTECT)
    PictureName = models.CharField(max_length=200)
    Create = models.ForeignKey(UserAccount,on_delete=models.PROTECT,max_length=20)
    CreateDate = models.DateTimeField()

    def __str__(self):
        return self.PictureName

class PersonalJourneyComment(models.Model):
    PersonalJourneyCommentID = models.AutoField(primary_key=True)
    PersonalJourney = models.ForeignKey(PersonalJourney,on_delete=models.PROTECT,related_name='PersonalJourneyComment_personalJourney')
    Comment = models.TextField()
    CreateUser = models.ForeignKey(UserAccount,on_delete=models.PROTECT,related_name='PersonalJourneyComment_CreateUser')
    CreateDate = models.DateTimeField()

    def __str__(self):
        return self.Comment

class PersonalJourneyDetail(models.Model):
    PersonalJourney = models.AutoField(primary_key=True)
    CreateDate = models.DateTimeField(primary_key=True)
    Latitude = models.CharField(max_length=30)
    Longitude = models.CharField(max_length=30)

    def __str__(self):
        return self.PersonalJourney

"""