# -*- coding:utf-8 -*-

from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.homepage),
    url(r'^home', views.homepage),
    url(r'^base', views.basepage)
]