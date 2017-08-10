# -*- coding: utf-8 -*-
from __future__ import unicode_literals
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
    result = {'result': 0}
    data = json.loads(request.body.decode("utf-8"))
    userId = data['userId']
    password = data['password']
    # query
    # players = Player.objects.filter(Email = email,Password = password)
    # response
    try:
        u = UserAccount.objects.get(UserID = userId,Password = password)
        result['userId'] = u.UserID
        result['email'] = u.EMail
        result['userName'] = u.UserName
        #result['userPicture'] = u.UserPicture
        #result['modifyDate'] = str(u.ModifyDate)
        result['result'] = 1
    except Exception as e:
        result['message'] = str(e)
    return JsonResponse(result)

def signUp(request):

    result = {'result': 0}
    data = json.loads(request.body.decode("utf-8"))
    userId = data['userId']
    email = data['email']
    password = data['password']
    userName = data['userName']
    # query
    try:
        if UserAccount.objects.filter(EMail = email).count() == 0 :
            now = datetime.datetime.now().replace(microsecond=0)
            UserAccount.objects.create(UserID=userId,EMail=email,Password=password,UserName=userName)
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
        u = UserAccount.objects.get(UserID=userId,Password=oldPassword)
        u.Password = newPassword
        u.save()
        result['result'] = 1
    except Exception as e:
        result['message'] = str(e)
    return JsonResponse(result)

def createFriend(request):
    result = {'result': 0}
    data = json.loads(request.body.decode("utf-8"))
    createId = data['createId']
    friendId = data['friendId']
    # query
    try: 
        u = UserAccount.objects.get(UserID = createId)
        uf = UserAccount.objects.get(UserID = friendId)
        now = datetime.datetime.now().replace(microsecond=0)
        UserFriend.objects.create(CreateUser = u,FriendUser = uf,CreateDate = now)
        result['result'] = 1
    except Exception as e:
        result['message'] = str(e)
    return JsonResponse(result)

def deleteFriend(request):
    result = {'result': 0}
    data = json.loads(request.body.decode("utf-8"))
    createId = data['createId']
    friendId = data['friendId']
    # query
    try: 
        u = UserAccount.objects.get(UserID = createId)
        uf = UserAccount.objects.get(UserID = friendId)
        UserFriend.objects.get(CreateUser = u,FriendUser = uf).delete()
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
        result['strangers'] = stranger
        result['result'] = 1 if len(stranger) > 0 else 0
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
    createId = data['createId']
    friendId = data['friendId']
    content = data['content']
    try:
        u = UserAccount.objects.get(UserID = createId)
        uf = UserAccount.objects.get(UserID = friendId)
        now = datetime.datetime.now().replace(microsecond=0)
        Chat.objects.create(CreateUser = u,FriendUser = uf,Content = content,CreateDate = now)
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
        selfChats = Chat.objects.select_related('CreateUser').filter(CreateUser__UserID = userId and FriendUser__UserID = friendId)
        otherChats = Chat.objects.select_related('CreateUser').filter(CreateUser__UserID = friendId and FriendUser__UserID = userId)
        for sc in selfChats:
            if sc.ChatId > lastChatId:
                
                chat = {}
                chat['chatId'] = sc.Chat.ChatId
                chat['userId'] = sc.Chat.UserID
                chat['userName'] = sc.Chat.UserName
                chat['content'] = sc.Chat.Content
                chat['createDate'] = sc.Chat.CreateDate
                chats.append(sc)

        for oc in otherChats:
            if oc.ChatId > lastChatId:
                chat = {}
                chat['chatId'] = oc.Chat.ChatId
                chat['userId'] = oc.Chat.UserID
                chat['userName'] = oc.Chat.UserName
                chat['content'] = oc.Chat.Content
                chat['createDate'] = oc.Chat.CreateDate
                chats.append(oc)
                           
        result['chats'] = chats
        result['result'] = 1 if len(chats) > 0 else 0
    except Exception as e:
        result['message'] = str(e)
    return JsonResponse(result)    





