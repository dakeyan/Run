#!/usr/bin/python
#coding=utf-8

import httplib2
import json
import re
import time
from api import common
from api.scene.scene import scene
from api.scene.scene_create import scene_create
from api.scene.scene_get import scene_get
from api.scene.scene_save import scene_save
from api.scene.scene_set import scene_set
from api.scene.scene_upload import scene_upload
from api.user import user
from conf.parameter_db import account_psd
from conf.parameter_db import static_value
from conf.parameter_website import pro_prefix



def main(scenes_str, target_user):
    foo_input_str = scenes_str
    foo_input_user = target_user
    foo_input_list = foo_input_str.split(',')
    foo_output_list = []
    
    aa = user('test')
#     _, foo_header = aa.login(account_psd.account_apptpl, account_psd.psd_apptpl)
    _, foo_header = aa.login(account_psd.account_type1, account_psd.psd_type1)
    bb = scene(foo_header)
    cc = scene_create(foo_header)
    uu = scene_upload(foo_header)
    ss = scene_save(foo_header)
    gg = scene_get(foo_header)
    ee = scene_set(foo_header)
    
    for foo_code in foo_input_list:
        foo_code = foo_code.strip()
        foo_replace_map = {}
        foo_scene_info, foo_scene_setting = common.get_scene_info(foo_code)
        foo_content = common.get_scene_content(foo_scene_info['scene_id'], foo_code)
        
        foo_pic_list = common.get_pic_from_scene(foo_content)
        foo_pic_list.append(foo_scene_setting['cover']) if foo_scene_setting['cover'] else ''
        
        foo_audio_list = common.get_audio_from_scene(foo_content)
        foo_audio_list.append(foo_scene_info['bgaudio']) if foo_scene_info['bgaudio'] else ''
        ## 上传
        for foo_pic in foo_pic_list:
            url = pro_prefix.url_res + '/' + foo_pic
            _, cont = httplib2.Http().request(url, 'GET')
            foo_if_64 = re.findall('\.(.*)', foo_pic, re.I)
            if len(foo_if_64) > 0:
                foo_new_path = uu.upload_pic_7niu_function(foo_header, foo_pic, cont)
            else:
                foo_new_path = uu.upload_pic64_7niu_function(foo_header, cont)
            foo_replace_map[foo_pic] = foo_new_path['obj']['path'].encode('utf-8')
        for foo_audio in foo_audio_list:
            joo_audio = re.search('http:\/\/', foo_audio, re.I)
            if joo_audio:
                _, cont = httplib2.Http().request(foo_audio, 'GET')
            else:
                url = pro_prefix.url_res + '/' + foo_audio
                _, cont = httplib2.Http().request(url, 'GET')
            foo_new_path = uu.upload_audio_7niu_function(foo_header, foo_audio, cont)
            foo_replace_map[foo_audio] = foo_new_path['obj']['path'].encode('utf-8')
            if foo_audio == foo_scene_info['bgaudio']:
                foo_set_audio_id = foo_new_path['obj']['id']
                foo_set_audio_url = foo_new_path['obj']['path'].encode('utf-8')
                foo_set_audio_name = foo_new_path['obj']['path'].encode('utf-8')
        ## 替换
        for foo_key in foo_replace_map.keys():
            foo_content = re.sub(foo_key, foo_replace_map[foo_key], foo_content)
        if foo_scene_setting['cover']:
            foo_cover_old = foo_scene_setting['cover']
            foo_cover_new = foo_replace_map[foo_cover_old].encode('utf-8')
            foo_scene_setting['cover'] = re.sub(foo_cover_old, foo_cover_new, foo_scene_info['cover_ori'])
    
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
        
        if foo_scene_info['bgaudio']:
            foo_set_audio = {'id':foo_set_audio_id,
                             'url':foo_set_audio_url,
                             'name':foo_set_audio_name}
            foo_set_audio_str = json.dumps(foo_set_audio)
            ee.set_audio(foo_header, foo_set_audio_str, foo_new_scene_id)
        foo_scene_setting['id'] = foo_new_scene_id
        foo_scene_setting['name'] = foo_scene_info['scene_name']
        ss.save_setting(foo_header, foo_scene_setting)
        bb.publish(foo_header, foo_new_scene_id)
        foo_output_list.append(foo_new_scene_id)
    
    for foo_output in foo_output_list:
        bb.transfer_scene(foo_header, foo_output, foo_input_user)
    
    aa.logout(foo_header)
    print 'DONE'
    return foo_output_list

