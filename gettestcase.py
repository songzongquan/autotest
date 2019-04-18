from login import *
import requests
def gettestcase(s,cycleId):
    url='https://code.bonc.com.cn/jira/rest/zapi/latest/execution'#接口
    url2='https://code.bonc.com.cn/jira/rest/api/2/issue'
    params = {'action':'expand','cycleId':cycleId}
    r = getJson(s,url,params)               #这个接口下的所有测试用例字典

    issues= r['executions'] #这个接口下的所有测试用例字典下所有executions字典
    result = []     #返回结果，元素是一个{id:filename}形式的字典
    for x in issues:                         #在executions字典中每找到一个issueId,就拼接url
       issueId = x['issueId']
       issue = getJson(s, url2 + '/' + str(issueId), None)
       attachments = issue['fields']['attachment']    #字典
       for attachment in attachments:                 #list
           id = attachment['id']
           filename = attachment['filename']
           #print(id)
           #print(filename)
           if ".py" in filename:
               e ={"id":id,"filename":filename}
               result.append(e)

    return result


if __name__ == '__main__':
    s = login('lixiaofan', 'Lixiaofan123!')
    r = gettestcase(s,14)
    print(r)