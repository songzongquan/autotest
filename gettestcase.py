from login import *
import requests
def gettestcase(s,cycleId):
    url='https://code.bonc.com.cn/jira/rest/zapi/latest/execution'#�ӿ�
    url2='https://code.bonc.com.cn/jira/rest/api/2/issue'
    params = {'action':'expand','cycleId':cycleId}
    r = getJson(s,url,params)               #����ӿ��µ����в��������ֵ�

    issues= r['executions'] #����ӿ��µ����в��������ֵ�������executions�ֵ�
    result = []     #���ؽ����Ԫ����һ��{id:filename}��ʽ���ֵ�
    for x in issues:                         #��executions�ֵ���ÿ�ҵ�һ��issueId,��ƴ��url
       issueId = x['issueId']
       issue = getJson(s, url2 + '/' + str(issueId), None)
       attachments = issue['fields']['attachment']    #�ֵ�
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