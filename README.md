# autotest
autotest是一个用python写的命令行小工具，它实现了将jira+zephyr 和 selenium 集成起来的效果。
统一在jira中进行测试用例与计划的管理、测试结果的统计与分析，不管是手动测试还是自动化测试脚本的测试。

## 安装
[安装说明](INSTALL.md)

## 目录文件说明

- 所有的 .py文件为程序文件
- log目录中放置系统运行日志文件autotest.log
- result目录存放测试后结果的临时数据文件
- screenshot为测试失败的界面截图文件，文件名称对应用例key
- testpy目录放的是从jira下载的测试脚本,为.py文件
- config目录下放程序的配置文件config.properties,主要配置jira的地址与用户名密码等。


## 使用
[使用说明](MANUAL.md)


# 开发人员参考api

## Zephyr的REST Api ：
https://getzephyr.docs.apiary.io/#reference/cycleresource/get-the-list-of-folder-for-a-cycle/get-cycle-information

## jira的REST api ：
https://developer.atlassian.com/cloud/jira/platform/rest/v2/


## requests 模块 
http://docs.python-requests.org/en/master
