#!/usr/bin/python
#coding=utf-8

import httplib2
import json
import urllib
from api import common
from conf.api_link import max_api
from conf.parameter_website import pro_prefix, test_prefix, dev_prefix

class backstage(object):
    
    h = httplib2.Http('.cache')

    def __init__(self, headers):
        if headers.has_key('Origin'):
            if headers['Origin'] == test_prefix.header_origin:
                self.prefix = test_prefix
            elif headers['Origin'] == pro_prefix.header_origin:
                self.prefix = pro_prefix
            elif headers['Origin'] == dev_prefix.header_origin:
                self.prefix = dev_prefix
            else:
                print 'Error: bad value in origin:', headers['Origin']
                raise
        else:
            print 'Error: there is no origin in header'
            raise

    def get_sms_log(self, headers, log_id):
        url = self.prefix.url_max + max_api.sms_log
        payload = {'sortOrder':'asc', 'pageSize':10, 'pageNumber':1,
                   'id':log_id, 'bid':'', 'sid':'', 'batch':'',
                   'createTime':'', 'createEndTime':'', 'status':''}
        resp, cont = self.h.request(url, 'POST', urllib.urlencode(payload), headers)
        print 'Debug: get_sms_log:', resp
        print 'Debug: get_sms_log:', cont
        return common.response_2_json(resp, cont)

    def get_sms_log_mobile(self, headers):
        url = self.prefix.url_max + max_api.sms_log_mobile
        payload = {'sortOrder':'asc', 'pageSize':10, 'pageNumber':1, 'lid':'', 'mobile':'',
                   'createTime':'', 'status':1}
        resp, cont = self.h.request(url, 'POST', urllib.urlencode(payload), headers)
        print 'Debug: get_sms_log_mobile:', resp
        print 'Debug: get_sms_log_mobile:', cont
        return common.response_2_json(resp, cont)
        pass

    def pass_tpl(self, headers, scene_id, platform=1, tpl_status=1, properties='890197'):
        '''
        platform: 1=pc  3=app
        tplstatus: 1=初审    2=复审
        properties: 样例标签: <t2_id>
        '''
        url = self.prefix.url_max + max_api.pass_tpl
        payload = {'ids':scene_id, 'type':platform, 'tplStatus':tpl_status, 'properties':properties,
                   'status':'true', 'optimization':2}
        resp, cont = self.h.request(url, 'POST', urllib.urlencode(payload), headers)
#         print 'Debug: pass_tpl:', resp
#         print 'Debug: pass_tpl:', cont
        return common.response_2_json(resp, cont)

    def send_sms(self, headers, mobile, title, msg):
        '''
        mobile: '2342342345, 234234545'
        title, msg: <str>
        '''
        url = self.prefix.url_postino + max_api.send_sms
        params = {'subject':title, 'message':msg}
        payload = {'tid':'6001', 'mobiles':mobile, 'pamams':json.dumps(params)}
        print url
        print json.dumps(params)
        print urllib.urlencode(payload)
        resp, cont = self.h.request(url, 'POST', urllib.urlencode(payload), headers)
        print 'Debug: send_sms:', resp
        print 'Debug: send_sms:', cont
        return common.response_2_json(resp, cont)
