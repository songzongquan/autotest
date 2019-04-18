#!/usr/bin/python
# -*- coding: UTF-8 -*-

from login import *
from gettestcase import *
from downpyfile import *



projectId = 12106

cycleId = 14 #先指定一个测试循环id

s = login('songzongquan','000000') #先登录jira
testcases = gettestcase(s,cycleId) #获取测试用例执行脚本
downloadFiles(s,testcases) #下载所有用例文件




#r = getText(s,'https://code.bonc.com.cn/jira/rest/api/2/project')

#print(r)

#downloadFile(s,'https://code.bonc.com.cn/jira/secure/thumbnail/24269/_thumb_24269.png','/home/song/_thumb_24269.png')

#r2 = uploadFile(s,'https://code.bonc.com.cn/jira/rest/api/2/issue/CLOUDIIP-679/attachments', '/home/song/Pictures/timg.jpeg')
#print(r2)
