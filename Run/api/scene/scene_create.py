#!/usr/bin/python
#coding=utf-8

import httplib2
import urllib
from api import common
from conf.api_link import scene_api
from conf.parameter_website import pro_prefix
from conf.parameter_website import test_prefix

class scene_create(object):
    
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

    def create_page(self, headers, page_id, long_page=''):
        ''' long_page: <int> '''
        if long_page:
            url = self.prefix.url_s + scene_api.create_page + '/' + str(page_id) + '?longPage=' + str(long_page)
        else:
            url = self.prefix.url_s + scene_api.create_page + '/' + str(page_id)
        resp, cont = self.h.request(url, 'GET', headers=headers)
        return common.response_2_json(resp, cont)

    def create_scene(self, headers, scene_type=101, page_mode=2, scene_name='', editor_mode=''):
        url = self.prefix.url_s + scene_api.create_scene
        payload = {'type':scene_type, 'pageMode':page_mode}
        if scene_name:
            payload['name'] = scene_name
        if editor_mode:
            ## editor_mode=3: 功能模板
            payload['editorModel'] = editor_mode
        resp, cont = self.h.request(url, 'POST', urllib.urlencode(payload), headers)
#         print 'Debug: create_scene:', resp
#         print 'Debug: create_scene:', cont
        return common.response_2_json(resp, cont)
