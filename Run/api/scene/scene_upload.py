#!/usr/bin/python
#coding=utf-8

import base64
import httplib2
import time
from api import common
from api.scene.scene import scene
from api.scene.scene_get import scene_get
from api.scene.scene_save import scene_save
from conf.parameter_db import static_value
from conf.parameter_website import pro_prefix
from conf.parameter_website import qiniu_prefix
from conf.parameter_website import test_prefix

class scene_upload():
    
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

    def upload_audio_7niu(self, headers, upload_token, file_name, file_buffer):
        url = qiniu_prefix.url_7niu
        foo_ext_name = common.get_ext_name(file_name)
        if not foo_ext_name:
            print 'Error: extention name is NULL'
        path_7niu = common.get_7niu_key() + '.' + foo_ext_name
        foo_tail = self.upload_pic_7niu_OPTIONS(headers)
        if foo_tail:
            boundary = '----WebKitFormBoundary' + foo_tail
        else:
            boundary = '----zzkkyy'
        if headers['Content-Type']:
            fooContentType = headers['Content-Type']
        foo_headers = headers
        foo_headers['Content-Type'] = 'multipart/form-data; boundary=%s' % boundary
        payload = common.get_upload_payload(boundary, path_7niu, upload_token, file_name, file_buffer, 'audio/mp3')
        resp, cont = self.h.request(url, 'POST', payload, foo_headers)
        if fooContentType:
            headers['Content-Type'] = fooContentType
        else:
            headers['Content-Type'] = 'application/x-www-form-urlencoded'
#         print 'Debug: upload_audio_7niu:', resp
#         print 'Debug: upload_audio_7niu:', cont
        return common.response_2_json(resp, cont)

    def upload_pic_7niu(self, headers, upload_token, file_name, file_buffer):
        url = qiniu_prefix.url_7niu
        ## filename
        foo_ext_name = common.get_ext_name(file_name)
        if not foo_ext_name:
            print 'Error: upload_pic_7niu: extention name is NULL'
        path_7niu = common.get_7niu_key() + '.' + foo_ext_name
        ## boundary
        foo_tail = self.upload_pic_7niu_OPTIONS(headers)
        if foo_tail:
            boundary = '----WebKitFormBoundary' + foo_tail
        else:
            boundary = '----zzkkyy'
#         headers['Referer'] = 'http://www.eqxiu.com/site/scene/create/40515?pageId=1'
#         headers['Referer'] = 'http://www.eqxiu.com/promotion/channel/mobile-alliance'
        if headers['Content-Type']:
            foo_ct = headers['Content-Type']
        foo_headers = headers
        foo_headers['Content-Type'] = 'multipart/form-data; boundary=%s' % boundary
    
        payload = common.get_upload_payload(boundary, path_7niu, upload_token, file_name, file_buffer)
        resp, cont = self.h.request(url, 'POST', payload, foo_headers)
#         print 'Debug: upload_pic_7niu:', resp
#         print 'Debug: upload_pic_7niu:', cont
#         del headers['Referer']
        if foo_ct:
            headers['Content-Type'] = foo_ct
        else:
            headers['Content-Type'] = 'application/x-www-form-urlencoded'
        return common.response_2_json(resp, cont)

    def upload_pic64_7niu(self, headers, upload_token, file_buffer):
        url = qiniu_prefix.url_7niu_64
        foo_headers = headers
        foo_headers['Authorization'] = 'UpToken ' + upload_token
        if headers['Content-Type']:
            foo_ct = headers['Content-Type']
        foo_headers['Content-Type'] = 'application/octet-stream'
        foo_buffer = base64.b64encode(file_buffer)
        resp, cont = self.h.request(url, 'POST', foo_buffer, foo_headers)
#         print 'Debug: upload_pic64_7niu:', resp
#         print 'Debug: upload_pic64_7niu:', cont
        if foo_ct:
            headers['Content-Type'] = foo_ct
        else:
            headers['Content-Type'] = 'application/x-www-form-urlencoded'
        del headers['Authorization']
        return common.response_2_json(resp, cont)
        
    def upload_pic_7niu_OPTIONS(self, headers):
        '''
        return: <str>
        '''
        url = qiniu_prefix.url_7niu
        resp, _ = self.h.request(url, 'OPTIONS', headers=headers)
        if resp.has_key('x-reqid'):
            return resp['x-reqid'].split(',')[0]
        else:
            return ''

    def upload_pic_7niu_function(self, headers, file_name, file_buffer):
        aa = scene_get(headers)
        bb = scene_save(headers)
        foo = aa.get_7niu_token(headers, 'image')
        foo_token = foo['map']['token']
        joo = self.upload_pic_7niu(headers, foo_token, file_name, file_buffer)
        foo_file_size = int(joo['size']) / 1024
        foo_file_path = joo['key']
        moo = bb.save_file_7niu(headers, foo_file_path, file_name, foo_file_size)
        return moo

    def upload_pic64_7niu_function(self, headers, file_buffer, file_name=''):
        aa = scene_get(headers)
        bb = scene_save(headers)
        foo = aa.get_7niu_token(headers, 'image')
        foo_token = foo['map']['token']
        joo = self.upload_pic64_7niu(headers, foo_token, file_buffer)
        foo_size = int(joo['size']) / 1024
        foo_path = joo['key']
        foo_name = file_name if file_name else foo_path
        moo = bb.save_file_7niu(headers, foo_path, foo_name, foo_size)
        return moo

    def upload_audio_7niu_function(self, headers, file_name, file_buffer, start=0, mp3_duration=0, file_type=2):
        aa = scene_get(headers)
        bb = scene_save(headers)
        cc = scene(headers)
        foo = aa.get_7niu_token(headers, 'audio')
        foo_token = foo['map']['token']
        joo = self.upload_audio_7niu(headers, foo_token, file_name, file_buffer)
        foo_size = int(joo['size']) / 1024
        foo_path = joo['key']
        moo = bb.save_file_7niu(headers, foo_path, file_name, foo_size, file_type)
        if start > 0 and mp3_duration > 0:
            noo = cc.audio_cutting(headers, foo_path, start, mp3_duration)
            foo_persist_id = noo['obj']
            for _ in xrange(static_value.LOOP_10):
                poo = aa.get_status_cutting(headers, foo_persist_id)
                foo_code = poo['map']['code']
                if 0 == foo_code:
                    break
                time.sleep(static_value.SLEEP_2)
            if not 0 == foo_code:
                print 'Error: get_status_cutting not finished'
                return poo
            foo_cut_path = poo['map']['path']
            foo_audio_id = moo['obj']['id']
            qoo = bb.save_audio_cutting(headers, foo_audio_id, foo_cut_path, start, mp3_duration)
            return qoo
        return moo
