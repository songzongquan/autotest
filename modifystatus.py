# coding:utf-8

from login import *
import json
import csv
from submitbug import *
from screenshot import *
import os,time
from config import *
from log import *

logger = logging.getLogger("main.modifyStatus")

'''读取执行后的CSV文件,CSV文件存储在当前文件夹中的result中,从第二行开始读取'''

def readCSV():
    basedir=os.getcwd()
    p=os.path.join(basedir+'/result/zhixing.csv')
    d=csv.reader(open(p,'r',encoding='UTF-8'))
    l = list(d)
    return l[1:]

'''通过issuKey(肉眼可见的用例编号如"CLOUDIIPZHYD-23"),获取issueId(从F12中获得的用例ID),versionId(版本ID,目前相当于写死的,日后会做更改),
projectId(项目ID),componentId(模块ID),主函数调用这些ID'''

def getIssueInfo(s,issueKey):

    path=getjiraUrl()
    # print(path)
    url=path+'rest/api/2/issue/'+issueKey
    #print(url)
    logger.debug('输出获取用例ID,版本ID,项目ID,组件ID的接口地址：'+url)
    r =getJson(s,url)
    issueId = r["id"]
    versionId=r["fields"]["customfield_11303"][0]["id"]
    projectId=r["fields"]["project"]["id"]
    componentId=r["fields"]['components'][0]['id']
    
    return (issueId,versionId,projectId,componentId)

'''创建新执行，通过cycleId(测试循环ID),issueId(从F12中获得的用例ID),projectId(项目ID)来获取executionId(用例执行ID)'''

def creatExcute(s,cycleId,issueId,projectId):

    path=getjiraUrl()
    # print(path)
    url=path+'rest/zapi/latest/execution' #调“创建新执行”的接口
    values = json.dumps({"cycleId":cycleId,"issueId":issueId,"projectId":projectId})
    q= post(s,url, data=values)
    q1 = json.loads(q)
    for k,v in q1.items(): #读取字典的key值
        excutionId=k

        return excutionId

'''主函数(修改用例状态):先读取执行文件,然后getIssueInfo函数调用执行文件中的issueKey来获取issueId,creatExcute函数调用getIssueInfo
中的issueId来获取executionId,最后主函数利用executionId来修改状态，用例状态为失败时调用submitbug函数提交bug，再调用screenshot函数来上传附件,'''

def modifyStatus(s,cycleId,projectId):

    data = readCSV() # 调用ReadCSV()函数
    for d in data:
        issueKey = d[0]    # CSV文件目前有四列，issueKey(用例key),status(用例状态),summary(标题),descr(描述

        issue = getIssueInfo(s,issueKey) #调用getIssueInfo()函数,获取各种id
        issueId=issue[0]
        excutionId=creatExcute(s,cycleId,issueId,projectId) # 获取用例的执行ID，通过CreatExcute()函数获得
        path=getjiraUrl()
        # print(path)
        url=path+'rest/zapi/latest/execution/'+excutionId+'/execute'

        status = d[1]
        t=-1
        if status == '通过':
            t= 1
        elif status == 'WIP':
            t= 3
        elif status == '阻止':
            t= 4
        elif status == '失败':
            t= 2
            summary = d[2]
            descr = d[3]
            versionId,componentId=issue[3],issue[1]
            bugkey=submitbug(s,summary,descr,versionId,projectId,componentId)
            screenshot(s,bugkey,issueKey)

        values = json.dumps({"status":t})
        p= put(s,url, data=values) # 修改用例状态方法用put
        #print(p)
        logger.debug('输出修改用例后的信息：'+p)

if __name__ == '__main__':
    s = login('wangyujia', 'wyj211421.')
    modifyStatus(s,'33','12106')














