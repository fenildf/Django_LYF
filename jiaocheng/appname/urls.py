# -*-coding:utf8-*-
import os
import sys
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'/index/$', views.index, name= 'index'),
    url(r'/add_number/$', views.add_number, name= 'add_number'),
    url(r'/add_number_second/(\d+)/(\d+)/$', views.add_number2, name= 'add_number_second'),
    url(r'/add_new/(\d+)/(\d+)/$', views.old_add2_redirect),
    url(r'/add_old/(\d+)/(\d+)/$', views.old_add_redirect),
    url(r'home?$', views.home, name= 'home'),
    url(r'home?$', views.home, name= 'home'),
]