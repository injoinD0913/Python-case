# _*_ coding:utf-8 _*_
# 开发团队：
# 开发人员：Administrator
# 开发时间：2019/11/109:11
# 文件名称：No5.py
# 开发工具：PyCharm

# 题目：输入三个整数x, y, z，请把这三个数由小到大输出。

# 程序分析：可以将三个数添加到一个空的数组中，再调用sort函数

l = []
for i in range(3):
    x = int(input('integer:\n'))
    l.append(x)
l.sort()
print(l)