#!/usr/bin/python
# -*- coding: UTF-8 -*-

from login import *

s = login('songzongquan','000000')

r = getText(s,'https://code.bonc.com.cn/jira/rest/api/2/project')

print(r)
