from functools import wraps
from random import randint
from django.db.utils import (
    ProgrammingError,
    InternalError
)
from question_viewer.models import (
    get_model_for_specified_table,
    Question
)


class EmptyModel(Exception):
    pass


class TableNotExists(Exception):
    pass


class NotStandardTable(Exception):
    pass


def catch_common_error(func):
    '''捕获通用的异常
    '''
    @wraps(func)
    def handle_exception(*args, **kwargs):
        # 处理的异常包括
        # 1. 数据表不存在
        # 2. 数据表结构不对
        try:
            res = func(*args, **kwargs)
        except ProgrammingError as err:
            if "doesn't exist" in str(err).lower():
                raise TableNotExists('数据表不存在')
            else:
                raise err
        except InternalError as err:
            print('--\n' * 100)
            if "unknown column" in str(err).lower():
                raise NotStandardTable('不是标准的question表')
            else:
                raise err
        return res
    return handle_exception


class QuestionFilterUtils(object):

    def _get_range_limited_query_set(self,
                                     model,
                                     min_id,
                                     max_id):
        '''获取限制了id范围的query_set
        '''
        query_set = model.objects
        if isinstance(min_id, int):
            query_set = query_set.filter(question_id__gte=min_id)
        if isinstance(max_id, int):
            query_set = query_set.filter(question_id__lte=max_id)
        return query_set

    def _get_question_id_range(self,
                               model,
                               min_id,
                               max_id):
        '''获取id的范围
        '''
        # 可能抛出的异常
        # 3. 数据表为空
        min_id_item = model.objects.order_by('question_id').first()
        if not min_id_item:
            raise EmptyModel('数据表为空数据表')
        real_min_id = min_id_item.question_id
        max_id_item = model.objects.order_by('-question_id').first()
        real_max_id = max_id_item.question_id
        if not min_id:
            min_id = real_min_id
        else:
            min_id = max(min_id, real_min_id)
        if not max_id:
            max_id = real_max_id
        else:
            max_id = min(max_id, real_max_id)
        return (min_id, max_id)

    @catch_common_error
    def get_random_question(self,
                            db_table,
                            min_id,
                            max_id,
                            size=2):
        '''随机选取题目
        '''
        # 随机筛选不适合利用MySQL的排序函数，因为数据量大时效率低下
        # 筛选方法:
        # 找出结果集中最大的id以及最小的id，随机取其中的某个数作为筛选条件
        # 找到id刚好比这个数大的记录作为结果返回
        model = get_model_for_specified_table(db_table)
        min_id, max_id = self._get_question_id_range(
            model, min_id, max_id
        )
        # 数据库自增id的间隔为19
        mysql_increase_step = 19
        if max_id - min_id < mysql_increase_step:
            middle_id = min_id
        else:
            # 为了选出足够的题目,需要限制id的最大值
            tmp_id = max_id - ((size - 1) * 19)
            middle_id = randint(min_id, tmp_id)
        question_lst = model.objects.filter(
            question_id__gte=middle_id,
            question_id__lte=max_id
        ).order_by('question_id')[:size]
        return question_lst

    @catch_common_error
    def get_question(self,
                     db_table,
                     min_id,
                     max_id,
                     ordering='asc',
                     size=2):
        '''按照顺序/逆序的方式获取题目
        '''
        model = get_model_for_specified_table(db_table)
        query_set = self._get_range_limited_query_set(
            model, min_id, max_id
        )
        if ordering == 'asc':
            query_set = query_set.order_by('question_id')
        else:
            query_set = query_set.order_by('-question_id')
        return query_set[:size]

    @catch_common_error
    def get_sibling_question(self,
                             db_table,
                             min_id,
                             max_id,
                             current_question_id,
                             which_sibling='previous',
                             size=2):
        '''根据question_id获取上/下一组题目
        '''
        model = get_model_for_specified_table(db_table)
        query_set = self._get_range_limited_query_set(
            model, min_id, max_id
        )
        if which_sibling == 'previous':
            query_set = query_set.filter(
                question_id__lt=current_question_id
            ).order_by('-question_id')
        else:
            query_set = query_set.filter(
                question_id__gt=current_question_id
            ).order_by('question_id')
        return query_set[:size]

    @catch_common_error
    def get_specified_question(self,
                               db_table,
                               spider_url,
                               size=2):
        '''根据spider_url获取指定的题目
        '''
        model = get_model_for_specified_table(db_table)
        return model.objects.filter(spider_url=spider_url)[:size]

    def get_question_from_question_pre(self, spider_url):
        '''根据spider_url从`question_pre`.`question`表中获取题目
        '''
        return Question.objects\
                       .filter(spider_url=spider_url)\
                       .first()

    @catch_common_error
    def get_question_by_question_id(self, question_id):
        '''根据传入的question_id获取题目
        '''
        return Question.objects\
                       .filter(question_id=question_id)\
                       .first()
