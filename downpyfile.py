# encoding:utf-8
from login import *
import os
import shutil
from config import *

def downpyfile(s,id,filename):
    jiraurl= getjiraUrl()
    url = jiraurl+"secure/attachment/" + id + "/" + filename  # 接口地址
    print(url)
    basedir = os.getcwd()  #获取当前路径
    path = os.path.join(basedir+'/testpy/') #py文件存取的目录
    target = path + filename  #py文件存取的最终显示路径
    d = downloadFile(s, url, target)  #调用login中的下载附件的函数
if not os.path.exists(os.path.join(os.getcwd()+'/testpy')):
    os.makedirs(os.path.join(os.getcwd() + '/testpy/'))
else:
    shutil.rmtree(os.path.join(os.getcwd()+'/testpy'))
    os.makedirs(os.path.join(os.getcwd() + '/testpy/'))
def downloadFiles(s,testcases):
    for testcase in testcases:
        fid = testcase['id']
        fname = testcase['filename']
        downpyfile(s,fid,fname)


if __name__ == '__main__':
    s = login('0111831', '1314wy8023jc.')
    result = [{'id':'25850','filename':'auto_CLOUDIIPZHYD-325_baidu.py'},{'id': '25856', 'filename': 'auto_CLOUDIIPZHYD-329_baidu.py'}]  #返回的附件列表
    for i in result:
        id = i['id']
        filename = i['filename']
        downpyfile(s,i['id'],filename)
