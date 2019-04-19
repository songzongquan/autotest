# -*- coding: utf-8 -*-
#! usr/bin/python

from selenium import webdriver
import os

current_path = os.getcwd()
shot = current_path+r"/screenshot/325.png"

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get("https://www.baidu.com/")
try:
    driver.find_element_by_id("kw")
except:
    result = "fail:元素不存在"
    driver.get_screenshot_as_file(shot)
else:
    result =  "pass:验证成功"
print(result)
