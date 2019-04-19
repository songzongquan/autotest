# -*- coding: utf-8 -*-
#! usr/bin/python

from selenium import webdriver
import os,time
from selenium.common.exceptions import *
#from xvfbwrapper import Xvfb

#vdisplay = Xvfb()
#vdisplay.start()

#from selenium.webdriver.chrome.options import Options
#chrome_options = Options()
#chrome_options.add_argument("--no-sandbox")
#chrome_options.add_argument("--disable-setuid-sandbox")


current_path = os.getcwd()
shot = current_path+r"/screenshot/CLOUDIIPZHYD-329.png"
#print(shot)

driver = webdriver.Chrome() #(chrome_options=chrome_options)
driver.implicitly_wait(3)
driver.get("https://www.baidu.com/")
#time.sleep(5)
try:
    driver.find_element_by_id("ab")
    result =  "pass:验证成功"
except NoSuchElementException:
    result = "fail:元素不存在"
    driver.save_screenshot(shot)
else:
    pass

driver.quit()

#vdisplay.stop()
print(result)
