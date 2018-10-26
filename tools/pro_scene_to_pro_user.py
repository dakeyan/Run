#!/usr/bin/python
#coding=utf-8

import json
import time
from api import common
from api.scene.scene import scene
from api.scene.scene_create import scene_create
from api.scene.scene_get import scene_get
from api.scene.scene_save import scene_save
from api.scene.scene_set import scene_set
from api.user import user
from conf.parameter_db import account_psd_pro
from conf.parameter_db import static_value

def main(scenes_str, target_user):
    foo_input_str = scenes_str
    foo_input_user = target_user
    foo_input_list = foo_input_str.split(',')
    foo_output_list = []
    
    aa = user('pro')
    _, foo_header = aa.login(account_psd_pro.account_show, account_psd_pro.psd_show)
    bb = scene(foo_header)
    cc = scene_create(foo_header)
    ss = scene_save(foo_header)
    gg = scene_get(foo_header)
    ee = scene_set(foo_header)
    
    for foo_code in foo_input_list:
        foo_code = foo_code.strip()
        foo_scene_info, foo_scene_setting = common.get_scene_info(foo_code)
        foo_content = common.get_scene_content(foo_scene_info['scene_id'], foo_code, foo_scene_info['publish_time'])
        
    
        foo_content_json = json.loads(foo_content, encoding='utf8')
        
        foo_new_scene = cc.create_scene(foo_header, scene_name=foo_scene_info['scene_name'])

        foo_new_scene_id = foo_new_scene['obj']
        foo_page = gg.get_page_list(foo_header, foo_new_scene_id)
        foo_page_id = foo_page['list'][0]['id']
        
        i = len(foo_content_json['list'])
        for joo in foo_content_json['list']:
            joo['id'] = foo_page_id
            joo['sceneId'] = foo_new_scene_id
            ss.save(foo_header, joo)
            if joo['name']:
                foo_page_name = joo['name'].encode('utf-8')
                ss.save_page_name(foo_header, foo_page_id, foo_new_scene_id, foo_page_name)
            i -= 1
            if i > 0:
                foo_page = bb.copy_page(foo_header, foo_page_id)
                foo_page_id = foo_page['obj']['id']
            time.sleep(static_value.SLEEP_0_5)
        
        if foo_scene_info['bgaudio_ori']:
            foo_set_audio_str = json.dumps(foo_scene_info['bgaudio_ori'])
            ee.set_audio(foo_header, foo_set_audio_str, foo_new_scene_id)
        foo_scene_setting['id'] = foo_new_scene_id
        foo_scene_setting['name'] = foo_scene_info['scene_name']
        foo_scene_setting['cover'] = foo_scene_info['cover_ori']
        ss.save_setting(foo_header, foo_scene_setting)
        bb.publish(foo_header, foo_new_scene_id)
        foo_output_list.append(foo_new_scene_id)
    
    for foo_output in foo_output_list:
        bb.transfer_scene(foo_header, foo_output, foo_input_user)
    
    aa.logout(foo_header)
    print 'DONE'
    return foo_output_list
