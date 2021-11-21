# 目前仅在WIN电脑上实现
其他操作系统的电脑不清楚

# 功能描述

CC98 和 NexusHD 自动签到

用 python-selenium 和 webdriver 实现 

CC98 自动签到获取财富值 & NexusHD 自动签到获取魔力值

# 使用说明

本人的python版本为3.10.0，selenium版本为4.0.0

需要将在两个文件中填写自己的用户名和密码，webdriver 是 0 cookie 的（我也不知道这样说对不对，还不太懂），每次启用进程都需要输入账号和密码

本人会继续使用pyinstaller将签到的py文件打包为exe，再在开机启动项中添加exe的快捷方式，从而实现自动签到

