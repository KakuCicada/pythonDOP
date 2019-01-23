# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response

hometitle='服务器管理系统'
# Create your views here.
def homepage(request):
    return render_to_response('home.html', {'title': hometitle,'username': 'Kaku'})

def basepage(request):
    return render_to_response('base.html')