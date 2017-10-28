import json
import re
from functools import wraps
from django.views import View
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout


from PowerRing import render_question_dict_for_tiku

from lib.interface import JsonResult
from lib.exceptions import UnknownRequest
from question_viewer.forms import QuestionLstFilterArgsForm
from question_viewer.utils import (
    QuestionFilterUtils,
    EmptyModel,
    TableNotExists,
    NotStandardTable
)

# Create your views here.

class IndexView(View):

    def get(self, request):
       return redirect('/web/index.html')


def required_login(func):
    '''验证用户是否登录
    '''
    @wraps(func)
    def check_login(instance, request, *args, **kwargs):
        if not request.user or \
                not request.user.is_active:
            jr = JsonResult()
            jr.need_login('请登录后再进行操作')
            return jr.to_http_resp()
        res = func(instance, request, *args, **kwargs)
        return res
    return check_login


@method_decorator(csrf_exempt, name='dispatch')
class LoginView(View):

    def post(self, request):
        jr = JsonResult()

        try:
            form_data = json.loads(request.body.decode('utf8'))
        except Exception as err:
            jr.invalid_params('参数错误')
        username = form_data.get('username', '')
        password = form_data.get('password', '')
        user = authenticate(username=username, password=password)
        login_success_flag = False
        if user is not None and \
                user.backend == 'django_auth_ldap.backend.LDAPBackend':
            if user.is_active:
                login_success_flag = True
        if login_success_flag:
            login(request, user)
            jr.success('登录成功')
            return jr.to_http_resp()
        else:
            jr.invalid_params('认证出错')
            return jr.to_http_resp()


class LogoutView(View):

    @required_login
    def get(self, request):
        jr = JsonResult()
        logout(request)
        jr.success('退出成功')
        return jr.to_http_resp()


class QuestionDetailView(QuestionFilterUtils, View):
    '''用于从question_pre.question表中取出题目数据
    '''
    @required_login
    def get(self, request, search_condition):
        jr = JsonResult()
        if re.match(r'^\s*$', search_condition):
            jr.invalid_params('参数不能为空')
            return jr.to_http_resp()
        if re.match(r'\d+', search_condition):
            question = \
                self.get_question_by_question_id(
                    search_condition
                )
        else:
            question = \
                self.get_question_from_question_pre(
                    search_condition
                )
        if not question:
            jr.not_exist('当前条件下查询不到题目')
            return jr.to_http_resp()
        question_html = render_question_dict_for_tiku(
            question
        )
        jr.success({
            'search_condition': search_condition,
            'html': question_html
        })
        return jr.to_http_resp()


class QuestionCompareView(QuestionFilterUtils, View):
    '''用于对比指定数据表的题目以及question_pre表的题目
    '''

    @required_login
    def get(self, request):
        jr = JsonResult()
        form = QuestionLstFilterArgsForm(request.GET)
        if form.is_valid():
            try:
                db_table = form.cleaned_data['db_table']
                new_question = self._get_question_from_table(
                    db_table, form.cleaned_data
                )
                if not new_question:
                    raise EmptyModel()
                print(new_question.spider_url)
                question = self.get_question_from_question_pre(
                    new_question.spider_url
                )
                new_question_html = render_question_dict_for_tiku(
                    new_question
                )
                res_data = {
                    'question': {
                        'question_id': new_question.question_id,
                        'html': new_question_html
                    }
                }
                if not question:
                    res_data['reference_question'] = None
                else:
                    question_html = render_question_dict_for_tiku(
                        question
                    )
                    res_data['reference_question'] = {
                        'question_id': question.question_id,
                        'html': question_html
                    }
                jr.success(res_data)
                return jr.to_http_resp()
            except TableNotExists as err:
                jr.not_exist(
                    '数据表`%s`不存在' % form.cleaned_data['db_table']
                )
                return jr.to_http_resp()
            except NotStandardTable:
                jr.not_exist(
                    '数据表`%s`不是标准的question表' % form.cleaned_data['db_table']
                )
                return jr.to_http_resp()
            except EmptyModel:
                jr.not_exist(
                    '数据表`%s`为空' % form.cleaned_data['db_table']
                )
                return jr.to_http_resp()
            except UnknownRequest as err:
                jr.invalid_params(str(err))
                return jr.to_http_resp()

        errors = form.errors.as_text().replace('\n', ';')
        jr.invalid_params(errors)
        return jr.to_http_resp()

    def _get_question_from_table(self, db_table, form_data):
        '''根据输入的条件获取题目列表
        '''
        size = 1
        # 1. 如果有question_url, 直接返回spider_url对应的题目
        if form_data.get('question_url'):
            new_question = self.get_specified_question(
                db_table, form_data['question_url']
            )
            return new_question
        # 2. 随机筛选题目
        elif form_data.get('filter_method') == 'random':
            new_question = self.get_random_question(
                db_table,
                form_data['min_id'],
                form_data['max_id'],
                size=size
            )
            new_question = new_question and new_question[0] or None
            return new_question
        # 3. 顺序或者逆序排列题目
        elif form_data.get('filter_method') in ('asc', 'desc'):
            new_question = self.get_question(
                db_table,
                form_data['min_id'],
                form_data['max_id'],
                form_data['filter_method']
            )
            new_question = new_question and new_question[0] or None
            return new_question
        # 4. 获取上一题或者下一题
        elif form_data.get('filter_method') in ('next', 'previous'):
            new_question = self.get_sibling_question(
                db_table,
                form_data['min_id'],
                form_data['max_id'],
                form_data['current_question_id'],
                which_sibling=form_data['filter_method'],
                size=size
            )
            new_question = new_question and new_question[0] or None
            return new_question
        else:
            raise UnknownRequest('未知服务')


class QuestionLstView(QuestionFilterUtils, View):
    '''用于筛选一组question列表
    '''

    @required_login
    def get(self, request):
        '''处理对题目列表的请求
        '''
        jr = JsonResult()
        form = QuestionLstFilterArgsForm(request.GET)
        if form.is_valid():
            try:
                question_lst = self._get_question_lst(
                    form.cleaned_data
                )
            except TableNotExists as err:
                jr.not_exist(
                    '数据表`%s`不存在' % form.cleaned_data['db_table']
                )
                return jr.to_http_resp()
            except NotStandardTable:
                jr.not_exist(
                    '数据表`%s`不是标准的question表' % form.cleaned_data['db_table']
                )
                return jr.to_http_resp()
            except EmptyModel:
                jr.not_exist(
                    '数据表`%s`为空' % form.cleaned_data['db_table']
                )
                return jr.to_http_resp()
            except UnknownRequest as err:
                jr.invalid_params(str(err))
                return jr.to_http_resp()
            if len(question_lst) == 1:
                question_lst = [question_lst[0], question_lst[0]]
            res_data = []
            for question in question_lst:
                question_html = render_question_dict_for_tiku(question)
                res_data.append({
                    'html': question_html,
                    'question_id': question.question_id
                })
            res_data = sorted(res_data, key=lambda m: m['question_id'])
            jr.success(res_data)
            return jr.to_http_resp()
        errors = form.errors.as_text().replace('\n', ';')
        jr.invalid_params(errors)
        return jr.to_http_resp()

    def _get_question_lst(self, form_data):
        '''根据输入的条件获取题目列表
        '''
        # 首先获取对应的的数据表模型
        if not form_data.get('size'):
            size = 2
        size = min(size, 4)
        db_table = form_data['db_table']
        # 1. 如果有question_url， 直接返回spider_url对应的题目
        if form_data.get('question_url'):
            return self.get_specified_question(
                db_table, form_data['question_url'], size=size
            )

        # 2. 随机筛选题目
        if form_data.get('filter_method') == 'random':
            return self.get_random_question(
                db_table,
                form_data['min_id'],
                form_data['max_id'],
                size=size
            )
        # 3. 顺序或者逆序排列题目
        elif form_data.get('filter_method') in ('asc', 'desc'):
            return self.get_question(
                db_table,
                form_data['min_id'],
                form_data['max_id'],
                form_data['filter_method'],
                size=size
            )
        # 4. 获取上一题或者下一题
        elif form_data.get('filter_method') in ('next', 'previous'):
            return self.get_sibling_question(
                db_table,
                form_data['min_id'],
                form_data['max_id'],
                form_data['current_question_id'],
                which_sibling=form_data['filter_method'],
                size=size
            )
        else:
            raise UnknownRequest('未知服务')
