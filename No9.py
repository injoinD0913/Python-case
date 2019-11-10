# _*_ coding:utf-8 _*_
# 开发团队：
# 开发人员：Administrator
# 开发时间：2019/10/14 12:11
# 文件名称：No9.py
# 开发工具：PyCharm

# 题目：暂停一秒输出。

# 程序分析：使用time模块的sleep()函数。

import time
myD = {1: 'a', 2: 'b'}
for key, value in dict.items(myD):
    print(key, value)
    time.sleep(1)  # 暂停 1 秒
