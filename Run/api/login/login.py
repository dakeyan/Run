#!/usr/bin/python
#coding=utf-8

import httplib2
import re
import urllib
from api import common
from conf.api_link import login_api
from conf.parameter_website import pro_header, test_header, pre_header
from conf.parameter_website import pro_prefix, test_prefix, pre_prefix

class session(object):
    
    h = httplib2.Http('.cache')
    headers = test_header.headers
    prefix = test_prefix
    
    def __init__(self, server_type='test'):
        if server_type == 'test':
            pass
        elif server_type == 'pro':
            self.headers = pro_header.headers
            self.prefix = pro_prefix
        elif server_type == 'pre':
            self.headers = pre_header.headers
            self.prefix = pre_prefix
        else:
            print 'Error: wrong parameter "server_type"'
            raise

    def bind_phone1(self, headers, phone, code, password):
        url = self.prefix.url_s + login_api.bind_phone1
        payload = {'phone':phone, 'code':code, 'pass':password}
        resp, cont = self.h.request(url, 'POST', urllib.urlencode(payload), headers)
        print 'Debug: bind_phone:', resp
        print 'Debug: bind_phone:', cont
        return common.response_2_json(resp, cont)

    def bind_phone_code(self, headers, phone, account_type):
        url = self.prefix.url_s + login_api.bind_phone_code1
        payload = {'phone':phone, 'type':account_type}
        resp, cont = self.h.request(url, 'POST', urllib.urlencode(payload), headers)
        return common.response_2_json(resp, cont)
    
    def get_account_info(self, headers):
        url = self.prefix.url_s + login_api.get_account_info
        resp, cont = self.h.request(url, 'GET', headers=headers)
        print 'Debug: get_account_info:', resp
        print 'Debug: get_account_info:', cont
        return common.response_2_json(resp, cont)

    def get_captcha(self, headers):
        url = self.prefix.url_s + login_api.get_captcha
        resp, cont = self.h.request(url, 'GET', headers=headers)
        print 'Debug: get_captcha:', resp
        print 'Debug: get_captcha:', cont
        return common.response_2_json(resp, cont)
    
    def get_login_status(self, headers):
        url = self.prefix.url_s + login_api.get_login_status
        resp, cont = self.h.request(url, 'GET', headers=headers)
#         print 'Debug: get_login_status:', resp
#         print 'Debug: get_login_status:', cont
        return common.response_2_json(resp, cont)

    def get_sms_token(self, headers, phone):
        url = self.prefix.url_s + login_api.get_sms_token + '?phone=' + phone
        resp, cont = self.h.request(url, 'GET', headers=headers)
        return common.response_2_json(resp, cont)

    def login(self, account, psd, remember_me='false'):
        '''
        return: <list>
        '''
        url = self.prefix.url_s + login_api.login
        payload = {'username':account,
                   'password':psd,
                   'rememberMe':remember_me}
        if self.headers.has_key('cookie'):
            del self.headers['cookie']
        resp, cont = self.h.request(url, 'POST', urllib.urlencode(payload), self.headers)
#         print 'Debug: user.login:', resp
#         print 'Debug: user.login:', cont
        foo_cookie = resp['set-cookie']
        foo_cookie = re.sub('__DAYU_PP=.*?(?=JSESSIONID)', '', foo_cookie)
        self.headers['cookie'] = foo_cookie
        foo_header = {}
        for foo in self.headers.keys():
            foo_header[foo] = self.headers[foo]
        return common.response_2_json(resp, cont), foo_header

    def login_dingding(self, headers, app_id, code, post_redirect_url):
        url = self.prefix.url_s + login_api.login_dingding + '?appId=' + app_id + '&code=' + code + '&post_redirect_url=' + post_redirect_url
        resp, cont = self.h.request(url, 'GET', headers=headers)
        return common.response_2_json(resp, cont)

    def login_mobile(self, headers, mobile_account):
        url = self.prefix.url_s + login_api.login_mobile
        payload = {'account': mobile_account}
        resp, cont = self.h.request(url, 'POST', urllib.urlencode(payload), headers)
        return common.response_2_json(resp, cont)

    def login_qq_pc(self, headers, qq_account):
        url = self.prefix.url_s + login_api.login_qq_pc
        payload = {'account': qq_account}
        resp, cont = self.h.request(url, 'POST', urllib.urlencode(payload), headers)
        return common.response_2_json(resp, cont)

    def login_wechatmp(self, headers, app_id, code, post_redirect_url):
        url = self.prefix.url_s + login_api.login_wechatmp + '?appId=' + app_id + '&code=' + code + '&state=' + post_redirect_url
        resp, cont = self.h.request(url, 'GET', headers=headers)
        return common.response_2_json(resp, cont)

    def login_wechatqr(self, headers, app_id, open_id):
        url = self.prefix.url_s + login_api.login_wechatqr
        payload = {'appId':app_id, 'openId':open_id}
        resp, cont = self.h.request(url, 'POST', urllib.urlencode(payload), headers)
        return common.response_2_json(resp, cont)

    def login_wechat_pc(self, headers, wechat_code):
        url = self.prefix.url_s + login_api.login_wechat_pc
        payload = {'code': wechat_code}
        resp, cont = self.h.request(url, 'POST', urllib.urlencode(payload), headers)
        return common.response_2_json(resp, cont)
    
    def login_weibo(self, headers, app_id, code, post_redirect_url):
        url = self.prefix.url_s + login_api.login_weibo + '?appId=' + app_id + '&code=' + code + '&state=' + post_redirect_url
        resp, cont = self.h.request(url, 'GET', headers=headers)
        return common.response_2_json(resp, cont)

    def merge_user(self, headers, major_user, slave_user):
        url = self.prefix.url_s + login_api.merge_user
        payload = {'userId':major_user, 'fromUserId':slave_user}
        resp, cont = self.h.request(url, 'POST', urllib.urlencode(payload), headers)
        return common.response_2_json(resp, cont)

    def modify_password(self, headers, old_password, new_password):
        url = self.prefix.url_s + login_api.modify_password
        payload = {'oldPwd':old_password, 'newPwd':new_password}
        resp, cont = self.h.request(url, 'POST', urllib.urlencode(payload), headers)
        print 'Debug: modify_password,'
        return common.response_2_json(resp, cont)

    def pwd_retrieve_email(self, headers, ticket, email):
        url = self.prefix.url_s + login_api.pwd_retrieve_email
        payload = {'email':email, 'ticket':ticket}
        resp, cont = self.h.request(url, 'POST', urllib.urlencode(payload), headers)
        print 'Debug: pwd_retrieve_email:', resp
        print 'Debug: pwd_retrieve_email:', cont
        return common.response_2_json(resp, cont)

    def pwd_retrieve_email_4app(self, headers, email):
        url = self.prefix.url_s + login_api.pwd_retrieve_email_4app
        payload = {'email':email}
        resp, cont = self.h.request(url, 'POST', urllib.urlencode(payload), headers)
        print 'Debug: pwd_retrieve_email:', resp
        print 'Debug: pwd_retrieve_email:', cont
        return common.response_2_json(resp, cont)
    
    def pwd_retrieve_email_get(self, headers):
        url = self.prefix.url_s + login_api.pwd_retrieve_email
        resp, cont = self.h.request(url, 'GET', headers=headers)
        return common.response_2_json(resp, cont)

    def quick_login(self, phone, code, login_type=2):
        '''
        login_type: 1=旧快捷登录，自动注册      2=返回新用户标识
        '''
        url = self.prefix.url_s + login_api.quick_login
        if self.headers.has_key('cookie'):
            del self.headers['cookie']
        payload = {'phone':phone, 'code':code, 'type':login_type}
        resp, cont = self.h.request(url, 'POST', urllib.urlencode(payload), self.headers)
        print 'Debug: quick_login:', resp
        print 'Debug: quick_login:', cont
        foo_cookie = resp['set-cookie']
        foo_cookie = re.sub('__DAYU_PP=.*?(?=JSESSIONID)', '', foo_cookie)
        self.headers['cookie'] = foo_cookie
        foo_header = {}
        for foo in self.headers.keys():
            foo_header[foo] = self.headers[foo]
        return common.response_2_json(resp, cont), foo_header

    def register_code(self, headers, phone, ticket):
        ''' 手机注册  '''
        url = self.prefix.url_s + login_api.register_code
        payload = {'phone':phone, 'ticket':ticket}
        resp, cont = self.h.request(url, 'POST', urllib.urlencode(payload), headers)
        return common.response_2_json(resp, cont)

    def register_email(self, headers, code, email, password):
        ''' 邮箱注册 '''
        url = self.prefix.url_s + login_api.register_email
        payload = {'code':code, 'email':email, 'password':password}
        resp, cont = self.h.request(url, 'POST', urllib.urlencode(payload), headers)
        return common.response_2_json(resp, cont)
    
    def register_email_code(self, headers, email, ticket):
        ''' 邮箱注册 '''
        url = self.prefix.url_s + login_api.register_email_code
        payload = {'email':email, 'ticket':ticket}
        resp, cont = self.h.request(url, 'POST', urllib.urlencode(payload), headers)
        return common.response_2_json(resp, cont)

    def register_phone(self, headers, phone, password, code):
        ''' 手机注册  '''
        url = self.prefix.url_s + login_api.register_phone
        payload = {'phone':phone, 'passowrd':password, 'code':code}
        resp, cont = self.h.request(url, 'POST', urllib.urlencode(payload), headers)
        return common.response_2_json(resp, cont)

    def reset_code_phone(self, headers, phone, ticket):
        url = self.prefix.url_s + login_api.reset_code_phone
        payload = {'phone': phone, 'ticket':ticket}
        resp, cont = self.h.request(url, 'POST', urllib.urlencode(payload), headers)
        return common.response_2_json(resp, cont)

    def reset_code_phone_get(self, headers, phone, ticket):
        url = self.prefix.url_s + login_api.reset_code_phone + '?phone=' + phone + '&ticket=' + ticket
        resp, cont = self.h.request(url, 'GET', headers=headers)
        return common.response_2_json(resp, cont)

    def reset_password(self, headers, key, new_pwd, security_level=2):
        '''
        security_level: 123 对应 低中高
        ## nginx 中的配置显示，这个接口是给app 用的
        '''
        url = self.prefix.url_m1 + login_api.reset_password
        payload = {'key':key, 'newPwd':new_pwd, 'secuLevel':security_level}
        resp, cont = self.h.request(url, 'POST', urllib.urlencode(payload), headers)
        return common.response_2_json(resp, cont)

    def unbind_third1(self, headers, third_type):
        '''
        third_type:  qq/weixin
        '''
        url = self.prefix.url_s + login_api.unbind_third1
        payload = {'type':third_type}
        resp, cont = self.h.request(url, 'POST', urllib.urlencode(payload), headers)
        print 'Debug: unbind_third:', resp
        print 'Debug: unbind_third:', cont
        return common.response_2_json(resp, cont)
