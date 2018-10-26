#!/usr/bin/python
#coding=utf-8

import os
import sys

BASE_PATH = os.path.dirname(__file__)
sys.path.append(BASE_PATH)

if 'pro_scene_to_test_user' == sys.argv[1]:
    from tools import pro_scene_to_test_user
    pro_scene_to_test_user.main(sys.argv[2], sys.argv[3])
if 'pro_scene_to_pro_user' == sys.argv[1]:
    from tools import pro_scene_to_pro_user
    pro_scene_to_pro_user.main(sys.argv[2], sys.argv[3])
if 'pro_scene_to_test_app_tpl' == sys.argv[1]:
    from tools import pro_scene_to_test_app_tpl
    pro_scene_to_test_app_tpl.main(sys.argv[2])
if 'pro_scene_to_test_pc_tpl' == sys.argv[1]:
    from tools import pro_scene_to_test_pc_tpl
    pro_scene_to_test_pc_tpl.main(sys.argv[2])
if 'scene_check_pv_test' == sys.argv[1]:
    from tools import scene_check_pv_test
    scene_check_pv_test.main(sys.argv[2])
if 'login_test' == sys.argv[1]:
    from case import login_test
    login_test.main()
    
print '**** run finish ****'