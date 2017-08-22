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

def getPersonalJourneyList(request):
    result = {'result': 0}
    data = json.loads(request.body.decode("utf-8"))
    userId = data['userId']
    try:
        personalJourneys = []
        for pj in PersonalJourney.objects.filter(CreateUser__UserID = userId):
            personalJourney = {}
            personalJourney['personalJourneyId'] = pj.PersonalJourneyID
            personalJourney['name'] = pj.PersonalJourneyName
            personalJourney['content'] = pj.PersonalJourneyContent
            personalJourney['status'] = pj.Status
            personalJourney['createDate'] = str(pj.CreateDate)
            personalJourneys.append(personalJourney)
        result['personalJourneys'] = personalJourneys
        result['result'] = 1 if len(personalJourneys) > 0 else 0
    except Exception as e:
        result['message'] = str(e)
    return JsonResponse(result)

def getPersonalJourney(request):
    result = {'result': 0}
    data = json.loads(request.body.decode("utf-8"))
    personalJourneyId = data['personalJourneyId']
    try:
        pj = PersonalJourney.objects.get(PersonalJourneyID = personalJourneyId)
        result['personalJourneyId'] = personalJourneyId
        result['name'] = pj.PersonalJourneyName
        result['content'] = pj.PersonalJourneyContent
        result['status'] = pj.Status
        result['isOpen'] = pj.IsOpen
        result['startTime'] = str(pj.StartTime)
        result['endTime'] = str(pj.EndTime)
        result['createDate'] = str(pj.CreateDate)
        result['modifyDate'] = str(pj.ModifyDate)
        result['result'] = 1
    except Exception as e:
        result['message'] = str(e)
    return JsonResponse(result)

def createPersonalJourneyComment(request):
    result = {'result': 0}
    data = json.loads(request.body.decode("utf-8"))
    personalJourneyId = data['personalJourneyId']
    userId = data['userId']
    comment = data['comment']
    try:
        pj = PersonalJourney.objects.get(PersonalJourneyID = personalJourneyId)
        u = UserAccount.objects.get(UserID = userId)
        PersonalJourneyComment.objects.create(
            PersonalJourney = pj,
            Comment = comment,
            CreateUser = u,
            CreateDate = now()
        )
        result['result'] = 1
    except Exception as e:
        result['message'] = str(e)
    return JsonResponse(result)

def createPersonalJourneyDetail(request):
    result = {'result': 0}
    data = json.loads(request.body.decode("utf-8"))
    personalJourneyId = data['personalJourneyId']
    personalJourneyDetails = data['personalJourneyDetails']
    try:
        pj = PersonalJourney.objects.get(PersonalJourneyID = personalJourneyId)
        pjds = []
        for personalJourneyDetail in personalJourneyDetails:
            pjd = PersonalJourneyDetail()
            pjd.PersonalJourney = pj
            pjd.Latitude = personalJourneyDetail['latitude']
            pjd.Longitude = personalJourneyDetail['longitude']
            pjd.CreateDate = now()
            pjds.append(pjd)
        PersonalJourneyDetail.objects.bulk_create(pjds)
        result['result'] = 1
    except Exception as e:
        result['message'] = str(e)
    return JsonResponse(result)

def getAllPersonalJourneyDetail(request):
    result = {'result': 0}
    data = json.loads(request.body.decode("utf-8"))
    personalJourneyId = data['personalJourneyId']
    try:
        personalJourneyDetails = []
        for pjd in PersonalJourneyDetail.objects.filter(PersonalJourney__PersonalJourneyID = personalJourneyId):
            personalJourneyDetail = {}
            personalJourneyDetail['personalJourneyDetailId'] = pjd.PersonalJourneyDetailID
            personalJourneyDetail['latitude'] = pjd.Latitude
            personalJourneyDetail['longitude'] = pjd.Longitude
            personalJourneyDetail['createDate'] = str(pjd.CreateDate)
            personalJourneyDetails.append(personalJourneyDetail)
        result['personalJourneyDetails'] = personalJourneyDetails
        result['result'] = 1 if len(personalJourneyDetails) > 0 else 0
    except Exception as e:
        result['message'] = str(e)
    return JsonResponse(result)

def now():
    return datetime.datetime.now().replace(microsecond=0)