# This code sample uses the 'requests' library:
# http://docs.python-requests.org
from login import *
import os

''' 输入s指的是login()返回的s，key为要添加附件的bug的bug号，id为测试结果为失败的用例对应的用例key值，如CLOUDIIP-23，为了取到该用例执行是对应的图片'''
def screenshot(s,key,id):

    url = "https://code.bonc.com.cn/jira/rest/api/2/issue/"+key+"/attachments"
    print(url)
    basedir=os.getcwd()
    source=os.path.join(basedir+'/screenshot/'+id+'.png')
    print(source)
    if os.path.exists(source):
        r = uploadFile(s,url,source)
        print(r)
    else:
        print('不存在报错图片')


if __name__ == '__main__':
    s = login('lixiaofan', 'Lixiaofan123!')
    screenshot(s,'CLOUDIIP-680','CLOUDIIP-680')
