# -*- coding:utf-8 -*-
#! usr/bin/python

import os
import csv
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

def excutetestcase()
    path = os.getcwd()
    script_path = path + "\testpy"
    scripts= os.listdir(script_path)
    length = len(scripts)
    #cycle_name是返回的循环的名称,作为csv文件的名称，创建一个csv文件
    cycle_name = "基本功能测试"
    csv_name = path+cycle_name+".csv"  
    with open(csv_name, "w") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["用例id", "用例执行状态", "描述"])  #填写表头
        for i in range(length):
            id = scripts[i].split("_")[1]  #case的id
            return = os.popen(script_path+scripts[i])   #返回执行文件的输出内容，为file对象
            return_read = return.read()
            status = return_read.split(":")[0]
            description = return_read.split(":")[1]
            writer.writerows([[id, status, description]])


