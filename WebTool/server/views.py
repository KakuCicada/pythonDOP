# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response

# Create your views here.
def homepage(request):
    return render_to_response('home.html')

def basepage(request):
    return render_to_response('base.html')