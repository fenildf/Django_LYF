# -*-coding:utf8-*-
from django.db import models
from datetime import datetime
from elasticsearch_dsl import DocType, Date, Integer, \
    Keyword, Text, Nested, Boolean, analyzer, InnerObjectWrapper, Completion
from elasticsearch_dsl.connections import connections
from elasticsearch_dsl.analysis import CustomAnalyzer as _CustomAnalyzer


# Create your models here.

connections.create_connection(hosts= ['localhost'])

class CustomAnalyzer(_CustomAnalyzer):
    def get_analysis_definition(self):
        return {}

ik_analyzer = CustomAnalyzer("ik_max_word", filter= ["lowercase"])

KIND_CHOICES = (
    ('Python技术', 'Python技术'),
    ('数据库技术', '数据库技术'),
    ('经济学', '经济学'),
    ('文体资讯', '文体资讯'),
    ('个人心情', '个人心情'),
    ('其他', '其他'),
)


class Employee(models.Model):
    class Meta:
        db_table = '20171024_employee_ceshi'
        managed = 'False'

    name = models.CharField(max_length= 200)

class Moment(models.Model):
    class Meta:
        db_table = '20171024_moment_ceshi'
        managed = 'False'

    content = models.CharField(max_length=200)
    user_name = models.CharField(max_length= 20, default= '匿名')
    #default= KIND_CHOICES[0]
    kind = models.CharField(max_length= 200, choices= KIND_CHOICES, default=KIND_CHOICES[0])

class Article(DocType):
    suggest = Completion(analyzer= ik_analyzer)
    title = Text(analyzer= 'ik_max_word')
    md5 = Keyword()
    public_time = Date()
    writer = Keyword()
    pattern = Text(analyzer= 'ik_max_word')
    wenzhang = Keyword()
    html = Text(analyzer= 'ik_max_word')
    spdier_url = Keyword()

    class Meta:
        index = 'jingmeiti'
        doc_type = 'jingmeiti'

# if __name__ == '__main__':
#     Article.init()

# class Account(models.Model):
#     user_name = models.CharField(max_length= 80)
#     password = models.CharField(max_length= 255)
#     reg_date = models.DateField()
#
#     def __str__(self):
#         return "Account : %s" % self.user_name
#
# class Contact(models.Model):
#     #一对一关系
#     account = models.OneToOneField(
#         Account,
#         on_delete= models.CASCADE,
#         primary_key= True,
#     )
#
#     # #一对多关系
#     # account = models.ForeignKey(
#     #     Account,
#     #     on_delete= models.CASCADE,
#     # )
#
#     # #多对多关系
#     # account = models.ManyToManyField(Account)
#
#     zip_code = models.CharField(max_length= 10)
#     address = models.CharField(max_length= 80)
#     mobile = models.CharField(max_length= 20)
#
#     def __str__(self):
#         return "%s , %s" % (self.account.user_name, self.mobile)

# class MessageBase(models.Model):
#     id = models.AutoField()
#     content = models.CharField(max_length= 100)
#     user_name = models.CharField(max_length= 80)
#     pub_date = models.DateField()
#
#     class Meta:
#         #如果False，则下面的字段从5个变成2个
#         abstract = True
#
# class MomentMB(MessageBase):
#     #5个字段id/content/user_name/pub_date/headlines
#     headline = models.CharField(max_length= 50)
#
# LEVELS = (
#     ('1', 'Very good'),
#     ('2', 'Good'),
#     ('3', 'Normal'),
#     ('4', 'Bad'),
# )
#
# class Comment(MessageBase):
#     #5个字段id/content/user_name/pub_date/level
#     level = models.CharField(max_length= 1, choices= LEVELS)