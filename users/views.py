# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from core.settings import MEDIA_ROOT, IMAGE_USER_URL, IMAGE_PERSONAL_JOURNEY_URL, IMAGE_GROUP_JOURNEY_URL, IMAGE_OTHER_URL
from users.models import *
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse,HttpResponse
import datetime
import json
import os


# Create your views here.

def index(request):
    return HttpResponse("Home")

def login(request):
    # request
    result = {'result': 0}
    data = json.loads(request.body.decode("utf-8"))
    userId = data['userId']
    password = data['password']
    # query
    try:
        u = UserAccount.objects.get(
            UserID=userId,
            Password=password
        )
        result['userId'] = u.UserID
        result['email'] = u.EMail
        result['userName'] = u.UserName
        result['userPicture'] = u.UserPicture
        result['modifyDate'] = str(u.ModifyDate)
        result['result'] = 1
    except Exception as e:
        result['message'] = str(e)
    return JsonResponse(result)

def signUp(request):
    # request
    result = {'result': 0}
    data = json.loads(request.body.decode("utf-8"))
    userId = data['userId']
    email = data['email']
    password = data['password']
    userName = data['userName']
    # query
    try:
        if UserAccount.objects.filter(EMail = email).count() == 0 :
            UserAccount.objects.create(
                UserID = userId,
                EMail = email,
                Password = password,
                UserName = userName,
                CreateDate = now(),
                ModifyDate = now()
            )
            result['result'] = 1
    except Exception as e:
        result['message'] = str(e)
    return JsonResponse(result)


def updatePassword(request):
    # request
    result = {'result': 0}
    data = json.loads(request.body.decode("utf-8"))
    userId = data['userId']
    oldPassword = data['oldPassword']
    newPassword = data['newPassword']
    # query
    try:
        u = UserAccount.objects.get(
            UserID = userId,
            Password = oldPassword
        )
        u.Password = newPassword
        u.save()
        result['result'] = 1
    except Exception as e:
        result['message'] = str(e)
    return JsonResponse(result)

def updatePicture(request):
    # request
    result = {'result': 0}
    data = json.loads(request.body.decode("utf-8"))
    userId = data['userId']
    picturePath = data['picturePath']
    # query
    try:
        u = UserAccount.objects.get(UserID=userId)
        u.UserPicture = picturePath
        u.save()
        result['result'] = 1
    except Exception as e:
        result['message'] = str(e)
    return JsonResponse(result)

def createFriend(request):
    result = {'result': 0}
    data = json.loads(request.body.decode("utf-8"))
    userId = data['userId']
    friendId = data['friendId']
    # query
    try: 
        u = UserAccount.objects.get(UserID = userId)
        uf = UserAccount.objects.get(UserID = friendId)
        if UserFriend.objects.filter(CreateUser = u, FriendUser = uf).count() == 0 :
            UserFriend.objects.create(
                CreateUser = u,
                FriendUser = uf,
                CreateDate = now()
            )
            result['result'] = 1
    except Exception as e:
        result['message'] = str(e)
    return JsonResponse(result)

def deleteFriend(request):
    result = {'result': 0}
    data = json.loads(request.body.decode("utf-8"))
    userId = data['userId']
    friendId = data['friendId']
    # query
    try: 
        u = UserAccount.objects.get(UserID = userId)
        uf = UserAccount.objects.get(UserID = friendId)
        UserFriend.objects.get(
            CreateUser = u,
            FriendUser = uf
        ).delete()
        result['result'] = 1
    except Exception as e:
        result['message'] = str(e)
    return JsonResponse(result)


def getStrangerList(request):
    result = {'result': 0}
    data = json.loads(request.body.decode("utf-8"))
    userId = data['userId']
    try:
        selfFriends = UserFriend.objects.select_related('CreateUser').filter(CreateUser__UserID = userId)
        otherFriends = UserFriend.objects.select_related('CreateUser').filter(FriendUser__UserID = userId)
        strangers = []
        for of in otherFriends:
            isFriend = False
            for sf in selfFriends:
                if of.CreateUser == sf.FriendUser:
                    isFriend = True
                    break
            if not isFriend:
                stranger = {}
                stranger['userId'] = of.CreateUser.UserID
                stranger['userName'] = of.CreateUser.UserName
                strangers.append(stranger)
        result['strangers'] = strangers
        result['result'] = 1 if len(strangers) > 0 else 0
    except Exception as e:
        result['message'] = str(e)
    return JsonResponse(result)

def getFriendList(request):
    result = {'result': 0}
    data = json.loads(request.body.decode("utf-8"))
    userId = data['userId']
    try:
        friends = []
        for uf in UserFriend.objects.select_related('FriendUser').filter(CreateUser__UserID = userId):
            friend = {}
            friend['userId'] = uf.FriendUser.UserID
            friend['userName'] = uf.FriendUser.UserName
            friends.append(friend)
        result['friends'] = friends
        result['result'] = 1 if len(friends) > 0 else 0
    except Exception as e:
        result['message'] = str(e)
    return JsonResponse(result)

def createFriendChat(request):
    result = {'result': 0}
    data = json.loads(request.body.decode("utf-8"))
    userId = data['userId']
    friendId = data['friendId']
    content = data['content']
    try:
        u = UserAccount.objects.get(UserID = userId)
        uf = UserAccount.objects.get(UserID = friendId)
        Chat.objects.create(
            CreateUser = u,
            FriendUser = uf,
            Content = content,
            CreateDate = now()
        )
        result['result'] = 1
    except Exception as e:
        result['message'] = str(e)
    return JsonResponse(result)

def getChatList(request):     
    result = {'result': 0}
    data = json.loads(request.body.decode("utf-8"))
    userId = data['userId']
    friendId = data['friendId']
    lastChatId = data['lastChatId']
    try:
        chats = []
        selfChats = Chat.objects.select_related('CreateUser').filter(CreateUser__UserID = userId  , FriendUser__UserID = friendId)
        otherChats = Chat.objects.select_related('CreateUser').filter(CreateUser__UserID = friendId , FriendUser__UserID = userId)
        for sc in selfChats:
            if sc.ChatID > lastChatId:                
                chat = {}
                chat['chatId'] = sc.ChatID
                chat['userId'] = sc.CreateUser.UserID
                chat['userName'] = sc.CreateUser.UserName
                chat['content'] = sc.Content
                chat['createDate'] = str(sc.CreateDate)
                chats.append(chat)

        for oc in otherChats:
            if oc.ChatID > lastChatId:
                chat = {}
                chat['chatId'] = oc.ChatID
                chat['userId'] = oc.CreateUser.UserID
                chat['userName'] = oc.CreateUser.UserName
                chat['content'] = oc.Content
                chat['createDate'] = str(oc.CreateDate)
                chats.append(chat)
                           
        result['chats'] = chats
        result['result'] = 1 if len(chats) > 0 else 0
    except Exception as e:
        result['message'] = str(e)
    return JsonResponse(result)    

def getPath(x):
    return {
        "0": IMAGE_USER_URL,
        "1": IMAGE_PERSONAL_JOURNEY_URL,
        "2": IMAGE_GROUP_JOURNEY_URL
    }.get(x, IMAGE_OTHER_URL)

def createPicture(request):
    # request
    result = {'result': 0}
    fileName = request.POST.get('fileName')
    subFileName = request.POST.get('subFileName')
    mFile = request.FILES.get('file')
    mType = request.POST.get('type')

    if mFile is not None:
        try:
            completeFileName = fileName + '.' + subFileName
            path = getPath(mType)
            with open(os.path.join(MEDIA_ROOT, path, completeFileName), 'wb+') as destination:
                for chunk in mFile.chunks():
                    destination.write(chunk)
            
            result['picturePath'] = completeFileName
            result['fullPath'] = 'http://' + request.get_host() + '/images/' + path + '/' + completeFileName
            result['result'] = 1
        except Exception as e:
            result['message'] = str(e)
    return JsonResponse(result)

def now():
    return datetime.datetime.now().replace(microsecond=0)