#!/usr/bin/python
# -*- coding: UTF-8 -*-

from login import *
from gettestcase import *
from downpyfile import *
from executetestcase import *
from modifystatus import *
from common import *
from config import *



# username = str(input("请输入账户名："))
# password = str(input("请输入密码："))

username=getUsername()
password=getPassword()
s=login(username,password)
# s = login('songzongquan','000000') #先登录jira

''' 输入项目的key值，返回项目的id：projectId'''
projectname = str(input("您好！您的自动化测试之旅马上开始，敬请期待！\n请输入项目key值："))
projectId= getproject(s,projectname)

''' 选择对应的版本序号，返回版本的id：versionId'''
versionId=getversions(s,projectId)

''' 选择对应的循环序号，返回循环的id：cycleId'''
cycleId=getcycleId(s,projectId,versionId)

testcases = gettestcase(s,cycleId) #获取测试用例执行脚本
downloadFiles(s,testcases) #下载所有用例文件
executetestcase()      #执行测试脚本
modifyStatus(s,cycleId,projectId)





#r = getText(s,'https://code.bonc.com.cn/jira/rest/api/2/project')

#print(r)

#downloadFile(s,'https://code.bonc.com.cn/jira/secure/thumbnail/24269/_thumb_24269.png','/home/song/_thumb_24269.png')

#r2 = uploadFile(s,'https://code.bonc.com.cn/jira/rest/api/2/issue/CLOUDIIP-679/attachments', '/home/song/Pictures/timg.jpeg')
#print(r2)
