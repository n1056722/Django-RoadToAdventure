# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from users.models import *
from django.shortcuts import render
#from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse,HttpResponse
import datetime
import json
import os

# Create your views here.

def index(request):
    return HttpResponse("Home")

def hello(request):
    result = {}
    result['result'] = 'users hello' #
    return JsonResponse(result)

def ya(request):
    result = {}
    result['result'] = 'users ya' #
    return JsonResponse(result)

def signIn(request):
    # request
    result = {}
    data = json.loads(request.body.decode("utf-8"))
    userId = data['userId']
    password = data['password']
    # query
    # players = Player.objects.filter(Email = email,Password = password)
    # response
    try:
        u = UserAccount.objects.get(UserID = userId,Password = password)
        result['userId'] = u.UserID
        result['email'] = u.Email
        result['userName'] = u.UserName
        result['userPicture'] = u.UserPicture
        result['modifyDate'] = str(u.ModifyDate)
        result['result'] = 1
    except UserAccount.DoesNotExist:
        result['result'] = 0
    return JsonResponse(result)

def signUp(request):

    result = {}
    data = json.loads(request.body.decode("utf-8"))
    userId = data['userId']
    email = data['EMail']
    password = data['password']
    userName = data['userName']
    # query
    if UserAccount.objects.filter(EMail = email).count() == 0 :
        now = datetime.datetime.now().replace(microsecond=0)
        UserAccount.objects.create(UserID=userId,EMail=email,Password=password,UserName=userName)
        result['result'] = 1
    else :
        result['result'] = 0
    return JsonResponse(result)
def updatePassword(request):
     # request
    result = {}
    data = json.loads(request.body.decode("utf-8"))
    userId = data['userId']
    oldPassword = data['oldPassword']
    newPassword = data['newPassword']
    # query
    try:
        u = UserAccount.objects.get(UserID=userId,Password=oldPassword)
        u.Password = newPassword
        u.save()
        result['result'] = 1
    except UserAccount.DoesNotExist:
        result['result'] = 0
    return JsonResponse(result)

def createFriend(request):
    result = {}
    data = json.loads(request.body.decode("utf-8"))
    userId = data['userId']
    friendId = data['friendId']
    # query
    if UserAccount.objects.filter(FriendID = friendId).count() == 0 :
        now = datetime.datetime.now().replace(microsecond=0)
        UserAccount.objects.create(UserID=userId,FriendID=friendId,CreateDate=now,UpdateDate=now)
        result['result'] = 1
    else :
       result['result'] = 0
    return JsonResponse(result)

def deleteFriend(request):
    result = {}
    data = json.loads(request.body.decode("utf-8"))
    userId = data['userId']
    friendId = data['friendId']
    # query
    if UserAccount.objects.filter(UserID = userId).count() == 0 :
        now = datetime.datetime.now().replace(microsecond=0)
        UserAccount.objects.delete(UserID=userId,FriendID=friendId)
        result['result'] = 1
    else :
        result['result'] = 0
    return JsonResponse(result)
