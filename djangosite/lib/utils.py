import json
import hashlib
from django.http import JsonResponse


DEFAULT_PAGE_SIZE = 10
MAX_PAGE_SIZE = 30

class Status(object):
    SUCCESS = 0
    NEED_LOGIN = 1
    INVALID_PARAMS = 2
    INTERNAL_ERROR = 3
    NOT_EXIST = 4


class JsonResult(object):
    def __init__(self):
        self.meta = {}
        self.data = {}

    def success(self, data=None, msg=None):
        self.meta['status'] = Status.SUCCESS
        if msg:
            self.meta['msg'] = msg
        else:
            self.meta['msg'] = 'ok'
        if data:
            self.data = data

    def need_login(self, msg=None):
        self.fail(Status.NEED_LOGIN, msg)

    def invalid_params(self, msg=None):
        self.fail(Status.INVALID_PARAMS, msg)

    def not_exist(self, msg=None):
        self.fail(Status.NOT_EXIST, msg)

    def sys_error(self, msg=None):
        self.fail(Status.INTERNAL_ERROR, msg)

    def fail(self, status, msg):
        self.meta['status'] = status
        if msg:
            self.meta['msg'] = msg

    def to_json(self):
        return json.dumps({
            'meta': self.meta,
            'data': self.data
        })

    def to_http_resp(self):
        return JsonResponse({
            'meta': self.meta,
            'data': self.data
        })


def get_pagination_arg(request):
    '''
    获取请求对象中的分页相关的数据
    :param request: http 请求对象
    :return: request_page: 请求第几页数据
    :return: page_size: 一页包含的数据量
    :exception: RequestArgError: 分页的参数错误
    '''
    request_page = request.GET.get('page', 1)
    page_size = request.GET.get('page_size', DEFAULT_PAGE_SIZE)
    try:
        request_page = int(request_page)
        page_size = int(page_size)
        if page_size > MAX_PAGE_SIZE:
            page_size = DEFAULT_PAGE_SIZE
    except ValueError:
        raise RequestArgError()
    return request_page, page_size

def get_page_from_pagination(paginator, request_page):
    '''
    根据传入的页码，返回分页对象中对应页面的数据
    :param paginator: 分页对象
    :param request_page:  请求的页面的序号
    :return: res_page:  返回的页面数据
    :return: current_page: 返回的页面数据对应的页码
    '''
    total_num_pages = paginator.num_pages
    current_page = request_page if request_page < total_num_pages else total_num_pages
    res_page = paginator.page(current_page)
    res_page = res_page.object_list
    return res_page, current_page, total_num_pages

def md5(string):
    m = hashlib.md5()
    m.update(string.encode("utf8"))
    return m.hexdigest()

