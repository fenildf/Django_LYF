# -*-coding:utf8-*-
import os
import sys
from django.forms import ModelForm, ValidationError
from jichu.models import Moment

#定义表单
class MomentForm(ModelForm):
    class Meta:
        model = Moment
        fields = '__all__'

    def clean(self):
        clean_data = super(MomentForm,self).clean()
        content = clean_data.get('content')
        if content is None:
            raise ValidationError("请输入Content内容！")
        elif content.find("ABCD") >= 0:
            raise ValidationError("不能输入敏感词汇！ ABCD")
        return clean_data

