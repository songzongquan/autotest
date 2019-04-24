# -*- encoding:utf-8 -*-

import os
from Util import Properties
import logging

logger = logging.getLogger("main.config")
def getConfig():
	
    basedir = os.getcwd()   # 获取当前文件所在目录
    logger.debug("获取当前文件所在的目录:",basedir)
    configpath = os.path.join(basedir + '/config/config.properties')    # 获取config.properties文件所在目录
    logger.debug("获取config.properties文件所在目录:",configpath)
    dictProperties = Properties(configpath).getProperties()     # 读取配置文件,字典形式返回文件内容
    logger.debug("字典形式返回配置文件内容:",str(dictProperties))
    return dictProperties

def getjiraUrl():
    properties = getConfig()
    logger.debug("在getjiraUrl方法中，字典形式返回配置文件内容:",str(properties))
    jiraurl = properties["url"]
    return jiraurl

def getUsername():
    properties = getConfig()
    username = properties["username"]
    return username

def getPassword():
    properties = getConfig()
    password = properties["password"]
    return password

if __name__ == '__main__':
    r = getjiraUrl()
    x = getUsername()
    y = getPassword()
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
    logging.info(x)
    logging.info(y)

