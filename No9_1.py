# _*_ coding:utf-8 _*_
# 开发团队：
# 开发人员：Administrator
# 开发时间：2019/10/14 13:25
# 文件名称：No9_1.py
# 开发工具：PyCharm

import time
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
# 暂停一秒
time.sleep(1)
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))