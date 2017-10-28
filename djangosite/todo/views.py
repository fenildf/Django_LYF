from django.shortcuts import render
from .models import TodoEntry
from .models import Charactor, User
from .forms import CharactorForm, UserForm
from django.shortcuts import render_to_response, render
from datetime import datetime
from django.http import HttpResponseRedirect, HttpResponse
import os
from django.template import RequestContext
from django.template import Context
from django.core.urlresolvers import reverse
from django.views import View
from lib.utils import (
    JsonResult,
    get_pagination_arg,
    get_page_from_pagination,
    md5,
)

from .models import (
    User,
    Charactor,
    TodoEntry,
)
# Create your views here.

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class DetailWordParse(View):
    def get(self, request, html_id):
        json_result = JsonResult()
        try:
            query = User.objects.get(html_id= html_id)
        except Exception as e:
            json_result.success([])
            return json_result.to_http_resp()

            # 如果没有用户姓名，也就没啥可展示的了，那就为空
            if query.userName == '':
                data = {}
            else:
                data = self.handle_json_data(query)

            json_result.success(data)
            return json_result.to_http_resp()

        def handle_json_data(self, query):
            data = {}

            data['html_id'] = query.html_id
            data['username'] = query.userName
            data['password'] = query.passWord
            data['cid'] = query.cid

            return data

class DetailArchive2Parse(View):
    def get(self, request, html_id):
        json_result = JsonResult()
        try:
            query = Charactor.objects.get(html_id= html_id)
        except Exception as e:
            json_result.success([])
            return json_result.to_http_resp()

        if query.charactor == '':
            data = {}
        else:
            data = self.handle_json_data(query)

        json_result.success(data)
        return json_result.to_http_resp()

    def handle_json_data(self, query):
        data = {}

        data['html_id'] = query.html_id
        data['charactor'] = query.charactor
        data['hGroup'] = query.hGroup

        return data

def welcome(request):
    return HttpResponse("<h1>Welcome to my tiny twitter!</h1>")

def Index(request):
    all_todo_list = TodoEntry.objects.all().order_by('-create_date')
    return render(os.path.join(PROJECT_ROOT, 'templates', 'index.html'),
                              {'all_todo_list': all_todo_list})

def add(request):
    try:
        task_msg = request.POST['task_msg']
        entry = TodoEntry(task=task_msg, status=1, create_date=datetime.now())
        entry.save()
    except Exception as e:
        print(e)

        return render(os.path.join(PROJECT_ROOT, 'templates', 'index.html'),
                                  {'error_msg': "no task msg isprovided!"})
def Input_charactor(request):
    if request.method == 'post':
        form = CharactorForm(request.POST)
        if form.is_valid():
            charactor = form.save()
            charactor.save()
            return HttpResponseRedirect(reverse('todo.views.welcome'))
    else:
        form = CharactorForm()
        return render(request, os.path.join(PROJECT_ROOT, 'templates', 'moments_input.html'),
                      {'form': form})

def Input_user(request):
    if request.method == 'post':
        form = UserForm(request.POST)
        user = form.save()
        user.save()
        return HttpResponseRedirect(reverse('todo.views.welcome'))
    else:
        form = UserForm()
        return render(request, os.path.join(PROJECT_ROOT, 'templates', 'moments_input.html'),
                      {'form': form})