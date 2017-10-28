from django.test import TestCase
import os
import json
# Create your tests here.
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NAME = os.path.join(PROJECT_ROOT, 'db.sqlite3')
CONFIG_FILE =  os.path.join(PROJECT_ROOT, 'config')
config = json.load(open(CONFIG_FILE))
print(CONFIG_FILE)
print(config['host'])
print(NAME)