#!/usr/bin/python
#coding=utf-8

import httplib2
import urllib
from api import common
from conf.api_link import scene_api
from conf.parameter_website import pro_prefix
from conf.parameter_website import test_prefix

class scene_set(object):
    
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

    def set_audio(self, headers, bg_audio, sceneId):
        '''
        bg_audio: <str>
            foo_bg_audio = {'id':foo_set_audio_id, 'url':foo_set_audio_url, 'name':foo_set_audio_name}
            foo_bg_audio_str = json.dumps(foo_bg_audio)
        '''
        url = self.prefix.url_s + scene_api.set_audio
        body = {}
        body['bgAudio'] = bg_audio if bg_audio else '{}'
        body['id'] = sceneId
        body['loading'] = 'ture'
        resp, cont = self.h.request(url, 'POST', urllib.urlencode(body), headers)
#         print 'Debug: set_audio:', resp
#         print 'Debug: set_audio:', cont
        return common.response_2_json(resp, cont)
