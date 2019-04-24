# This code sample uses the 'requests' library:
# http://docs.python-requests.org
from login import *
import os
from log import *
from config import *

sub_logger = logging.getLogger("main.screenshot")
# 输入s指的是login()返回的s，key为要添加附件的bug的bug号，id为测试结果为失败的用例对应的用例key值，如CLOUDIIP-23，为了取到该用例执行是对应的图片
def screenshot(s,key,id):

    path = getjiraUrl()
    url = path + "rest/api/2/issue/"+key+"/attachments"
    # print(url)
    sub_logger.debug("jira:上传附件接口的url：",url)

    basedir=os.getcwd()
    source=os.path.join(basedir+'/screenshot/'+id+'.png')
    # print(source)
    sub_logger.debug("用来上传的附件的地址：",source)
    if os.path.exists(source):
        r = uploadFile(s,url,source)
        # print(r)
        sub_logger.debug("附件上传成功：",r)
    else:
        sub_logger.info('不存在报错图片')


if __name__ == '__main__':
    s = login('lixiaofan', 'Lixiaofan123!')
    screenshot(s,'CLOUDIIPZHYD-329','CLOUDIIPZHYD-329')
