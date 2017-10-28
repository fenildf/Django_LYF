# -*-coding:utf8-*-

from appname.models import Blog
import django
if django.VERSION >= (1, 7):#自动判断版本
    django.setup()
from jiaocheng.wsgi import *
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jiaocheng.settings")


PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APPNAME_ROOT = os.path.dirname(os.path.abspath(__file__))

def main():
    with open(APPNAME_ROOT + '/db/oldblog.txt', 'r') as f:
        for line in f:
            title , content = line.split('****')
            Blog.objects.create(title= title, content= content)
        #BlogList = [Blog(title=line.split('****')[0], content=line.split('****')[1]) for line in f]
    f.close()
    Blog.objects.bulk_create(BlogList)


if __name__ == '__main__':
    print("start the txt2db.txt")
    script_dir = os.path.split(os.path.realpath(__file__))[0]  # 获取脚本所在的目录
    prj_dir = os.path.dirname(script_dir)  # 获取其上级目录，及django项目所在的目录。
    sys.path.append(prj_dir)  # 在python系统路径中加入上一步得到的目录。

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jiaocheng.settings")
    os.environ.update("DJANGO_SETTINGS_MODULE", "jiaocheng.settings")
    django.setup()

    main()
    print("DONE!")