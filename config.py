# -*- encoding:utf-8 -*-
#import configparser

import os
from Util import Properties

def getjiraUrl():
    properties  = getProperties()
    jiraUrl =  properties['url']
    return jiraUrl

def getUsername():
    properties = getProperties()
    username = properties['username']
    return username

def getPassword():
    properties = getProperties()
    password =  properties['password']

    return password


def getProperties():
    
    basedir = os.getcwd()   # 获取当前文件所在目录
    #print(basedir)
    configpath = os.path.join(basedir + '/config/config.properties')    # 获取config.properties文件所在目录
    #print(configpath)
    dictProperties = Properties(configpath).getProperties()     # 读取配置文件,字典形式返回文件内容
    return dictProperties
