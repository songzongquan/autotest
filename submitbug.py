##!/usr/bin/python
# -*- coding: UTF-8 -*-

from login import *
import json

''' 输入s指的是login()返回的s，summary为提交的bug的主题，description为提交的bug的描述，返回bug的key值'''
def submitbug(s,summary, description):

    url = "https://code.bonc.com.cn/jira/rest/api/2/issue"

    payload=json.dumps({"fields": {"summary": summary,"issuetype": {"id": "1"},"components": [{"id": "11952"}],"project": {"id": "12017"},"description": description}})
    ''' 调用login中的post方法'''
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
    submitbug(s,'summary','description')