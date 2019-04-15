#!/usr/bin/python
# -*- coding: UTF-8 -*-

from login import *

s = login('songzongquan','000000')

r = getText(s,'https://code.bonc.com.cn/jira/rest/api/2/project')

print(r)

downloadFile(s,'https://code.bonc.com.cn/jira/secure/thumbnail/24269/_thumb_24269.png','/home/song/_thumb_24269.png')


