#coding: utf-8

class test_prefix(object):
    header_origin = 'http://www.yqxiu.cn'
    url         = 'http://www.yqxiu.cn'
    url_as      = 'http://test.yqxiu.cn'
    url_h5      = 'http://h5.yqxiu.cn'
    url_m1      = 'http://m1.yqxiu.cn'
    url_max     = 'http://max.yqxiu.cn'
    url_open    = 'http://open.yqxiu.cn'
    url_postino = 'http://postino.eqshow.cn'
    url_res     = 'http://test.res.eqh5.com'
    url_res1    = 'http://7xrzj5.com1.z0.glb.clouddn.com'
    url_res2    = 'http://7xrzj5.com2.z0.glb.clouddn.com'
    url_s       = 'http://service.yqxiu.cn'
    url_s1      = 'http://s1.yqxiu.cn'
    url_s2      = 'http://s2.yqxiu.cn'
    url_s3      = 'http://s3.yqxiu.cn'
    url_search  = 'http://search.yqxiu.cn'
    url_v       = 'http://vservice.yqxiu.cn'

class pro_prefix(object):
    header_origin = 'http://www.eqxiu.com'
    url         = 'http://www.eqxiu.com'
    url_as      = 'http://as.eqxiu.com'
    url_h5      = 'http://h5.eqxiu.com'
    url_m1      = 'http://m1.eqxiu.com'
    url_max     = 'http://max.eqxiu.com'
    url_open    = 'http://open.eqxiu.com'
    url_postino = 'http://postino.eqxiu.com'
    url_res     = 'http://res.eqh5.com'
    url_res1    = 'http://res1.eqh5.com'
    url_res2    = 'http://res2.eqh5.com'
    url_s       = 'http://service.eqxiu.com'
    url_s1      = 'http://s1-cdn.eqxiu.com'
    url_s2      = 'http://s2.eqxiu.com'
    url_s3      = 'http://s3.eqxiu.com'
    url_search  = 'http://search.eqxiu.com'
    url_v       = 'http://vservice.eqxiu.com'

class dev_prefix(object):
    header_origin = 'http://www.eqshow.cn'
    url_max     = 'http://max.eqshow.cn'
    url_s       = 'http://max.eqshow.cn'

class pre_prefix(object):
    header_origin = 'http://www.eqxiu.cc'
    url_s       = 'http://service.eqxiu.cc'

class test_header(object):
    headers = {'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
               'connection':'keep-alive',
               'cache-control':'no-cache, no-store, max-age=0',
               'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
               'Origin':'http://www.yqxiu.cn'
               }

class dev_header(object):
    headers = {'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
               'connection':'keep-alive',
               'cache-control':'no-cache, no-store, max-age=0',
               'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
               'Origin':'http://www.eqshow.cn'
               }

class pre_header(object):
    headers = {'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
               'connection':'keep-alive',
               'cache-control':'no-cache, no-store, max-age=0',
               'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
               'Origin':'http://www.eqxiu.cc'
               }

class pro_header(object):
    headers = {'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
               'connection':'keep-alive',
               'cache-control':'no-cache, no-store, max-age=0',
               'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
               'Origin':'http://www.eqxiu.com'
               }
    
class suffix(object):
    time_line = '?1=1&from=timeline&isappinstalled=0&ad=1'
    group_msg = '?1=1&from=groupmessage&isappinstalled=0&ad=2'
    single_msg = '?1=1&from=singlemessage&isappinstalled=0&ad=2'

class qiniu_prefix(object):
    url_7niu = 'http://upload.qiniu.com'
    url_7niu_64 = 'http://up.qiniu.com/putb64/-1/'

