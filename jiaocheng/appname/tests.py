from django.test import TestCase
import os
import django

version = django.VERSION
# Create your tests here.
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APPNAME_ROOT = os.path.dirname(os.path.abspath(__file__))
f = open(APPNAME_ROOT + '/db/oldblog.txt')
for line in f:
    title, content = line.split('****')
    print(title)
print(APPNAME_ROOT)