# coding:utf-8
# !/usr/bin/env python
# coding:utf-8
# @Date    : 2017-03-01 12:38:38
# @Author  : Smile Hu (smile.hu@sap.com)
# @Link    : http://www.smilehu.com

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import json
import requests
from time import sleep

headers_default = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/44.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive'
}

# 请定义你想要的reponse是什么样子的
def isGetWantedResponse(response):
    try:
        if response.status_code == 200:
            print '* [Good response]'
            sleep(2)
            return True
        else:
            print '* [Bad response]'
            return False
    except:
        print '* [Error response]'
        return False

def isPostWantedResponse(response):
    try:
        if 'Key' in response or 'Count' in response:
            print '* [Good response]'
            sleep(2)
            return True
        else:
            print '* [Bad response]'
            return False
    except:
        print '* [Error response]'
        return False

def getTheBestProxiesAndIp():
    try:
        r = requests.get('http://127.0.0.1:7999/?count=1', timeout=5)
    except requests.exceptions.ConnectionError as e:
        raise Exception('多半是没有开启IPProxy服务哦~：', e)

    ip_ports = json.loads(r.text)
    if len(ip_ports)==0 or r.text=='[]':
        print '没有IP代理啦啦啦啦啦啦啦啦啦！'
        raise Exception('IP代理池里面没有代理啦或者出错啦', r)
    print "【代理】获取代理: ", ip_ports

    ip = ip_ports[0][0]
    port = ip_ports[0][1]
    proxies = {
        'http': 'http://%s:%s' % (ip, port),
        'https': 'http://%s:%s' % (ip, port)
    }

    return proxies,ip

def getCurrentIp():
    try:
        r = requests.get('http://127.0.0.1:7999/?count=1', timeout=5)
    except requests.exceptions.ConnectionError as e:
        raise Exception('多半是没有开启IPProxy服务哦~：', e)

    ip_ports = json.loads(r.text)
    if len(ip_ports)==0 or r.text=='[]':
        print '没有IP代理啦啦啦啦啦啦啦啦啦！'
        ip = '0'
        raise Exception('IP代理池里面没有代理啦或者出错啦', r)
    else:ip = ip_ports[0][0]
    return ip

def deleteProxies(ip):
    print '【代理】删除代理：',ip
    r = requests.get('http://127.0.0.1:7999/delete?ip='+ip)

def postWithProxies(url, postdata, isDeleteProxies=False, headers=headers_default, timeout=10):
    print '【代理】post 开始用 proxies 进行处理'
    try:
        if isDeleteProxies: deleteProxies(getCurrentIp())
        proxies, ip = getTheBestProxiesAndIp()
        response = requests.post(url=url, data=postdata, proxies=proxies, headers=headers, timeout=timeout)
        print '【代理】post 代理的 response:  ', response
        return response
    except Exception as e:
        print '【代理】出现错误：', e
        deleteProxies(getCurrentIp())
        return ''

def getWithProxies(url,isDeleteProxies=False, headers=headers_default, timeout=10):
    print '【代理】get 开始用 proxies 进行处理'
    try:
        if isDeleteProxies: deleteProxies(getCurrentIp())

        proxies, ip = getTheBestProxiesAndIp()
        response = requests.get(url=url, proxies=proxies, headers=headers, timeout=timeout)
        print '【代理】get 代理的 response:  ', response
        return response
    except Exception as e:
        print '【代理】出现错误：', e
        deleteProxies(getCurrentIp())
        return ''


# 输入：url, postdata
# 输出：response
# 首先不用代理取出reponse, 判断是否为自己想要的
# 如果不是想要的，就用代理解决，直到拿到自己想要的response
def post(url, data, headers=headers_default, timeout=10):
    print '********************************** post begein **********************************'

    # 首先不用代理取出reponse
    response = requests.post(url=url, data=data, headers=headers, timeout=timeout).text
    print '*【原生】post 不用代理的 response:  ', response

    i = 1
    # 判断返回的结果是不是自己想要的
    while not isPostWantedResponse(response):
        print '【代理】---------------------'
        print '【代理】尝试代理次数：',i
        if i==1:
            response = postWithProxies(url, data,isDeleteProxies=False, headers=headers, timeout=timeout)
        else:
            response = postWithProxies(url, data, isDeleteProxies=True, headers=headers, timeout=timeout)

        i = i +1

    print '*********************************** post end **********************************'
    return response

def get(url, headers=headers_default, timeout=10):
    print '********************************** get begein **********************************'

    # 首先不用代理取出reponse
    response = requests.get(url=url, headers=headers, timeout=timeout)
    print '*【原生】get 不用代理的 response:  ', response.status_code

    i = 1
    # 判断返回的结果是不是自己想要的
    while not isGetWantedResponse(response):
        print '【代理】---------------------'
        print '【代理】尝试代理次数：',i
        if i==1:
            response = getWithProxies(url, isDeleteProxies=False, headers=headers, timeout=timeout)
        else:
            response = getWithProxies(url, isDeleteProxies=True, headers=headers, timeout=timeout)

        i = i +1

    print '*********************************** get end **********************************'
    return response