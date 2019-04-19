# coding:utf-8

from login import *
import json
import csv
from submitbug import *
from screenshot import *
import os

# 读取聪聪的CSV文件
def readCSV():
    basedir=os.getcwd()
    p=os.path.join(basedir+'/result/zhixing.csv') #文件路径
    d=csv.reader(open(p,'r')) # 打开CSV文件
    # for line in f: # 逐行读取文件
    #     d=line[:]
    l = list(d)    
    return l[1:]

def getIssueId(s,issuekey):
    url='https://code.bonc.com.cn/jira/rest/api/2/issue/'+issuekey
    print(url)
    r =getJson(s,url)
    issueid = r["id"]
    versionid=r["fields"]["customfield_11303"][0]["id"]
    projectid=r["fields"]["project"]["id"]
    componentid=r["fields"]['components'][0]['id']
    # print(issueid,versionid,projectid,componentid)
    return (issueid,versionid,projectid,componentid)


# 创建新执行，cycleId为测试循环ID,issueId为测试用例ID,projectId为项目ID
def createxcute(s,cycleId,key,projectId):
    url='https://code.bonc.com.cn/jira/rest/zapi/latest/execution' #调“创建新执行”的接口
    issueid = getIssueId(s,key)
    values = json.dumps({"cycleId":cycleId,"issueId":issueid,"projectId":projectId})
    q= post(s,url, data=values)
    # print(q)
    q1 = json.loads(q)
    for k,v in q1.items(): #读取字典的key
        excutionId=k
        # print(excutionId)

    return excutionId

# 主函数，修改用例状态，excutionId为执行ID
def modifystatus(s,cycleId,projectId):

    data = readCSV() # 调用ReadCSV()函数
    for d in data:

        key = d[0]    # CSV文件共三列，id(用例id),status(用例状态),descr(描述)
        status = d[1]
        descr = d[2]

        excutionId=createxcute(s,cycleId,key,projectId) # 获取用例的执行ID，通过Createxcute()函数获得
        url='https://code.bonc.com.cn/jira/rest/zapi/latest/execution/'+excutionId+'/execute'#
        #print(status)
        t=-1
        if status == 'pass':
            t= 1
        elif status =='fail':
            t= 2
            key=submitbug(s,descr,descr,componentid,projectid,versionid)
            screenshot(s,key,key)
        #print(t)
        values = json.dumps({"status":t})
        p= put(s,url, data=values) # 修改用例状态方法用put
    #    print(p)


if __name__ == '__main__':
    s = login('wangyujia', 'wyj211421.')
    modifystatus(s,'33','12106')













