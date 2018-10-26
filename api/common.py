#coding: utf-8

import httplib2
import json
import random
import re
import string
import time
from conf.parameter_website import pro_prefix
from conf.parameter_website import test_prefix
from conf.parameter_website import pro_header
from conf.parameter_website import test_header
from conf.api_link import view_api


def decimal_2_x(decimal, x=10):
    '''
    Description: decimal to x
    decimal: [0, n]
    x: [2, 62]
    '''
    if decimal < 0:
        print 'Error: bad decimal'
        return ''
    if x < 2:
        print 'Error: bad x'
        return ''
    foo_dec = decimal
    foo_x = (x-1) % 62 + 1
    foo_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
               'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
               'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
               'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
               'U', 'V', 'W', 'X', 'Y', 'Z']
    foo_out = []
    while foo_dec > foo_x:
        foo_out.append(foo_list[foo_dec%foo_x])
        foo_dec = foo_dec / foo_x
    foo_out.append(foo_list[foo_dec])
    foo_out.reverse()
    return ''.join(foo_out)

def get_7niu_key():
    foo = 'o_'
    foo += decimal_2_x(long(time.time()*1000), 32)
    for _ in xrange(5):
        foo += decimal_2_x(random.randint(0, 65535), 32)
    return foo

def get_audio_from_scene(scene_content):
    upload_list = []
    foo_all_audio = re.findall('[^"\']*?\.(?:mp3)', scene_content, re.I)
    for poo in foo_all_audio:
        poo = re.sub('"', '', poo)
        upload_list.append(poo)
    return upload_list

def get_ext_name(file_ame):
    foo = str(file_ame).strip()
    joo = re.search('.*\.(jpg|jpeg|gif|png|svg|mp3|html|md|doc|c|htm|txt)', foo, re.I)
    if joo:
        return joo.group(1).lower()
    else:
        print 'Error: get_ext_name: get ext name failed:', foo
    return ''

def get_pic_from_scene(scene_content):
    upload_list = []
    foo_scene_json = json.loads(scene_content, encoding='utf8')
    
    for doo in foo_scene_json['list']:
        if doo.has_key('elements') and doo['elements']:
            for dudu in doo['elements']:
                if dudu['type'] == 4 or dudu['type'] == '4':
                    if dudu['properties'].has_key('originSrc') and dudu['properties']['originSrc']:
                        eoo = dudu['properties']['originSrc']
                    elif dudu['properties'].has_key('src') and dudu['properties']['src']:
                        eoo = dudu['properties']['src']
                        eoo = eoo.replace('\?.*', '')
                    else:
                        continue
                elif dudu['type'] == 3 or dudu['type'] == '3':
                    if dudu['properties'].has_key('originSrc') and dudu['properties']['originSrc']:
                        eoo = dudu['properties']['originSrc']
                    elif dudu['properties'].has_key('imgSrc') and dudu['properties']['imgSrc']:
                        eoo = dudu['properties']['imgSrc']
                        eoo = eoo.replace('\?.*', '')
                    else:
                        continue
                elif dudu['type'] == 'h':
                    if dudu['properties'].has_key('src') and dudu['properties']['src']:
                        eoo = dudu['properties']['src']
                        eoo = eoo.replace('\?.*', '')
                    else:
                        continue
                else:
                    continue
                if eoo not in upload_list:
                    upload_list.append(eoo)
        if doo.has_key('properties') and doo['properties']:
            if doo['properties'].has_key('thumbSrc') and doo['properties']['thumbSrc']:
                eoo = doo['properties']['thumbSrc']
                eoo = eoo.replace('\?.*', '')
                if eoo not in upload_list:
                    upload_list.append(eoo)
    return upload_list

def get_random_string(length):
    foo = string.ascii_letters + string.digits
    return ''.join(random.choice(foo) for _ in xrange(length))

def get_scene_info(code, server_type='pro'):
    '''
    scene_setting['cover']: 不含裁切参数的图片，类型 str
    scene_info['cover_ori']: cover原始内容，类型str
    scene_setting['bgaudio']: url参数对应的音频文件，类型str
    scene_info['bgaudio_ori']: bgaudio原始内容，类型dict
    '''
    scene_setting = {}
    scene_info = {}
    if server_type == 'pro':
        url = pro_prefix.url_h5 + view_api.get_template + '/' + code
        headers = pro_header.headers
    elif server_type == 'test':
        url = test_prefix.url_h5 + view_api.get_template + '/' + code
        headers = test_header.headers
    _, cont = httplib2.Http('.cache').request(url, 'GET', headers=headers)
#     foo_all = re.search('<script[^>]*>.*?var\s+scene\s+=\s+({.*?});\s+</script>', cont, flags=20)
    foo_all = re.search('var\s+scene\s+=\s+({.*?});', cont, flags=20)
    foo_info = foo_all.group(1)
    foo_scene_id = re.search('id:\s*(\d+)', foo_info, re.I).group(1)
    foo_scene_name = re.search('name:\s*"([^"]+)"', foo_info, re.I).group(1)
    foo_scene_publish_time = re.search('publishTime:\s*(\d+)', foo_info, re.I).group(1)

    scene_info['scene_id'] = foo_scene_id
    scene_info['scene_name'] = foo_scene_name
    scene_info['publish_time'] = foo_scene_publish_time
    scene_setting['id'] = foo_scene_id
    scene_setting['name'] = foo_scene_name

    joo_auto_flip = re.search('\"autoFlip\":(true|false)', foo_info, re.I)
    foo_auto_flip = joo_auto_flip.group(1) if joo_auto_flip else 'false'
    foo_flip_time = int(re.search('\"autoFlipTime\":(\d+)', foo_info, re.I).group(1))
    joo_cover_cut = re.search('cover:\s*"(([^"]+)\?[^"]+")', foo_info, re.I)
    joo_cover = re.search('cover:\s*"([^"]+)"', foo_info, re.I)
    if joo_cover_cut:
        foo_cover = joo_cover_cut.group(2)
        scene_info['cover_ori'] = joo_cover.group(1)
    else:
        foo_cover = joo_cover.group(1) if joo_cover else ''
        scene_info['cover_ori'] = joo_cover.group(1) if joo_cover else ''
        
    joo_description = re.search('description:\s*"([^"]*)"', foo_info, re.I)
    foo_description = joo_description.group(1) if joo_description else ''
    joo_forbid_hand_flip = re.search('\"\":(true|false)', foo_info, re.I)
    foo_forbid_hand_flip = joo_forbid_hand_flip.group(1) if joo_forbid_hand_flip else 'false'
    foo_page_mode = re.search('pageMode:\s*(\d+)', foo_info, re.I).group(1) 
    foo_slid_number = re.search('\"slideNumber\":(true|false)', foo_info, re.I).group(1)
    foo_triger_loop = re.search('\"triggerLoop\":(true|false)', foo_info, re.I).group(1)
    foo_scene_type = re.search('type:\s*(\d+),', foo_info).group(1)

    scene_setting['autoFlip'] = foo_auto_flip
    scene_setting['autoFlipTime'] = foo_flip_time
    scene_setting['cover'] = foo_cover
    scene_setting['description'] = foo_description
    scene_setting['forbidHandFlip'] = foo_forbid_hand_flip
    scene_setting['pageMode'] = foo_page_mode
    scene_setting['slideNumber'] = foo_slid_number
    scene_setting['status'] = 1
    scene_setting['triggerLoop'] = foo_triger_loop
    scene_setting['type'] = foo_scene_type

    ## 背景音乐有两种形式，一种是带大括号的，一种是不带大括号的
    joo_bgaudio_str = re.search('bgAudio:\s*"([^"]*)"', foo_info, re.I)
    joo_bgaudio_dict = re.search('bgAudio:\s*({[^\{\}]*}),', foo_info, re.I)
    if joo_bgaudio_str:
        foo_bgaudio = joo_bgaudio_str.group(1)
        scene_info['bgaudio_ori'] = {'url':foo_bgaudio}
    elif joo_bgaudio_dict:
        scene_info['bgaudio_ori'] = joo_bgaudio_dict.group(1)
        foo_bgaudio_json = json.loads(joo_bgaudio_dict.group(1), encoding='utf-8')
        foo_bgaudio = foo_bgaudio_json['url']
    else:
        foo_bgaudio = ''
        scene_info['bgaudio_ori'] = {}

    scene_info['bgaudio'] = foo_bgaudio
    return scene_info, scene_setting

def get_scene_content(scene_id, scene_code, publish_time, server_type='pro'):
    if server_type == 'pro':
        url = pro_prefix.url_s1 + view_api.get_page + '/' + scene_id + '?code=' + scene_code + '&time=' + publish_time
        headers = pro_header.headers
    elif server_type == 'test':
        url = test_prefix.url_s1 + view_api.get_page + '/' + scene_id + '?code=' + scene_code
        headers = test_header.headers
    headers['Origin'] = 'http://www.eqxiu.com'
    _, cont = httplib2.Http().request(url, 'GET', headers=headers)
#     print 'Debug: get_scene_content:', resp
#     print 'Debug: get_scene_content:', cont
    return cont

def get_upload_payload(boundary, key_7niu, token, file_name, file_buffer, ct='image/jpeg'):
    foo = []
    foo.append('--%s' % boundary)
    foo.append('Content-Disposition: form-data; name="name"')
    foo.append('')
    foo.append(key_7niu) 
    foo.append('--%s' % boundary)
    foo.append('Content-Disposition: form-data; name="chunk"')
    foo.append('')
    foo.append('0')
    foo.append('--%s' % boundary)
    foo.append('Content-Disposition: form-data; name="chunks"')
    foo.append('')
    foo.append('1')
    foo.append('--%s' % boundary)
    foo.append('Content-Disposition: form-data; name="key"')
    foo.append('')
    foo.append(key_7niu)
    foo.append('--%s' % boundary)
    foo.append('Content-Disposition: form-data; name="token"')
    foo.append('')
    foo.append(token)
    foo.append('--%s' % boundary)
    foo.append('Content-Disposition: form-data; name="file"; filename="%s"' % file_name)
    foo.append('Content-Type: %s' % ct)
    foo.append('')
    foo.append(file_buffer)
    foo.append('--%s--' % boundary)
    foo_str = []
    for fofo in foo:
        foo_str.append(str(fofo))
    return '\r\n'.join(foo_str)

def msecond_2_string(millisecond):
    if millisecond:
        if long == type(millisecond) or str == type(millisecond) or int == type(millisecond):
            try:
                joo = float(millisecond)
            except Exception, e:
                print 'Error: input value with exception: ', e
                return
            foo = joo/1000
            foo = '{0:.3f}'.format(foo)
            result = time.asctime(time.localtime(float(foo)))
            return result
        else:
            print 'Error: wrong type of input'
    else:
        print 'Error: millisecond input is NULLL'
    return ''

def response_2_json(resp, content):
    '''
    type(resp) = dict
    type(content) = str
    '''
    if resp.has_key('status') and '200' == resp['status']:
        if content:
            return json.loads(content, encoding='utf-8')
        else:
            print 'Warning: content is NULL'
            return {'success':True}
    else:
        print 'Warning: status in response is not 200:', resp
        return {'success':False}

def string_2_list(str_in):
    out_list = []
    if str == type(str_in):
        for i in str_in.split(','):
            out_list.append(i)
    else:
        print 'Error: type of input should be <str>'
    return out_list


