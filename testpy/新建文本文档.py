import requests


'''登录，输入用户名和密码，返回session,此session具有request的所有的函数，
如果下面包装的方法不够用，你可以直接用s来调用相关的函数;'''
def login(username,password):
    s = requests.Session()
    s.auth = (username,password)
    return s