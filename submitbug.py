##!/usr/bin/python
# -*- coding: UTF-8 -*-

from login import *
import json
from config import *
from log import *

# 输入s指的是login()返回的s，summary为提交的bug的主题，description为提交的bug的描述，返回bug的key值,componetsid为用例所属的模块的id，projectid为用例所属项目的id，versionid为用例所属版本的id

sub_logger = logging.getLogger("main.submitbug")
def submitbug(s,summary, description,componentid,projectid,versionid):

    path=getjiraUrl()
    url = path+ 'rest/api/2/issue'

    sub_logger.debug("jira:CREATE ISSUE接口的url：",url)

    payload=json.dumps({"fields": {"summary": summary,"issuetype": {"id": "1"},"components": [{"id": componentid}],"project": {"id": projectid},"description": description,"customfield_11303":[{"id":versionid}]}})

    r= post(s,url,data=payload)
    # print(r)
    sub_logger.debug("jira:CREATE ISSUE接口的返回的text格式内容：",r)
    ''' 返回提交的bug对应的key值'''
    dict=json.loads(r)
    # print(dict)
    sub_logger.debug("将text转换成json格式内容：", dict)
    key=dict.get("key")
    # print(key)
    sub_logger.debug("获取bug的key值：",key)
    return(key)



if __name__ == '__main__':
    s = login('lixiaofan', 'Lixiaofan123!')
    submitbug(s,'summary','description','12327','12106','12003')