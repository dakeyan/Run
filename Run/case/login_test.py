#!/usr/bin/python
#coding=utf-8

import cx_Oracle
import os
from api.login.login import session
from conf.parameter_db import oracle_test


# config_flag = 0



def set_configuration():
    os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
    foo_dsn = cx_Oracle.makedsn(oracle_test.addr, oracle_test.port, oracle_test.sid)
    db_oracle = cx_Oracle.connect(oracle_test.account, oracle_test.psd, foo_dsn)
    cursor = db_oracle.cursor()
#     sql = ''' select code from eqs_scene_template where source_id = %s ''' % '58262'
    sql = ''' update eqs_user set join_time = '', expiry_time = '' where login_name = 'mt8' '''
    cursor.execute(sql)
#     foo_all = cursor.fetchall()
#     print foo_all
#     foo_code = foo_all[0][0]
#     print foo_code
    cursor.close()
    db_oracle.close()

def check():
    a = session()
    _, foo_header = a.login('mt8', 'qqq321')
    foo_login = a.get_login_status(foo_header)
    if foo_login['code'] == 200:
        foo_obj = foo_login['obj']
        if not foo_obj['name'] == 'member8':
            print 'Error: wrong name'
        if not foo_obj['loginName'] == 'mt8':
            print 'Error: wrong loginName'
        if not foo_obj['email'] == 'member8@qq.cc':
            print 'Error: wrong email'
        if not foo_obj['type'] == 2:
            print 'Error: wrong type'
        if not foo_obj['id'] == '402879bb527662aa015276f14b6a0002':
            print 'Error: wrong id'
    else:
        print 'Error: get_login_status API failed'
    print 'Info: get_login_status: success'
    

def main():
    print '**** test start ****'
    check()
    print 'DONE'


# if __name__ == '__main__':
#     check()
#     print 'DONE'
