from django.db import models
from django.apps import apps


# 参考这里: http://dynamic-models.readthedocs.io/en/latest/pdfindex.html#

APP_LABEL = 'question_offline'


class Question(models.Model):
    question_id = models.IntegerField(primary_key=True)
    spider_source = models.IntegerField()
    spider_url = models.CharField(unique=True, max_length=256)
    knowledge_point = models.CharField(max_length=512)
    subject = models.IntegerField()
    zhuanti = models.CharField(max_length=256)
    exam_year = models.IntegerField()
    exam_city = models.CharField(max_length=128)
    question_type = models.IntegerField()
    question_quality = models.IntegerField()
    question_html = models.TextField()
    option_html = models.TextField()
    answer_all_html = models.TextField()
    jieda = models.TextField()
    fenxi = models.TextField()
    dianping = models.TextField()
    flag = models.IntegerField()

    class Meta:
        app_label = APP_LABEL
        db_table = '`question_pre`.`question`'


def get_model_for_specified_table(table_name):
    '''动态获取题目数据表模型
    '''
    class QuestionMetaClass(models.base.ModelBase):
        def __new__(cls, name, bases, attrs):
            model = super(QuestionMetaClass, cls)\
                    .__new__(cls, name, bases, attrs)
            return model

    class UniversalQuestion(models.Model):
        __metaclass__ = QuestionMetaClass

        question_id = models.IntegerField(primary_key=True)
        spider_source = models.IntegerField()
        spider_url = models.CharField(unique=True, max_length=256)
        knowledge_point = models.CharField(max_length=512)
        subject = models.IntegerField()
        zhuanti = models.CharField(max_length=256)
        exam_year = models.IntegerField()
        exam_city = models.CharField(max_length=128)
        question_type = models.IntegerField()
        question_quality = models.IntegerField()
        question_html = models.TextField()
        option_html = models.TextField()
        answer_all_html = models.TextField()
        jieda = models.TextField()
        fenxi = models.TextField()
        dianping = models.TextField()
        flag = models.IntegerField()

        class Meta:
            app_label = APP_LABEL
            db_table = table_name

    # 如果已经创建该数据模型，删除缓存的数据模型
    if apps.all_models.get(APP_LABEL) and \
            apps.all_models[APP_LABEL].get('universalquestion'):
        apps.all_models[APP_LABEL].pop('universalquestion')

    return UniversalQuestion
