# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def Create(request):
    result = {'result': 0}
    data = json.loads(request.body.decode("utf-8"))
    userId = data['userId']
    name = data['name']
    content = data['content']
    points = data['points']
    startTime = data['startTime']
    endTime = data['endTime']
    try:        
        PersonalJourney.objects.create(UserID=userId,PersonalJourneyName=name,PersonalJourneyContent=content,Status='0',IsOpen='0',StartTime=startTime,EndTime=endTime,Points=points,CreateDate=now())
        result['result'] = 1
    except Exception as e:
        result['message'] = str(e)
    return JsonResponse(result)

def now():
    return datetime.datetime.now().replace(microsecond=0)