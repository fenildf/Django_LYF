"""
Django settings for djangosite project.

Generated by 'django-admin startproject' using Django 1.11.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""
from etcd.client import Client
import os
import json
import pymysql

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
#D:\pycharm\PyCharm 2017.1\djangosite
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_FILE =  os.path.join(BASE_DIR, 'config')
config = json.load(open(CONFIG_FILE))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '07#-&^w*cku2x3q9=o=gjx8f7-^ar@y(@b1-g!*@6%$p0(wltl'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['192.168.2.115', '192.168.20.214']


# Application definition

INSTALLED_APPS = [
    #'jichu.apps.JichuConfig'
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'jichu.apps.JichuConfig',
    'todo.apps.TodoConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'djangosite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'djangosite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'html_archive2',
        'USER': config['user'],
        'PASSWORD': config['password'],
        'HOST': config['host'],
        'PORT': '3306',
    },
}
#     'html_db': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'html_archive2',
#         'USER': config['user'],
#         'PASSWORD': config['password'],
#         'HOST': config['host'],
#         'PORT': '3306',
#     },
#     'gevent_db': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'question_db_offline',
#         'USER': config['user'],
#         'PASSWORD': config['password'],
#         'HOST': config['host'],
#         'PORT': '3306',
#     },
# }

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

DATABASE_APPS_MAPPING = {
    # example:
    #'app_name':'database_name',
    'jichu': 'html_db',
    'todo': 'gevent_db',
}

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

RQ_QUEUES = {
    'default': {
        'HOST': '10.170.251.183',
        'PORT': 16379,
        'DB': 4,
        'PASSWORD': '',
        'DEFAULT_TIMEOUT': 60,
    }
}