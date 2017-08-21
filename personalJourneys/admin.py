# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from personalJourneys.models import *

admin.site.register(PersonalJourney)
'''
admin.site.register(PersonalJourneyComment)
admin.site.register(PersonalJourneyDetail)
'''