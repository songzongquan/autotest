# encoding:utf-8
from login import *
import os
def downpyfile(s,id,filename):
    url = "https://code.bonc.com.cn/jira/rest/api/2/attachment/"+id  #接口
    #print(url)
    basedir = os.getcwd()  #获取当前路径
    path = basedir + '\\testpy\\'  #py文件存取的目录
    if not os.path.exists(path):   #判断py文件存取的文件夹是否存在，不存在的话就新建
        #print("Selected target not exist, try to create it.")
        os.makedirs(path)
    target = path + filename  #py文件存取的最终显示路径
    #print(target)
    d = downloadFile(s, url, target)  #调用login中的下载附件的函数
    #print(d)
if __name__ == '__main__':
    s = login('0111831', '1314wy8023jc.')
    result = [{'id': '25817', 'filename': 'UntitledTestCase.py'}, {'id': '25781', 'filename': '新建文本文档.py'}]  #返回的附件列表
    for i in result:
        #print(i['id'], i['filename'])
        downpyfile(s,i['id'],i['filename'])