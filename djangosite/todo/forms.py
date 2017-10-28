# -*-coding:utf8-*-
import os
import sys
from django.forms import ModelForm
from todo.models import Charactor, User

#定义表单
class CharactorForm(ModelForm):
    class Meta:
        model = Charactor
        fields = '__all__'

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
