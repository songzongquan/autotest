from login import *
from config import *
import json
from log import *



sub_logger = logging.getLogger("main.common")

# 输入s指的是login()返回的s，projectname为项目的key值，如CLOUDIIPZHYD，通过此函数返回该项目名称对应的项目的id：projectId
def getproject(s,projectkey):
    path = getjiraUrl()
    url = path + "rest/api/2/project"
    # print(url)
    sub_logger.debug("获取project信息的接口的地址："+url)
    list = getJson(s,url,params=None)
    # print(list)
    sub_logger.debug("获取的porject列表信息："+str(list))
    tag = "false"
    for i in list:
        if i["key"] == projectkey:
            projectId = i["id"]
            # print("项目的id：",projectId)
            sub_logger.debug("循环获取的项目id:"+projectId)
            tag = "true"
            return(projectId)
    if tag == "false":
        print("此项目不存在")

# 输入s指的是login()返回的s，projectId为项目的id，此函数实现选择对应的版本序号，返回版本的id：versionId
def getversions(s,projectId):
    path = getjiraUrl()
    url = path + "rest/api/2/project/"+projectId+"/versions"
    # print(url)
    sub_logger.debug("获取版本信息的接口的地址："+url)
    print("如下是该项目下的版本信息：")
    r = getJson(s, url, params=None)
    # print(r)
    sub_logger.debug("获取的版本信息的内容："+str(r))
    list_len=len(r)
    for i in range(list_len):
        # print(i+1,'.',"versionid:",r[i]["id"],"versionname:",r[i]["name"])
        print(i + 1, '.', r[i]["name"])
    number=int(input("请输入需要的版本的序号："))
    # print("版本的id：",r[number-1]["id"])
    sub_logger.debug(r[number-1]["id"])
    return(r[number-1]["id"])



 # 输入s指的是login()返回的s，projectId为项目的id，versionId为版本的id，此函数实现选择对应的循环的序号，返回循环的id：cycleId
def getcycleId (s, projectId, versionId):
    path = getjiraUrl()
    url = path + "rest/zapi/latest/cycle?projectId=" + projectId + "&versionId=" + versionId + "&expand=executionSummaries"
    # print(url)
    sub_logger.debug("获取循环列表的接口地址："+url)
    dict = getJson(s, url, params=None)
    # print(dict)
    sub_logger.debug("获取的循环列表的内容："+str(dict))
    print("如下是该项目对应的测试循环信息：")
    # 已读取为dict
    key_list = list(dict.keys())
    key_list.pop() #因为列表的最后一行是统计数据，故去掉最后一行
    # print(key_list)
    sub_logger.debug("获取的循环对应的id列表："+str(key_list))
    aa = []
    value_list = list(dict.values())
    value_list.pop() #因为列表的最后一行是统计数据，故去掉最后一行
    for i in value_list:
        aa.append(i["name"])
    # print(aa)
    sub_logger.debug("获取的循环对应的名字列表："+str(aa))
    length = len(key_list)
    for j in range(length):
        # print(j + 1, ". ", " id:", key_list[j], "name:", aa[j])
        print(j + 1, ". ", aa[j])
    project = int(input("请输入对应的循环的序号："))
    # print(aa[project-1])
    sub_logger.debug("选择某个循环对应的循环的名字"+aa[project-1])
    # print("循环的id:",key_list[project-1])
    sub_logger.debug("选择某个循环对应的循环的id"+key_list[project-1])
    return(key_list[project-1])

if __name__ == '__main__':
    s = login('lixiaofan', 'Lixiaofan123!')
#     # projectkey = str(input("请输入项目的key值："))
#     getproject(s,"CLOUDIIP")
#     getversions(s,'12106')
    getcycleId(s,'12106','12003')



