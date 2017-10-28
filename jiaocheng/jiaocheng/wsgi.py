"""
WSGI config for jiaocheng project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
import sys  # 4
from django.core.wsgi import get_wsgi_application

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 3

sys.path.insert(0, PROJECT_DIR)  # 5

os.environ["DJANGO_SETTINGS_MODULE"] = "jiaocheng.settings"
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jiaocheng.settings")

application = get_wsgi_application()
