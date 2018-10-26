#coding: utf-8

class login_api(object):
    get_account_info    = '/account/info'
    get_captcha         = '/eqs/captcha'
    register_email      = '/eqs/email/register'
    register_email_code = '/eqs/email/register/code'
    register_phone      = '/eqs/phone/register'
    reset_password      = '/eqs/pwd/reset'  #nginx中显示，是给app 用的
    pwd_retrieve_email  = '/eqs/pwd/retrieve'
    pwd_retrieve_email_4app = '/eqs/pwd/retrieve4app'
    quick_login         = '/eqs/quick/login'
#     register            = '/eqs/register'
    register_code       = '/eqs/register/code'
    login               = '/login'
    login_qq_pc         = '/eqs/relAccount'
    login_mobile        = '/eqs/relAccountByMobile'
    login_wechat_pc     = '/eqs/relWechatAccount'
    login_dingding      = '/eqs/rel-account/dingding'
    login_wechatmp      = '/eqs/rel-account/wechat-mp'
    login_wechatqr      = '/eqs/rel-account/wechat-qr'
    login_weibo         = '/eqs/rel-account/weibo'
    reset_code_phone    = '/eqs/reset/code'
    get_sms_token       = '/eqs/sms/token'  #nginx中显示，给app 用
    get_login_status    = '/login/status'
    modify_password     = '/m/base/user/changePwd'
    bind_phone_code1    = '/m/u/bind/user/phone'  #nginx 中显示，会跳转到 /user/bind/phone/code
    bind_phone1         = '/m/u/phone/verify'  #nginx 中显示，会跳转到 /user/bind/phone
    unbind_third1       = '/m/u/unRelation'  #nginx 中显示，会跳转到 /user/unbind/third
    reset_pwd_email     = '/pwd/reset/email'
#     bind_phone          = '/user/bind/phone'
#     bind_phone_code     = '/user/bind/phone/code'
    bind_thrid          = '/user/bind/third'
    merge_user          = '/user/merge'
#     unbind_third        = '/user/unbind/third'

class mall_api(object):
    publish_product     = '/m/mall/product/publish'
    revoke_product      = '/m/mall/product/unpublish'
    update_index        = '/m/mall/product/updateIndex'

class max_api(object):
    pass_tpl            = '/m/scene/apply/check'
    sms_log             = '/m/sms/log/list.json'
    sms_log_mobile      = '/m/sms/log/mobile/list.json'
    send_sms            = '/sms/send'

class scene_api(object):
    get_7niu_token      = '/m/base/file/uptokens'
    save_file           = '/m/base/file/info/save'
    apply_app_tpl       = '/m/e/scene/new/tpl/apply'
    save_audio_cut      = '/m/scene/audio/cut/save'
    set_audio           = '/m/scene/audio/set'
    audio_status        = '/m/scene/audio/status'
    audio_cut           = '/m/scene/audio/transfer'
    copy_scene          = '/m/scene/copyScene'
    create_scene        = '/m/scene/create'
    create_scene_tpl    = '/m/scene/createByTpl'
    create_page         = '/m/scene/createPage'
    delete_scene        = '/m/scene/delete'
    get_scene_setting   = '/m/scene/detail'
    get_scene_list      = '/m/scene/my'
    save_page_ctpl      = '/m/scene/page/companytpl/save'
    save_page_tpl       = '/m/scene/page/mytpl/save'
    page_list           = '/m/scene/pageList'
    publish             = '/m/scene/publish'
    save                = '/m/scene/save'
    save_pagename       = '/m/scene/savePage'
    save_setting        = '/m/scene/setting/save'
    transfer_scene      = '/m/scene/transfer'
    
class user_api(object):
    login               = '/login'
    logout              = '/logout'

class view_api(object):
    get_template        = '/s'
    get_page            = '/eqs/page'