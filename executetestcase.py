# -*- coding:utf-8 -*-
#! usr/bin/python

import os
import csv

#执行用例的名称命名和jira中对应用例保持一致
#执行用例中判断结果,输出为:if condition:result="通过”；else:result="失败:标题:详细描述”

def executetestcase():
    path = os.getcwd()  #获取当前路径
    script_path = os.path.join(path+"/testpy/")  
    print(script_path)
    scripts= os.listdir(script_path) #获取所有执行脚本
    length = len(scripts)  #执行脚本的个数
    result_path = os.path.join(path+"/result/")  #存放结果的路径
    screenshot_path = os.path.join(path+"/screenshot/") #截图存放路径
    #结果路径若不存在，新建此路径
    if os.path.exists(result_path):
        pass
    else:
        os.makedirs(result_path)
    #截图路径若存在，删除后新建，若不存在，直接新建
    if os.path.exists(screenshot_path):
        os.rmdir(screenshot_path)
        os.makedirs(screenshot_path)
    else:
        os.makedirs(screenshot_path)
    #执行结果写入csv文件
    csv_name = os.path.join(path+"/result/zhixing.csv")
    #如果文件存在，删除
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
            print(write_list)
            writer.writerows([write_list])