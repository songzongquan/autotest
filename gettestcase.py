# -*- coding: UTF-8 -*-

from login import *
import requests
from config import *
import os
import logging
'''
根据测试循环id查询测试用例的附件，返回附件id与文件名
'''
def gettestcase(s,cycleId):

    logger = logging.getLogger("main.gettestcase")

    r = getjiraUrl()
    url=os.path.join(r+'rest/zapi/latest/execution')#接口
    url2=os.path.join(r+'rest/api/2/issue')
    params = {'action':'expand','cycleId':cycleId}
    r = getJson(s,url,params)               #这个接口下的所有测试用例字典

    issues= r['executions'] #这个接口下的所有测试用例字典下所有executions字典
    result = []     #返回结果，元素是一个{id:filename}形式的字典
    for x in issues:                         #在executions字典中每找到一个issueId,就拼接url
       issueId = x['issueId']
       issue = getJson(s, url2 + '/' + str(issueId), None)
       attachments = issue['fields']['attachment']    #字典
       for attachment in attachments:                 #list
           id = attachment['id']
           filename = attachment['filename']
           logger.debug("这是附件的id："+id)
           logger.debug("这是附件的filename："+filename)
           if ".py" in filename:
               e ={"id":id,"filename":filename}
               result.append(e)
    logger.debug("这是附件的字典信息"+str(result))
    
    return result



if __name__ == '__main__':
    s = login('lixiaofan', 'Lixiaofan123!')
    r = gettestcase(s,33)
    print(r)

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

