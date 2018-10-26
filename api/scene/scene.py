#!/usr/bin/python
#coding=utf-8

import httplib2
import urllib
from api import common
from conf.api_link import scene_api
from conf.parameter_website import pro_prefix
from conf.parameter_website import test_prefix

class scene(object):
    
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

    def audio_cutting(self, headers, path, start=0, mp3_duration=0):
        url = self.prefix.url_s + scene_api.audio_cut
        payload = {'path':path, 'start':start, 'duration':mp3_duration}
        resp, cont = self.h.request(url, 'POST', urllib.urlencode(payload), headers)
        return common.response_2_json(resp, cont)
        pass

    def apply_app_tpl(self, headers, scene_id, t1_id='890163', t1_name='节假热点', t2_id='890197', t2_name='热点2', price=0):
        url = self.prefix.url_s + scene_api.apply_app_tpl
        payload = {'category':[{'id':t1_id, 'name':t1_name, 'children':[{'id':t2_id, 'name':t2_name}]}],
                   'id':scene_id, 'price':price}
        resp, cont = self.h.request(url, 'POST', urllib.urlencode(payload), headers)
#         print 'Debug: apply_app_tpl:', resp
#         print 'Debug: apply_app_tpl:', cont
        return common.response_2_json(resp, cont)

    def copy_page(self, headers, page_id):
        url = self.prefix.url_s + scene_api.create_page + '/' + str(page_id) + '?copy=true'
        resp, cont = self.h.request(url, 'GET',headers=headers)
        return common.response_2_json(resp, cont)
    
    def copy_scene_emodel2(self, headers, scene_id):
        url = self.prefix.url_s + scene_api.copy_scene
        payload = {'id':scene_id, 'editorModel':2}
        resp, cont = self.h.request(url, 'POST', urllib.urlencode(payload), headers)
#         print 'Debug: copy_scene_emodel2:', resp
#         print 'Debug: copy_scene_emodel2:', cont
#         return['obj'] is new scene id
        return common.response_2_json(resp, cont)

    def publish(self, headers, scene_id, check_type=''):
        '''
        checkType:1=加急, 2=驳回加急
        return: <dict>
        '''
        if check_type:
            url = self.prefix.url_s + scene_api.publish + '?id=' + str(scene_id) + '&checkType=' + str(check_type)
        else:
            url = self.prefix.url_s + scene_api.publish + '?id=' + str(scene_id)
        resp, cont = self.h.request(url, 'GET', headers=headers)
#         print 'Debug: publish:', resp
#         print 'Debug: publish:', cont
        return common.response_2_json(resp, cont)

    def transfer_scene(self, headers, scene_id, receiver):
        url = self.prefix.url_s + scene_api.transfer_scene
        payload = {'id':scene_id, 'loginName':receiver, 'platform':0}
        resp, cont = self.h.request(url, 'POST', urllib.urlencode(payload), headers)
        return common.response_2_json(resp, cont)
