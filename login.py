##!/usr/bin/python
# -*- coding: UTF-8 -*-
#引用时请使用 'from login import *',即可直接调用函数名
import requests


'''登录，输入用户名和密码，返回session,此session具有request的所有的函数，
如果下面包装的方法不够用，你可以直接用s来调用相关的函数;'''
def login(username,password):
    s = requests.Session()
    s.auth = (username,password)
    return s
''' 请求url，返回文本,输入s指的是login()返回的s，params为字典类型,如{'key1':'value1','key2':'value2'} '''
def getText(s,url,params=None):
    r =  s.get(url,params=params)
    return r.text
''' 和getText类似，只是返回的是json对象 '''
def getJson(s,url,params=None):
    r = s.get(url,params=params)
    return r.json()
''' post提交，data 是字典类型,如{'key1':'value1','key2':'value2'}'''
def post(s,url,data=None):
    headers={"Accept": "application/json","Content-Type": "application/json"}
    s.headers.update(headers)
    r = s.post(url,data=data)
    return r.text
'''
这里将实现一个公用的按url下载文件的函数
url: 远程地址
target: 本地保存路径,注意包含文件名
'''
def downloadFile(s,url,target):
    r = s.get(url)
    f = open(target,'wb')
    for chunk in r.iter_content(100000):
        f.write(chunk)

    f.close()


'''
将文件上传到指定的服务地址
url:文件上传服务地址
source:本地源文件路径
'''
def uploadFile(s,url,source):
   # files = [('images',('foo.jpeg',open(source,'rb'),'image/jpeg')),('images',('bar.jpeg',open(source,'rb'),'image/jpeg'))]
    headers ={"X-Atlassian-Token": "no-check"}

    s.headers.update(headers)
    files = {'file':open(source,'rb')}
    r = s.post(url,files=files)
    return r.text






