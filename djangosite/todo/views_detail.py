# -*-coding:utf8-*-
import os
import sys
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

class DetailWordParse(View):
    def get(self, request, html_id):
        json_result = JsonResult()
        try:
            query = User.objects.get(html_id= html_id)
        except ObjectDoesNotExist as e:
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
