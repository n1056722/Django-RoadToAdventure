# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from personalJourneys.models import *
from users.models import UserAccount
import datetime
import json

# Create your views here.
def createPersonalJourney(request):
    result = {'result': 0}
    data = json.loads(request.body.decode("utf-8"))
    userId = data['userId']
    name = data['name']
    content = data['content']
    points = data['points']
    status = data['status']
    isOpen = data['isOpen']
    startTime = data['startTime']
    endTime = data['endTime']
    try:
        u = UserAccount.objects.get(UserID = userId)
        PersonalJourney.objects.create(
            PersonalJourneyName = name,
            PersonalJourneyContent = content,
            Status = status,
            IsOpen = isOpen,
            StartTime = startTime,
            EndTime = endTime,
            Points = points,
            CreateUser = u,
            CreateDate = now()
        )
        result['result'] = 1
    except Exception as e:
        result['message'] = str(e)
    return JsonResponse(result)

def updatePersonalJourney(request):
    result = {'result': 0}
    data = json.loads(request.body.decode("utf-8"))
    personalJourneyId = data['personalJourneyId']
    name = data['name']
    content = data['content']
    points = data['points']
    status = data['status']
    isOpen = data['isOpen']
    startTime = data['startTime']
    endTime = data['endTime']

    try:
        pj = PersonalJourney.objects.get(PersonalJourneyID = personalJourneyId)
        pj.PersonalJourneyName = name
        pj.PersonalJourneyContent = content
        pj.Points = points
        pj.Status = status
        pj.IsOpen = isOpen
        pj.StartTime = startTime
        pj.EndTime = endTime
        pj.ModifyDate = now()
        pj.save()
        result['result'] = 1
    except Exception as e:
        result['message'] = str(e)
    return JsonResponse(result)

def now():
    return datetime.datetime.now().replace(microsecond=0)