##!/usr/bin/python
# -*- coding: UTF-8 -*-

from login import *
# import requests
import json

def submitbug(s,summary, description):
    url = "https://code.bonc.com.cn/jira/rest/api/2/issue"

    headers = {"Accept": "application/json","Content-Type": "application/json"}

    payload = {'project': {'id': '12017'}, 'issuetype': {'name': u'缺陷'}, 'components': {'name':u'99-其他'}}
               #'assignee': {'name': 'lixiaofan'}, 'summary': summary,'description': description,'priority': {'name': u'重要'}, 'customfield_11303': [{'name': "base_1.0"}]}

    response = s.request("POST", url, data=payload,headers=headers)

    print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

if __name__ == '__main__':
    s = login('lixiaofan', 'Lixiaofan123!')
    submitbug(s,'summary','description')