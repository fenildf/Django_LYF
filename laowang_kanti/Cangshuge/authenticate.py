#!/usr/bin/env python
# coding=utf-8

import os
import ldap
from etcd import Client
from django_auth_ldap.config import LDAPSearch, GroupOfNamesType

ETCD_HOST = os.environ['EV_ETCD_HOST']
ETCD_PORT = int(os.environ['EV_ETCD_PORT'])
ETCD_USERNAME = os.environ.get('EV_ETCD_USERNAME')
ETCD_PASSWORD = os.environ.get('EV_ETCD_PASSWORD')
client = Client(
    host=ETCD_HOST,
    port=ETCD_PORT,
    username=ETCD_USERNAME,
    password=ETCD_PASSWORD,
    allow_redirect=False
)
LDAP_CONFIG_DICT = eval(client.read('/common/ldap').value)
client.__del__()

__all__ = ['AUTH_LDAP_SERVER_URI',
           'AUTH_LDAP_CONNECTION_OPTIONS',
           'AUTH_LDAP_BIND_DN',
           'AUTH_LDAP_BIND_PASSWORD',
           'AUTH_LDAP_USER_SEARCH',
           'AUTH_LDAP_USER_ATTR_MAP',
           'AUTH_LDAP_ALWAYS_UPDATE_USER',
           'AUTHENTICATION_BACKENDS']

AUTH_LDAP_SERVER_URI = LDAP_CONFIG_DICT['host']
AUTH_LDAP_CONNECTION_OPTIONS = {ldap.OPT_REFERRALS: 0}
AUTH_LDAP_BIND_DN = LDAP_CONFIG_DICT['user']
AUTH_LDAP_BIND_PASSWORD = LDAP_CONFIG_DICT['passwd']
AUTH_LDAP_USER_SEARCH = LDAPSearch("dc=lejent, dc=cn",
    ldap.SCOPE_SUBTREE, "(uid=%(user)s)")
AUTH_LDAP_USER_ATTR_MAP = {
    "username": "uid",
    "first_name": "givenName",
    "last_name": "sn",
    "email": "mail",
    "is_staff": "active",
    "is_active": "active",
}
AUTH_LDAP_ALWAYS_UPDATE_USER = True
AUTHENTICATION_BACKENDS = (
    'django_auth_ldap.backend.LDAPBackend',
)
