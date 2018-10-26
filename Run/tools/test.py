#!/usr/bin/python
#encoding: utf-8

import cx_Oracle
import httplib2
import json
import os
import pymysql
import re
# import urllib
# from api import common
from api.login.login import session
from api.max.max import backstage
# from api.scene import scene
from api.scene.scene_upload import scene_upload
from api.user import user
from conf.parameter_db import account_psd_pro, mysql_test, oracle_test, mongo_test
from conf.parameter_website import pro_header 
# from conf.parameter_website import test_header
from pymongo import mongo_client

def test_upload():
    aa = user('pro')
    _, foo_header = aa.login(account_psd_pro.account_show, account_psd_pro.psd_show)
    bb = scene_upload(foo_header)
    with open('C:\\Users\Ke\\Desktop\\a.js') as f:
        bb.upload_pic64_7niu_function(foo_header, f.read())
    aa.logout(foo_header)
    print 'DONE'

def test_mysql():
    db_mysql = pymysql.connect(mysql_test.addr, mysql_test.account, mysql_test.psd, 'mall_test')
    cursor = db_mysql.cursor()
    foo_code = 'dbWEjtRt'
    sql = '''select id from product where code = '%s' ''' % foo_code
    cursor.execute(sql)
    foo_all = cursor.fetchall()
    print 'foo all:', foo_all
    foo_product_id = foo_all[0][0]
    print 'product id:', foo_product_id
    sql = ''' select attr_value from product_attribute where product_id = %s and attr_key_id = 27''' % foo_product_id
    cursor.execute(sql)
    foo_all = cursor.fetchall()
    print 'foo all attr:', foo_all
    foo_value = foo_all[0][0]
    print 'attr value:', foo_value
    sql = ''' update product_attribute set attr_value = '%s' where product_id = %s and attr_key_id = 6''' % (foo_value, foo_product_id)
    tmp = cursor.execute(sql)
    print 'dodo:', tmp
    foo_all = cursor.fetchall()
    print 'foo all update:', foo_all
    cursor.close()
    db_mysql.close()
    pass

def test_oracle():
    os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
    foo_dsn = cx_Oracle.makedsn(oracle_test.addr, oracle_test.port, oracle_test.sid)
    db_oracle = cx_Oracle.connect(oracle_test.account, oracle_test.psd, foo_dsn)
    cursor = db_oracle.cursor()
    sql = ''' select code from eqs_scene_template where source_id = %s ''' % '58262'
    cursor.execute(sql)
    foo_all = cursor.fetchall()
    print foo_all
    foo_code = foo_all[0][0]
    print foo_code
    cursor.close()
    db_oracle.close()
    pass

def test_mongo():
    ''' datebase: scene_test
        table: eqs_scene_form '''
    client_mongo = mongo_client.MongoClient(mongo_test.addr, mongo_test.port)
    db_mongo = client_mongo[mongo_test.SCENE_TEST]
    foo_result = db_mongo[mongo_test.EQS_SCENE_FORM].find().skip(1).limit(2).sort('_id', -1)
    foo = foo_result[1]
    print type(foo)
    print foo
    foo = json.dumps(foo, ensure_ascii=False)
    print type(foo)
    print foo
    client_mongo.close()
    pass

def test_regexp():
    foo_scene_code = '4Wl7HIp6'
    url = 'http://h5.eqxiu.com/s/' + foo_scene_code
    headers = pro_header.headers
    h = httplib2.Http('.cache')
    _, cont = h.request(url, 'GET', headers=headers)
#     foo_all = re.search('var\s+scene\s+=\s+({.*?});', cont, flags=20)
    foo_all = re.search('<scripqt[^>]*>.*?var\s+scene\s+=\s+({.*?});\s+</script>', cont, flags=20)
    if foo_all and foo_all.group:
        print "YYYYY"
    else:
        print 'NNNNN'
    
#     headers = test_header.headers
    mm = backstage(headers)
    mobiles = '15011536587'
    title = 'GUESS'
    message = 'fantastic'
    mm.send_sms(headers, mobiles, title, message)
#     params = {'subject':'GUESS', 'message':'fantastic'}
#     payload = {'tid':'1006', 'mobiles':mobiles,
#                'params':json.dumps(params)}
#     url = 'http://postino.eqxiu.com/sms/send'
#     print json.dumps(params)
#     print urllib.urlencode(payload)
#     resp, cont = h.request(url, 'POST', urllib.urlencode(payload), headers)
#     print resp
#     print cont

def test_login():
    aa = user('pre')
    _, foo_header = aa.login('show@me.com', 'the')
    bb = session('pre')
    bb.unbind_third(foo_header, 'qq')
    ##############
    code = ''
    bb.bind_phone(foo_header, '15011536587', code, '111111')

def test_get_sms():
    aa = user('dev')
    _, foo_header = aa.login('admin', '1')
    bb = backstage(foo_header)
    foo = bb.get_sms_log_mobile(foo_header)
    foo_log_id = foo['rows'][0]['lid']
    joo = bb.get_sms_log(foo_header, foo_log_id)
    moo = joo['rows'][0]['content']
    qq = re.search('{code=(\w+)}', moo)
    print 'code is: %s' % qq.group(1)


if __name__ == '__main__':
#     test_upload()
#     test_mysql()
#     test_oracle()
#     test_mongo()
#     test_regexp()
#     test_login()
#     test_get_sms()
    pass