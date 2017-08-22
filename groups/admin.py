# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from groups.models import *
# Register your models here.
admin.site.register(Group)
admin.site.register(GroupRole)
admin.site.register(UserInGroup)
admin.site.register(GroupChat)