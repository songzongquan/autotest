# coding:utf-8

from login import *
import json
import csv
from submitbug import *
from screenshot import *

# 读取聪聪的CSV文件
def ReadCSV():
    p=os.getcwd()+'report.csv' #文件路径
    f=csv.reader(open(p,'r', encoding = 'utf-8')) # 打开CSV文件
    for line in f: # 逐行读取文件
        a=line[:]
        print(a)
    return a

# 创建新执行，cycleId为测试循环ID,issueId为测试用例ID,projectId为项目ID
def Createxcute(s,cycleId,id,projectId):
    url='https://code.bonc.com.cn/jira/rest/zapi/latest/execution' #调“创建新执行”的接口
    values = json.dumps({"cycleId":cycleId,"issueId":id,"projectId":projectId})
    q= post(s,url, data=values)
    print(q)
    q1 = json.loads(q)
    for k,v in q1.items(): #读取字典的key
        excutionId=k

    return excutionId

# 主函数，修改用例状态，excutionId为执行ID
def Modifytatus(s,projectId,cycleId):
    excutionId=Createxcute(s,cycleId,id,projectId) # 获取用例的执行ID，通过Createxcute()函数获得
    url='https://code.bonc.com.cn/jira/rest/zapi/latest/execution/'+excutionId+'/execute'#
    data = ReadCSV() #调用的ReadCSV()函数
    for d in data:

        id = d[0]    # CSV文件共三列，id(用例id),status(用例状态),descr(描述)
        status = d[1]
        descr = d[2]

        if status == 'pass' :
            t= 1
        elif status == 'fail':
            t= 2

        values = json.dumps({"status":t})
        q= put(s,url, data=values) # 修改用例状态方法用put
        print(q)

        submitbug(s,descr,descr)









