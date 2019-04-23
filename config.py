# -*- encoding:utf-8 -*-
import configparser
import os
from Util import Properties
import logging

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

if __name__ == '__main__':
    r = getjiraUrl()
    current_path = os.getcwd()
    log_file = os.path.join(current_path + "/log/autotest.log")
    logging.basicConfig(level=logging.DEBUG,  # 控制台打印的日志级别
                        filename=log_file,
                        filemode='a',  ##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
                        # a是追加模式，默认如果不写的话，就是追加模式
                        format=
                        '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                        # 日志格式
                        )

    logging.info(r)


