# coding:utf-8
from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
import random
from appname.forms import AddForm
import os
from lib.interface import JsonResult
from lib.exceptions import UnknownRequest

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def Index(request):
    if request.method == 'POST':
        form = AddForm(request.POST)

        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(int(a) + int(b)))

    else:
        form = AddForm()
    return render(request,
                  os.path.join(PROJECT_ROOT, 'templates', 'index.html'),
                  {'form': form})


def index(request):
    # return render(request,
    #               os.path.join(PROJECT_ROOT, 'templates', 'home.html'))
    #return HttpResponse(u"hello world!")
    return render(request,
                  os.path.join(PROJECT_ROOT, 'templates', 'index.html'))


def add_number(request):
    a = request.GET.get('a',
                        random.randint(1,10))
    b = request.GET.get('b',
                        random.randint(10, 20))
    c = int(a) + int(b)
    return HttpResponse(str(c))

def add_number2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))

def old_add2_redirect(request, a, b):
    return HttpResponseRedirect(reverse('add_number_second',
                                        args=(a, b)))

def old_add_redirect(request):
    a = request.GET.get('a',
                        random.randint(1, 10))
    b = request.GET.get('b',
                        random.randint(10, 20))
    return HttpResponseRedirect(reverse('add_number',
                                        args=(a, b)))

def home(request):
    string = u"Django训练!"
    TutorialList = ["HTML", "CSS", "jQuery", "Python", "Django"]
    info_dict = {'site': u'自强学堂', 'content': u'各种IT技术教程'}
    List = map(str, range(100))
    return render(request,
                  os.path.join(PROJECT_ROOT, 'templates', 'home.html'),
                  {'string': string,
                   'TutorialList': TutorialList,
                   'info_dict': info_dict,
                   'List':List})