# encoding:utf-8
from login import *
import os
import shutil
def downpyfile(s,id,filename):
    url = "https://code.bonc.com.cn/jira/secure/attachment/"+id+"/"+filename  #接口
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
    result = [{'id':'25833','filename':'auto_0001_baidu.py'},{'id': '25781', 'filename': '新建文本文档.py'}]  #返回的附件列表
    for i in result:
        downpyfile(s,i['id'],i['filename'])
