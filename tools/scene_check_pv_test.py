#!/usr/bin/python
#coding=utf-8

import httplib2
import json

def main(scene_id):
    foo_pv = 100
    h = httplib2.Http()
    url = 'http://rmq.yqxiu.cn:15672/api/exchanges/%2Fscene/exchange.scene/publish'
    headers = {'authorization':'Basic YWRtaW46UEBzc3cwcmQ=',
               'Content-Type':'text/plain;charset=UTF-8',
               'Connection':'keep-alive',
               'Cache-Control':'no-cache',
               'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}
    payload = {'delivery_mode':'2',
               'headers':{},
               'name':'exchange.scene',
               'payload':'{"total_pv":"%s","id":"%s"}' % (foo_pv, scene_id),
               'payload_encoding':'string',
               'properties':{'delivery_mode':2,'headers':{}},
               'props':{},
               'routing_key':'scene.check.pv.test',
               'vhost':'/scene'}
    resp, cont = h.request(url, 'POST', json.dumps(payload), headers)
    print resp
    print cont
    print 'DONE'