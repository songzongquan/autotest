# This code sample uses the 'requests' library:
# http://docs.python-requests.org
from login import *
import os

def upload(s,key,caseid):

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
    upload(s,'CLOUDIIP-680','680')