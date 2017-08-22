# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from users.models import UserAccount
from groups.models import *
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.db import transaction
import datetime
import json
# Create your views here.
def createGroup(request):
    # request
    result = {'result': 0}
    data = json.loads(request.body.decode("utf-8"))
    userId = data['userId']
    name = data['name']
    picturePath = data['picturePath']
    # query
    try:
        with transaction.atomic():
            u = UserAccount.objects.get(UserID = userId)
            g = Group.objects.create(
                GroupName = name,
                GroupPicture = picturePath,
                CreateUser = u,
                CreateDate = now(),
                ModifyUser = u,
                ModifyDate = now()
            )
            gr = GroupRole.objects.get(GroupRoleID = 'group_manager')
            UserInGroup.objects.create(
                User = u,
                Group = g,
                GroupRole = gr
            )
            result['result'] = 1
    except Exception as e:
        result['message'] = str(e)
    return JsonResponse(result)

def updateGroup(request):
    # request
    result = {'result': 0}
    data = json.loads(request.body.decode("utf-8"))
    groupId = data['groupId']
    userId = data['userId']
    name = data['name']
    picturePath = data['picturePath']
    # query
    try:
        u = UserAccount.objects.get(UserID = userId)
        g = Group.objects.get(GroupID = groupId)
        g.GroupName = name
        g.GroupPicture = picturePath
        g.ModifyUser = u
        g.ModifyDate = now()
        g.save()
        result['result'] = 1
    except Exception as e:
        result['message'] = str(e)
    return JsonResponse(result)

def getGroupList(request):
    # request
    result = {'result': 0}
    data = json.loads(request.body.decode("utf-8"))
    userId = data['userId']
    # query
    try:
        groups = []
        for uig in UserInGroup.objects.select_related('Group').filter(User__UserID = userId):
            group = {}
            group['groupId'] = uig.Group.GroupID
            group['name'] = uig.Group.GroupName
            group['picturePath'] = uig.Group.GroupPicture
            groups.append(group)
        result['groups'] = groups
        result['result'] = 1 if len(groups) > 0 else 0
    except Exception as e:
        result['message'] = str(e)
    return JsonResponse(result)

def getGroup(request):
    # request
    result = {'result': 0}
    data = json.loads(request.body.decode("utf-8"))
    groupId = data['groupId']
    # query
    try:
        g = Group.objects.get(GroupID = groupId)
        result['groupId'] = g.GroupID
        result['name'] = g.GroupName
        result['picturePath'] = g.GroupPicture
        members = []
        for uig in UserInGroup.objects.select_related('User', 'GroupRole').filter(Group = g):
            member = {}
            member['userId'] = uig.User.UserID
            member['userName'] = uig.User.UserName
            member['userPicture'] = uig.User.UserPicture
            member['groupRoleId'] = uig.GroupRole.GroupRoleID
            member['groupRoleName'] = uig.GroupRole.GroupRoleName
            members.append(member)
        result['members'] = members
        result['result'] = 1 if len(members) > 0 else 0
    except Exception as e:
        result['message'] = str(e)
    return JsonResponse(result)

def createGroupUser(request):
    # request
    result = {'result': 0}
    data = json.loads(request.body.decode("utf-8"))
    groupId = data['groupId']
    #userId = data['userId'] for check permission
    targetUserId = data['targetUserId']
    groupRoleId = data['groupRoleId']
    # query
    try:
        tu = UserAccount.objects.get(UserID = targetUserId)
        g = Group.objects.get(GroupID = groupId)
        if UserInGroup.objects.filter(User = tu, Group = g).count() == 0:
            gr = GroupRole.objects.get(GroupRoleID = groupRoleId)
            UserInGroup.objects.create(
                User = tu,
                Group = g,
                GroupRole = gr
            )
            result['result'] = 1
    except Exception as e:
        result['message'] = str(e)
    return JsonResponse(result)

def updateGroupUser(request):
    # request
    result = {'result': 0}
    data = json.loads(request.body.decode("utf-8"))
    groupId = data['groupId']
    #userId = data['userId'] for check permission
    targetUserId = data['targetUserId']
    groupRoleId = data['groupRoleId']
    # query
    try:
        gr = GroupRole.objects.get(GroupRoleID = groupRoleId)
        uig = UserInGroup.objects.get(User__UserID = targetUserId, Group__GroupID = groupId)
        uig.GroupRole = gr
        uig.save()
        result['result'] = 1
    except Exception as e:
        result['message'] = str(e)
    return JsonResponse(result)

def deleteGroupUser(request):
    # request
    result = {'result': 0}
    data = json.loads(request.body.decode("utf-8"))
    groupId = data['groupId']
    #userId = data['userId'] for check permission
    targetUserId = data['targetUserId']
    # query
    try:
        UserInGroup.objects.get(User__UserID = targetUserId, Group__GroupID = groupId).delete()
        result['result'] = 1
    except Exception as e:
        result['message'] = str(e)
    return JsonResponse(result)

def createGroupChat(request):
    # request
    result = {'result': 0}
    data = json.loads(request.body.decode("utf-8"))
    groupId = data['groupId']
    userId = data['userId']
    content = data['content']
    # query
    try:
        g = Group.objects.get(GroupID = groupId)
        u = UserAccount.objects.get(UserID = userId)
        GroupChat.objects.create(
            Group = g,
            User = u,
            Content = content,
            CreateDate = now()
        )
        result['result'] = 1
    except Exception as e:
        result['message'] = str(e)
    return JsonResponse(result)

def getGroupChatList(request):
    # request
    result = {'result': 0}
    data = json.loads(request.body.decode("utf-8"))
    groupId = data['groupId']
    lastChatId = data['lastChatId']
    # query
    try:
        groupChats = []
        for gc in GroupChat.objects.filter(Group__GroupID = groupId, GroupChatID__gt = lastChatId):
            groupChat = {}
            groupChat['groupChatId'] = gc.GroupChatID
            groupChat['userId'] = gc.User.UserID
            groupChat['userName'] = gc.User.UserName
            groupChat['userPicture'] = gc.User.UserPicture
            groupChat['content'] = gc.Content
            groupChat['createDate'] = str(gc.CreateDate)
            groupChats.append(groupChat)
        result['groupChats'] = groupChats
        result['result'] = 1 if len(groupChats) > 0 else 0
    except Exception as e:
        result['message'] = str(e)
    return JsonResponse(result)

def now():
    return datetime.datetime.now().replace(microsecond = 0)