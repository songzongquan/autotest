# autotest简介
autotest是一个用python写的命令行小工具，它将jira+zephyr 和 selenium 集成起来，实现jira测试管理对自动化测试的支持，也减少了手工填报自动化测试结果到jira的工作量，整合了jira测试管理能力和selenium的自动化测试能力。
利用它，可以统一在jira中进行手动测试的管理与自动测试的管理，只需要将python写的测试脚本作为用例的附件上传，通过autotest工具可以实现这些测试脚本的自动执行，自动填写测试结果并且自动的填报bug与上传错误页面截图。
目前，仅支持功能测试的整合，未来可以整合jmeter来实现压力测试的自动化与统一管理。

## 技术架构
1. autotest 登录jira，拉取当前项目当前版本的当前测试循环的测试用例的自动化测试脚本，并下载到本地。
2. autotest 分别调用这些测试脚本，驱动本地浏览器执行自动化测试。并保存测试的结果和截图
3. autotest再次连上jira，将测试结果与错误截图上报到jira系统。


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



