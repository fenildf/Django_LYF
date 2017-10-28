import json

from django.http import JsonResponse


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
            self.meta['msg'] = 'success'
        if data is not None:
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
        }, ensure_ascii=False)

    def to_http_resp(self):
        return JsonResponse({
            'meta': self.meta,
            'data': self.data
        }, json_dumps_params={'ensure_ascii': False})
