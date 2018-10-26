#!/usr/bin/python
#coding=utf-8

import httplib2
import json
import urllib
from api import common
from conf.api_link import scene_api
from conf.parameter_website import pro_prefix
from conf.parameter_website import test_prefix

class scene_save(object):
    
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

    def save(self, headers, payload):
        url = self.prefix.url_s + scene_api.save
        if headers['Content-Type']:
            fooContentType = headers['Content-Type']
        foo_headers = headers
        foo_headers['Content-Type'] = 'text/plain; charset=UTF-8'
        if str == type(payload) or unicode == type(payload):
            foo_payload = payload
        elif dict == type(payload):
            foo_payload = json.dumps(payload)
        else:
            print 'Error: wrong payload:', payload
        resp, cont = self.h.request(url, 'POST', foo_payload, foo_headers)
        if fooContentType:
            headers['Content-Type'] = fooContentType
        else:
            headers['Content-Type'] = 'application/x-www-form-urlencoded'
        return common.response_2_json(resp, cont)

    def save_audio_cutting(self, headers, audio_id, cut_path, start=0, mp3_duration=30, rate=''):
        url = self.prefix.url_s + scene_api.save_audio_cut
        payload = {'id':audio_id, 'start':start, 'duration':mp3_duration,
                   'url':cut_path, 'rate':rate}
        resp, cont = self.h.request(url, 'POST', urllib.urlencode(payload), headers)
        return common.response_2_json(resp, cont)

    def save_file_7niu(self, headers, path, name, size, file_type=1, biz_type=0, tag_id=0):
        '''
        fileType: 1=图片，2=背景音乐, 4=音效
        return: <dict>
        '''
        url = self.prefix.url_s + scene_api.save_file
        payload = {'name':name, 'size':size, 'path':path, 'tmbPath':path,
                   'fileType':file_type, 'bizType':biz_type, 'tagId':tag_id}
        resp, cont = self.h.request(url, 'POST', urllib.urlencode(payload), headers)
#         print 'Debug: save_file_7niu:', resp
#         print 'Debug: save_file_7niu:', cont
        return common.response_2_json(resp, cont)

    def save_page_name(self, headers, page_id, scene_id, page_name):
        url = self.prefix.url_s + scene_api.save_pagename
        payload = {'id':page_id, 'sceneId':scene_id, 'name':page_name}
        resp, cont = self.h.request(url, 'POST', urllib.urlencode(payload), headers)
#         print 'Debug: save_page_name:', resp
#         print 'Debug: save_page_name:', cont
        return common.response_2_json(resp, cont)

    def save_setting(self, headers, foo):
        '''
        foo = {}
            if bf.has_key('accessCode'):
                foo['accessCode'] = bf['accessCode']
            foo['autoFlip'] = autoFlip
            foo['autoFlipTime'] = autoFlipTime
            foo['cover'] = cover
            foo['description'] = desc
            foo['forbidHandFlip'] = forbidHandFlip
            foo['id'] = sceneId
            foo['name'] = name
            foo['pageMode'] = pageMode
            foo['shareDes'] = shareDes
            foo['slideNumber'] = slideNumber
            foo['status'] = status
            foo['triggerLoop'] = triggerLoop
            foo['type'] = sceneType
        '''
        url = self.prefix.url_s + scene_api.save_setting
        resp, cont = self.h.request(url, 'POST', urllib.urlencode(foo), headers)
#         print 'Debug: save_setting:', resp
#         print 'Debug: save_setting:', cont
        return common.response_2_json(resp, cont)
