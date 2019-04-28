# -*- coding:utf-8 -*-
#! usr/bin/python

import os
import csv 
import shutil #需要使用pip install pytest-shutil安装此模块
import logging

logger = logging.getLogger("main.executetestcase")



def executetestcase():
    path = os.getcwd()  #获取当前路径
    script_path = os.path.join(path+"/testpy/")  
    scripts= os.listdir(script_path) #获取所有执行脚本
    length = len(scripts)  #执行脚本的个数
    #print("此次循环要执行的用力个数为：",length)
    logger.debug("此次循环要执行的用例个数为：",length)
    result_path = os.path.join(path+"/result/")  #存放结果的路径
    screenshot_path = os.path.join(path+"/testpy/screenshot/") #截图存放路径
    #截图路径若存在,删除后新建,若不存在,直接新建
    if os.path.exists(screenshot_path):
        shutil.rmtree(screenshot_path)
        os.makedirs(screenshot_path)
    else:
        os.makedirs(screenshot_path)
    #结果路径若不存在,新建此路径
    if os.path.exists(result_path):
        pass
    else:
        os.makedirs(result_path)
    #执行结果写入csv文件
    csv_name = os.path.join(path+"/result/zhixing.csv")
    logger.debug("测试结果存放路径:",result_path)
    logger.debug("截图存放路径:",screenshot_path)
    #如果csv文件存在,删除
    if os.path.exists(csv_name):
        os.remove(csv_name)
    with open(csv_name, "w") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["用例id", "用例执行状态", "标题","详细描述"])  #填写表头
        for i in range(length):
            filestr = scripts[i].split(".") 
            id = filestr[0]  #case的id
            back_result = os.popen("python3 "+script_path+scripts[i])   #返回执行文件的输出内容,为file对象
            back_read = back_result.read()
            csv_write = back_read.split(":")
            write_list = [id]
            write_list.extend(csv_write)
            logger.debug("执行完成：",i/length)
            #print("用例执行结果：",write_list)
            writer.writerows([write_list])            
    logger.debug("用例执行完成")