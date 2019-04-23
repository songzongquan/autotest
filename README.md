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

##测试用例脚本编写规范
1.标题
标题名称取jira中对应用例的编号，如：CLOUDIIP-123。
2.执行结果
执行结果有四种：成功、失败、阻止、WIP，执行成功，输出为：“成功”；执行失败，输出为：“失败：失败原因：详细描述”；执行被阻止，输出为：“阻止：被阻止原因”；执行正在进行，输出为：“WIP：原因说明”，所有的冒号用英文下的冒号。
3.执行结果输出
执行结果要用print输出，调用执行此脚本的程序才能获取到
4.截图
执行失败的用例，截图保存在当前路径下的screenshot文件夹，截图名称和用例编号保持一致。
5.关闭浏览器
脚本的末尾，使用webdriver.quit（）关闭浏览器

