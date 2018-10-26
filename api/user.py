#!/usr/bin/python
#coding=utf-8

import httplib2
import re
import urllib
from api import common
from conf.api_link import user_api
from conf.parameter_website import pro_header, test_header, dev_header, pre_header
from conf.parameter_website import pro_prefix, test_prefix, dev_prefix, pre_prefix


class user(object):
    
    h = httplib2.Http('.cache')
    headers = test_header.headers
    prefix = test_prefix
    
    def __init__(self, server_type='test'):
        if server_type == 'test':
            pass
        elif server_type == 'pro':
            self.headers = pro_header.headers
            self.prefix = pro_prefix
        elif server_type == 'dev':
            self.headers = dev_header.headers
            self.prefix = dev_prefix
        elif server_type == 'pre':
            self.headers = pre_header.headers
            self.prefix = pre_prefix
        else:
            print 'Error: wrong parameter "server_type"'
            raise

    def login(self, account, psd, remember_me='false'):
        '''
        return: <list>
        '''
        url = self.prefix.url_s + user_api.login
        payload = {'username':account,
                   'password':psd,
                   'rememberMe':remember_me}
        if self.headers.has_key('cookie'):
            del self.headers['cookie']
        resp, cont = self.h.request(url, 'POST', urllib.urlencode(payload), self.headers)
        print 'Debug: user.login:', resp
        print 'Debug: user.login:', cont
        foo_cookie = resp['set-cookie']
        foo_cookie = re.sub('__DAYU_PP=.*?(?=JSESSIONID)', '', foo_cookie)
        self.headers['cookie'] = foo_cookie
        foo_header = {}
        for foo in self.headers.keys():
            foo_header[foo] = self.headers[foo]
        return common.response_2_json(resp, cont), foo_header

    def logout(self, headers):
        url = self.prefix.url_s + user_api.logout
        resp, cont = self.h.request(url, 'GET', headers=headers)
#         print 'Debug: user.logout:',resp
#         print 'Debug: user.logout:',cont
        return common.response_2_json(resp, cont)
        
