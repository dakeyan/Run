#!/usr/bin/python
#coding=utf-8

import httplib2
import urllib
from api import common
from conf.api_link import scene_api
from conf.parameter_website import pro_prefix
from conf.parameter_website import test_prefix

class scene_delete(object):
    
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

    def delete_scene(self, headers, scene_id):
        url = self.prefix.url_s + scene_api.delete_scene
        payload = {'id':scene_id}
        resp, cont = self.h.request(url, 'POST', urllib.urlencode(payload), headers)
        return common.response_2_json(resp, cont)
