# -*- coding: utf-8 -*-
import os
import sys
import datetime
import time
import operator
import csv
import urllib2
import base64
import json
try:
    from collections import OrderedDict
except:
    from ordereddict import OrderedDict

from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.core import serializers
from django.utils.timezone import utc
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseNotFound
from django.http import HttpResponseForbidden
from django.conf import settings
from django.db.models import Count

from .models import *


def events(request):
    t = get_template('cc/event.html')
    html = t.render(Context({
        'title': u'黒ノ砦前線 活動排名',
    }))
    return HttpResponse(html)


def events_new(request):
    t = get_template('cc/tprs.html')
    html = t.render(Context({
        'title': u'黒ノ砦前線 活動排名',
    }))
    return HttpResponse(html)


def dps(request):
    t = get_template('cc/dps.html')
    html = t.render(Context({
        'title': u'DPS模擬器',
    }))
    return HttpResponse(html)



