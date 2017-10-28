# -*-coding:utf8-*-
import os
import sys
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'Charactor', views.Input_charactor),
    url(r'User', views.Input_user),
    url(r'detailarchive2parse', views.DetailArchive2Parse.as_view(), name= 'detailarchive2parse'),
    url(r'detailwordparse', views.DetailWordParse.as_view(), name= 'detailwordparse'),
    url(r'detailwordparse/(?P<html_id>[0-9a-z]+)/$', views.DetailWordParse.as_view(), name= 'detailwordparse'),
]