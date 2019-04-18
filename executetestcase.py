# -*- coding:utf-8 -*-
#! usr/bin/python

import os
import csv
import sys
#reload(sys)
#sys.setdefaultencoding("utf-8")

#执行用例的名称命名格式为：auto_caseID_功能.py，如auto_0001_login.py
#执行用例中判断结果，输出两种情况：if condition：result=“pass：执行通过”；else：result=“fail：fail的原因”

def executetestcase():
    path = os.getcwd()
    script_path = path + r"/testpy/"
    scripts= os.listdir(script_path)
    length = len(scripts)
    #cycle_name是返回的循环的名称,作为csv文件的名称，创建一个csv文件
    csv_name = path+r"/zhixing.csv"  
    if os.path.exists(csv_name):
        os.remove(csv_name)
    with open(csv_name, "w") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["用例id", "用例执行状态", "描述"])  #填写表头
        for i in range(length):
            filestr = scripts[i].split("_") 
            if len(filestr) > 1:
                id = filestr[1]  #case的id
                back_result = os.popen("python3 "+script_path+scripts[i])   #返回执行文件的输出内容，为file对象
                print(back_result)
                back_read = back_result.read()
                status = back_read.split(":")[0]
                description = back_read.split(":")[1]
                writer.writerows([[id, status, description]])


