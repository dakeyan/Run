#!/usr/bin/python
#coding=utf-8

import httplib2
import urllib
from api import common
from conf.api_link import scene_api
from conf.parameter_website import pro_prefix
from conf.parameter_website import test_prefix

class scene_get(object):

    h = httplib2.Http('.cache')

    def __init__(self, headers):
        if headers.has_key('Origin'):
            if headers['Origin'] == test_prefix.header_origin:
                self.prefix = test_prefix
            elif headers['Origin'] == pro_prefix.header_origin:
                self.prefix = pro_prefix
            else:
                print 'Error: bad value in origin:', headers['Origin']
                raise
        else:
            print 'Error: there is no origin in header'
            raise

    def get_7niu_token(self, headers, token_type):
        ''' token_type: image audio video attach '''
        url = self.prefix.url_s + scene_api.get_7niu_token
        payload = {'type':token_type}
        resp, cont = self.h.request(url, 'POST', urllib.urlencode(payload), headers)
#         print 'Debug: get_7niu_token:', resp
#         print 'Debug: get_7niu_token:', cont
        return common.response_2_json(resp, cont)

    def get_page_list(self, headers, scene_id):
        url = self.prefix.url_s + scene_api.page_list + '/' + str(scene_id)
        resp, cont = self.h.request(url, 'GET', headers=headers)
        return common.response_2_json(resp, cont)

    def get_scene_list(self, headers, page_size=12, page_num=1, sub_account='', scene_name='', scene_group_id=''):
        url = self.prefix.url_s + scene_api.get_scene_list
        payload = {'pageNo':page_num, 'pageSize':page_size,
                   'user':sub_account, 'name':scene_name, 'groupId':scene_group_id}
        resp, cont = self.h.request(url, 'POST', urllib.urlencode(payload), headers)
        # return['list'][0]['id']
        return common.response_2_json(resp, cont)

    def getIdsScene(self, pageSize=12, pageNo=1, user=None, name=None, groupId=None):
        self.result = {}
        self.result['sceneId'] = []
        self.result['sceneCode'] = []
        url = self.urlService + '/m/scene/my'
        body = {'pageSize':pageSize,
                'pageNo':pageNo}
        if user:
            body['user'] = user
        if name:
            body['name'] = name
        if groupId:
            body['groupId'] = groupId
#         url='http://service.yqxiu.cn/m/scene/my?pageNo=1&pageSize=11'
        resp, content = self.h.request(url, 'POST', headers=self.headers, body=urllib.urlencode(body))
        foo = self.toJSON(resp, content)
        self.result['success'] = foo['success']
        if foo.has_key('map') and foo['map']:
            self.result['map'] = foo['map']
        if foo.has_key('list') and foo['list']:
            for joo in foo['list']:
                self.result['sceneId'].append(joo['id'])
                self.result['sceneCode'].append(joo['code'])

    def get_scene_setting(self, headers, scene_id):
        url = self.prefix.url_s + scene_api.get_scene_setting + '/' + str(scene_id)
        resp, cont = self.h.request(url, 'GET', headers=headers)
        return common.response_2_json(resp, cont)

    def get_status_cutting(self, headers, persist_id):
        url = self.prefix.url_s + scene_api.audio_status + '?pid=' + str(persist_id)
        resp, cont = self.h.request(url, 'GET')
        return common.response_2_json(resp, cont)
