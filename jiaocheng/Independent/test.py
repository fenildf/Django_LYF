# -*-coding:utf8-*-
import os
import sys
from etcd import Client
from django.conf import settings
settings.configure()
#from appname.models import Blog

# script_dir = os.path.split(os.path.realpath(__file__))[0]           # 获取脚本所在的目录
# prj_dir = os.path.dirname(script_dir)                               # 获取其上级目录，及django项目所在的目录。
# #sys.path.append(prj_dir)                                            # 在python系统路径中加入上一步得到的目录。
#
# environ_settings = os.environ.get("DJANGO_SETTINGS_MODULE")
#
# print(environ_settings)
# print("***" * 30)
# print(script_dir)
# print("++++++" * 20)
# print(prj_dir)


ETCD_HOST = os.environ['EV_ETCD_HOST']
ETCD_PORT = int(os.environ['EV_ETCD_PORT'])
ETCD_USERNAME = os.environ.get('EV_ETCD_USERNAME')
ETCD_PASSWORD = os.environ.get('EV_ETCD_PASSWORD')
# ETCD_CLIENT = Client(
#     host=ETCD_HOST,
#     port=ETCD_PORT,
#     username=ETCD_USERNAME,
#     password=ETCD_PASSWORD,
#     allow_redirect=False
# )
# question_offline_db_value = ETCD_CLIENT.get(
#     '/db/question_pre_db',
# )
# print(question_offline_db_value)
# DB_CONFIG_DICT['question_offline_db'] = eval(
#     question_offline_db_value.value
# )
# assert DB_CONFIG_DICT['question_offline_db']['host'] == '10.44.149.251'
# DB_CONFIG_DICT['question_offline_db']['db'] = 'question_db_offline'

print(ETCD_HOST)
print('\n')
print(ETCD_PORT)
print('\n')
print(ETCD_PASSWORD)
print('\n')
print(ETCD_USERNAME)