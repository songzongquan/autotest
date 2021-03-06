# 使用说明

## 前提
 需要autotest及依赖的环境都已安装成功。

## 使用步骤

1. 维护测试用例
 即在jira+zephyr中管理好版本，测试循环，以及测试用例（步骤为文本描述）

2. 为测试用例添加自动测试脚本附件

 首先编写测试脚本，需要用python语言来编写。
 可以先通用selemniu IDE这样的工具录制后改写，也可以直接手写。
 但要注意必须遵循下列规范

   - 测试脚本除print 出测试结果信息外，不能有别的打印。
   - 打印的测试结果必须是用:分隔的一行文本，分别有四段内容，第一列为用例key，第二列为结果(pass/fail),第三列为结果的标题，第四列为结果的描述
   
3. 将脚本以附件形式上传到对应的用例中，命名规范 {用例key}.py ，如  CLOUDIIP-329.py

4. 执行自动化测试

``` 
$cd autotest
$python3 main.py

``` 
此时系统会提示你选择一个项目，选择后回车，系统会提示你选择版本、选择后回车，系统会提示你选择一个测试循环。选择后回车，
系统开始执行下载脚本、以及执行脚本等动作。此时可以看到本地的浏览器可能会被打开执行测试步骤 ，此时应等待其执行全部完成

5. 检查测试结果
等全部脚本执行完毕后，由autotest自动打开的浏览器窗口会全部关闭。并提示运行完成。
此时打开jira，查看各个测试执行的状态，然后针对测试失败的对应的用例，看看是否生成了bug，是否有对应的截图上传。
如果这些都ok，即成功完成本轮测试。

## 测试用例脚本编写规范
1. 标题
标题名称取jira中对应用例的编号，如：CLOUDIIP-123。
2. 执行结果
执行结果有四种：成功、失败、阻止、WIP，执行成功，输出为：“成功”；执行失败，输出为：“失败：失败原因：详细描述”；执行被阻止，输出为：“阻止：被阻止原因”；执行正在进行，输出为：“WIP：原因说明”，所有的冒号用英文下的冒号。
3. 执行结果输出
执行结果要用print输出，调用执行此脚本的程序才能获取到
4. 截图
执行失败的用例，截图保存在当前路径下的screenshot文件夹，截图名称和用例编号保持一致。
5. 关闭浏览器
脚本的末尾，使用webdriver.quit（）关闭浏览器
