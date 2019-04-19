##!/usr/bin/python
# -*- coding: UTF-8 -*-

from login import *
import json
from config import *

''' 输入s指的是login()返回的s，summary为提交的bug的主题，description为提交的bug的描述，返回bug的key值,componetsid为用例所属的模块的id，projectid为用例所属项目的id，versionid为用例所属版本的id'''
def submitbug(s,summary, description,componentid,projectid,versionid):

    path=getjiraUrl()
    # print(path)
    url = path+ 'rest/api/2/issue'
    print(url)

    payload=json.dumps({"fields": {"summary": summary,"issuetype": {"id": "1"},"components": [{"id": componentid}],"project": {"id": projectid},"description": description,"customfield_11303":[{"id":versionid}]}})

    r= post(s,url,data=payload)
    print(r)
    ''' 返回提交的bug对应的key值'''
    dict=json.loads(r)
    print(dict)
    key=dict.get("key")
    print(key)
    return(key)

if __name__ == '__main__':
    s = login('lixiaofan', 'Lixiaofan123!')
    submitbug(s,'summary','description','12327','12106','12003')