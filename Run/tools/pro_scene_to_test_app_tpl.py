#!/usr/bin/python
#coding=utf-8

import cx_Oracle
import os
import pymysql
import time
from conf.parameter_db import (account_psd,
                               mysql_test,
                               oracle_test,
                               static_value)
from api import common
from api.max.max import backstage
from api.mall.mall_max import mall_max
from api.scene.scene import scene
from api.scene.scene_delete import scene_delete
from api.scene.scene_get import scene_get
from api.scene.scene_save import scene_save
from api.user import user
from tools import pro_scene_to_test_user


def main(scenes_str):
    foo_list = pro_scene_to_test_user.main(scenes_str, account_psd.account_apptpl)
    
    aa = user('test')
    _, foo_header = aa.login(account_psd.account_apptpl, account_psd.psd_apptpl)
    bb = scene(foo_header)
    dd = scene_delete(foo_header)
    ss = scene_save(foo_header)
    gg = scene_get(foo_header)
    
    joo_list = []
    for foo_id in foo_list:
        foo_copied_scene = bb.copy_scene_emodel2(foo_header, foo_id)
        foo_copied_scene_id = foo_copied_scene['obj']
        joo_list.append(foo_copied_scene_id)
        
        foo_setting = gg.get_scene_setting(foo_header, foo_id)
        _, foo_new_setting = common.get_scene_info(foo_setting['obj']['code'], 'test')
        foo_new_setting['id'] = foo_copied_scene_id
        ss.save_setting(foo_header, foo_new_setting)
        
        bb.publish(foo_header, foo_copied_scene_id)
        bb.apply_app_tpl(foo_header, foo_copied_scene_id)
        dd.delete_scene(foo_header, foo_id)
    aa.logout(foo_header)

    cc = user('test')
    _, joo_header = cc.login(account_psd.account_admin, account_psd.psd_admin)
    mm = backstage(joo_header)
    ll = mall_max(joo_header)
    for joo_id in joo_list:
        mm.pass_tpl(joo_header, joo_id, 3, 1)
        time.sleep(static_value.SLEEP_3)
        mm.pass_tpl(joo_header, joo_id, 3, 2)
        time.sleep(static_value.SLEEP_3)
    ll.update_index(joo_header)
    cc.logout(joo_header)
    print 'DONE'

def get_tpl_code(source_scene_id):
    os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
    foo_dsn = cx_Oracle.makedsn(oracle_test.addr, oracle_test.port, oracle_test.sid)
    db_oracle = cx_Oracle.connect(oracle_test.account, oracle_test.psd, foo_dsn)
    cursor = db_oracle.cursor()
    sql = ''' select code from eqs_scene_template where source_id = %s ''' % source_scene_id
    cursor.execute(sql)
    foo_all = cursor.fetchall()
    print foo_all
    cursor.close()
    db_oracle.close()
    return foo_all[0][0]

def replace_scene_cover(foo_list):
    db_mysql = pymysql.connect(mysql_test.addr, mysql_test.account, mysql_test.psd)
    cursor = db_mysql.cursor()
    for foo_code in foo_list:
        sql = '''select id from product where code = '%s' ''' % foo_code
        cursor.execute(sql)
        foo_all = cursor.fetchall()
        foo_product_id = foo_all[0][0]
        sql = ''' select attr_value from product_attribute where product_id = %s and attr_key_id = 27 ''' % foo_product_id
        cursor.execute(sql)
        foo_all = cursor.feetchall()
        foo_value = foo_all[0][0]
        sql = ''' update product_attribute set attr_value = '%s' where product_id = %s and attr_key_id = 6 ''' % (foo_value, foo_product_id)
        cursor.execute(sql)
    cursor.close()
    db_mysql.close()
