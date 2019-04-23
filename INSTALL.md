# 安装指南

## 依赖软件环境

- python3.x
- jira
- Zephyr
- zapi
- selenium  
- firfox or chrome 以及其driver程序  

## 安装步骤

1. 下载autotest

 - 可以直接用git clone  https://github.com/songzongquan/autotest.git 下载
 

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


