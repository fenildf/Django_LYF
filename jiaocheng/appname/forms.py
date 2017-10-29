# -*-coding:utf8-*-
import re
from django import forms

class AddForm(forms.Form):
    a = forms.IntegerField()
    b = forms.IntegerField()