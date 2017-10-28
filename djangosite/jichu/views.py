from django.shortcuts import render
from django.http import HttpResponse
from jichu.models import Moment, Employee
import os
from django.http import HttpResponseNotFound
from jichu.forms import MomentForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
import datetime
# Create your views here.

def welcome(request):
    return HttpResponse("<h1>Welcome to my tiny twitter!</h1>")

def employee_database(request):
    if request.method == 'post':
        form = Employee(request.POST)
        if form.is_valid():
            employee = form.save()
            employee.save()
            return HttpResponseRedirect(reverse("jichu.views.welcome"))
    else:
        form = Employee()
    PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return render(request, os.path.join(PROJECT_ROOT, 'templates', 'moments_input.html'),
                  {'form': form})

def moments_input(request):
    if request.method == 'post':
        form = MomentForm(request.POST)
        if form.is_valid():
            moment = form.save()
            moment.save()
            return HttpResponseRedirect(reverse("jichu.views.welcome"))

    else:
        form = MomentForm()
    PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return render(request, os.path.join(PROJECT_ROOT, 'templates', 'moments_input.html'),
                  {'form': form})

def view_moment(request):
    data = {'content': 'Please input the content',
            'user_name': '匿名',
            'kind': 'Python技术',
            }
    f = MomentForm(request.POST, initial= data)
    if f.has_changed():
        print("如下字段进行了修改： %s" % '')
        for filed in f.changed_data:
            print(filed)

def current_datetime(request):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return HttpResponse(now)

def detail(request, moment_id):
    m = Moment.objects.get(id = moment_id)
    return render(request, 'templates/moment.html', {'headline': m.headline, 'user': m.user_name})

def my_view(request):
    #return HttpResponse(status= 404)\
    return HttpResponseNotFound()

