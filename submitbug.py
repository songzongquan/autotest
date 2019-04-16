##!/usr/bin/python
# -*- coding: UTF-8 -*-

from login import *
import requests
import json

def submitbug(s,summary, description):

    url = "https://code.bonc.com.cn/jira/rest/api/2/issue"

    headers={"Accept": "application/json","Content-Type": "application/json"}

    payload=json.dumps({"fields": {"summary": summary,"issuetype": {"id": "1"},"components": [{"id": "11952"}],"project": {"id": "12017"},"description": description}})


    r= post(s,url,data=payload)


    print(r)

if __name__ == '__main__':
    s = login('lixiaofan', 'Lixiaofan123!')
    submitbug(s,'summary','description')