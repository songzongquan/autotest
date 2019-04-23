# 安装指南

## 依赖软件环境

- python3.x
- jira
- Zephyr - jira的测试管理插件 https://zephyrdocs.atlassian.net/
- zapi   - zephyr api https://zephyrdocs.atlassian.net/wiki/spaces/DEVELOPER/pages/33095703/ZAPI+Server
- selenium with python  - https://selenium-python.readthedocs.io
- driver for web browser  - https://selenium-python.readthedocs.io 中1.3.Drivers 章节
- Firfox/Chrome/Edge/safari   

## 安装步骤

1. 下载autotest

 - 可以直接用git clone  https://github.com/songzongquan/autotest.git 得到autotest目录及文件
 - 或者访问此下载：https://github.com/songzongquan/autotest/archive/master.zip，然后解压到autotest目录

2. 配置jira访问信息

首先进入config目录，用编辑器打开config.properties文件。

```shell
$cd autotest/config
$vi config.properties
```
可见文件内容如下：

```
 url = https://code.bonc.com.cn/jira/  #jira服务主地址
 username = xxxxx   # 账号名
 password = yyyyy   #密码

```
请将以上内容修改为你的jira环境的实际的值。


3. 运行autotest

```shell
$ cd autotest
$ python3  main.py

```
如果能够提示您选择项目，即安装成功。

## 注意事项
1. 注意浏览器的版本号与selenium Driver的版本号是否适配，不然调用浏览器时会失败

