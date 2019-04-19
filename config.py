# -*- encoding:utf-8 -*-
import configparser
import os
from Util import Properties

def getjiraUrl():
    basedir = os.getcwd()   # 获取当前文件所在目录
    #print(basedir)
    configpath = os.path.join(basedir + '/config/config.properties')    # 获取config.properties文件所在目录
    #print(configpath)
    dictProperties = Properties(configpath).getProperties()     # 读取配置文件,字典形式返回文件内容
    #print(dictProperties)
    configurl = list(dictProperties.values())[0]        # 将字典形式的值转化为列表形式，返回列表的第一个元素
    #print(configurl)
    return configurl

