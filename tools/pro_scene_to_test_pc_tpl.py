#!/usr/bin/python
#coding=utf-8

import time
from conf.parameter_db import account_psd
from conf.parameter_db import static_value
from api.max.max import backstage
from api.mall.mall_max import mall_max
from api.scene.scene import scene
from api.user import user
from tools import pro_scene_to_test_user


def main(scenes_str):
    foo_list = pro_scene_to_test_user.main(scenes_str, account_psd.account_tpl)
    
    aa = user('test')
    _, foo_header = aa.login(account_psd.account_tpl, account_psd.psd_tpl)
    bb = scene(foo_header)
    for foo_id in foo_list:
        bb.apply_app_tpl(foo_header, foo_id, 5, '企业用途', 36, '年会', 0)
    aa.logout(foo_header)

    cc = user('test')
    _, joo_header = cc.login(account_psd.account_admin, account_psd.psd_admin)
    mm = backstage(joo_header)
    ll = mall_max(joo_header)
    for joo_id in foo_list:
        mm.pass_tpl(joo_header, joo_id, 3, 1)
        time.sleep(static_value.SLEEP_3)
        mm.pass_tpl(joo_header, joo_id, 3, 2)
        time.sleep(static_value.SLEEP_3)
    ll.update_index(joo_header)
    cc.logout(joo_header)
    print 'DONE'
