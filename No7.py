# _*_ coding:utf-8 _*_
# 开发团队：
# 开发人员：Administrator
# 开发时间：2019/10/13 19:46
# 文件名称：No7.py
# 开发工具：PyCharm

# 题目：将一个列表的数据复制到另一个列表中

# 程序分析：使用列表[:]

a = []
for i in range(10):
    i = input('输入列表a的元素值:\n')
    a.append(i)
b = a[:]
print(b)