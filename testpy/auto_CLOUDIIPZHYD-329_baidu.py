# -*- coding: utf-8 -*-
#! usr/bin/python

from selenium import webdriver
import os

current_path = os.getcwd()
shot = current_path+r"/screenshot/CLOUDIIPZHYD-329.png"
#print(shot)

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get("https://www.baidu.com/")
try:
    r = driver.find_element_by_id("ab")
    if r:
    	result =  "pass:验证成功"
    else:
    	result = "fail:元素不存在"
    	#driver.save_screenshot(shot)
        
        
except:
    result = "fail:测试程序异常，测试被阻止："
    #driver.save_screenshot(shot)
    
#driver.close()


print(result)
