#!/usr/bin/python
#coding=utf-8

import httplib2
import urllib
from api import common
from conf.api_link import mall_api
from conf.parameter_website import pro_prefix
from conf.parameter_website import test_prefix

class mall_max(object):
    
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

    def product_publish(self, headers, product_id):
        '''
        product_id: '12345'   or   '12345; 23456'
        '''
        url = self.prefix.url_max + mall_api.publish_product
        payload = {'ids':product_id}
        resp, cont = self.h.request(url, 'POST', urllib.urlencode(payload), headers)
        return common.response_2_json(resp, cont)

    def product_revoke(self, headers, product_id):
        url = self.prefix.url_max + mall_api.revoke_product
        payload = {'ids':product_id}
        resp, cont = self.h.request(url, 'POST', urllib.urlencode(payload), headers)
        return common.response_2_json(resp, cont)
    
    def update_index(self, headers):
        url = self.prefix.url_max + mall_api.update_index
        payload = {'thirdCateId':''}
        resp, cont = self.h.request(url, 'POST', urllib.urlencode(payload), headers)
        return common.response_2_json(resp, cont)