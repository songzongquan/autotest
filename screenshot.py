# This code sample uses the 'requests' library:
# http://docs.python-requests.org
from login import *
import os

''' 输入s指的是login()返回的s，key为要添加附件的bug的bug号，caseid为测试结果为失败的用例对应的用例编号，为了取到该用例执行是对应的图片'''
def screenshot(s,key,caseid):

    url = "https://code.bonc.com.cn/jira/rest/api/2/issue/"+key+"/attachments"
    print(url)
    # source='./screenshot/{caseid}.png'
    basedir=os.getcwd()
    source = basedir+'\\screenshot\\'+caseid+'.png'
    print(dir)
    r=uploadFile(s,url,source)
    print(r)

if __name__ == '__main__':
    s = login('lixiaofan', 'Lixiaofan123!')
    screenshot(s,'CLOUDIIP-680','680')