# -*-coding:utf8-*-
import os
import sys
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'welcome', views.welcome),
    url(r'moments_input', views.moments_input),
    url(r'employee_database', views.employee_database),
    url(r'now', views.current_datetime),
    url(r'detail', views.detail),
]