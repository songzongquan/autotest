# autotest
autotest是一个用python写的命令行小工具，它实现了将jira+zephyr 和 selenium 集成起来的效果。
统一在jira中进行测试用例与计划的管理、测试结果的统计与分析，不管是手动测试还是自动化测试脚本的测试。

# 参考api

## Zephyr的REST Api ：
https://getzephyr.docs.apiary.io/#reference/cycleresource/get-the-list-of-folder-for-a-cycle/get-cycle-information

## jira的REST api ：
https://developer.atlassian.com/cloud/jira/platform/rest/v2/
end

## 任务分解



| 模块名字                     | 模块文件名称      | 类名                                        | 返回值                                                       | 需求描述                                                     | 负责人 |
| ---------------------------- | ----------------- | ------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------ |
| 登录jira                     | login.py          | 类：Login(username,password)函数：get（）， | Login()返回loginstatus（1：登录成功；0：登录失败）；get（）函数返回字符串 | 实现用户成功登陆jira，其余人调用时不用考虑用户名密码，直接是已登录状态 |        |
| 批量获取该测试循环的所有用例 | gettestcase.py    | Gettestcase（projectid，cycid,version）     | 返回包含caseid，title的列表                                  | 实现jira上批量获取某个项目下某个测试循环的所有用例，返回包含caseid，title的列表 |        |
| 下载py附件                   | downpyfile.py     | Downpyfile（caseid）                        | 返回包含caseid的列表                                         | 下载以.py结尾的文件，放置到python安装路径的testpy文件夹下，例如git仓库中autotest\testpy，需判断是否存在该文件夹，不存在需要创建 |        |
| 执行py文件                   | excutetestcase.py | Excutetestcase（caseid）                    | 返回py文件名中的caseid，及执行成功与失败的status，图片的url的列表 | 执行下载的py附件，返回py文件名中的caseid，及执行成功与失败的status，图片的url的列表，错误图片路径为autotest\testpy\photo |        |
| 修改用例的状态               | modifystatus.py   | Modifystatus（caseid，status）              | 返回caseid，casestatus（用例对应的状态），modifystatus（jira用例修改成功与否的状态）的列表 | 需要调用jira修改执行过的用例的状态，返回caseid，casestatus（用例对应的状态），modifystatus（jira用例修改成功与否的状态）的列表 |        |
| 提交bug                      | submmitbug.py     | Submmitbug（caseid）                        | 返回值：submitbugstatus：成功/失败                           | 需要实现选择casestatus为失败的用例，提交bug标题，内容选择Gettestcase返回的titil后面添加“失败”两个字，从错误图片路径中获取该caseid对应的图片，提交附件。 |        |
|                              |                   |                                             |                                                              |                                                              |        |