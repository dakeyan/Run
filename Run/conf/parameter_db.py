#coding: utf-8

class mysql_test(object):
    addr = 'mysql.yqxiu.cn'
    account = 'root'
    psd = 'eqs123'

class oracle_test(object):
    addr = 'test.db.yqxiu.cn'
    account = 'eqxiu_test'
    psd = 'keqs789'
    port = '1521'
    sid = 'oragbk'

class mongo_test(object):
    addr = 'mdb.yqxiu.cn'
    port = 27010
    SCENE_TEST = 'scene_test'
    EQS_SCENE_FORM = 'eqs_scene_form'

class oracle_dev(object):
    addr = 'test.db.yqxiu.cn'
    account = 'eqxiu_dev'
    psd = 'keqs123'
    port = '1521'
    sid = 'oragbk'

class static_value(object):
    LOOP_10 = 10
    SLEEP_2 = 2
    SLEEP_3 = 3
    SLEEP_0_5 = 0.5

class account_psd(object):
    account_type1   = 'show0428@me.com'
    psd_type1       = 'the'
    account_tpye2   = 'show@me.com'
    psd_type2       = '111111'
    account_type4   = 'show04282@me.com'
    psd_type4       = 'the'
    account_apptpl  = 'apptpl'
    psd_apptpl      = 'eqxiu'
    account_tpl     = 'tpl'
    psd_tpl         = 'eqxiu'
    account_admin   = 'admin'
    psd_admin       = '992qwe'

class account_psd_pro(object):
    account_show    = 'show@me.com'
    psd_show        = 'the'
    account_type1   = 'show0429@me.com'
    psd_type1       = 'the'
    account_type4   = 'show04292@me.com'
    psd_type4       = 'the'

class account_psd_dev(object):
    account_admin   = 'admin'
    psd_admin       = '1'