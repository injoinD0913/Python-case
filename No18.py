# _*_ coding:utf-8 _*_
# 开发团队：
# 开发人员：Administrator
# 开发时间：2019/10/24 22:18
# 文件名称：No18.py
# 开发工具：PyCharm

# 题目：字符串排序。

str1 = input('input string:\n')
str2 = input('input string:\n')
str3 = input('input string:\n')
print(str1, str2, str3)
if str1 > str2:
    str1, str2 = str2, str1
if str1 > str3:
    str1, str3 = str3, str1
if str2 > str3:
    str2, str3 = str3, str2
print('排序后：')
print(str1, str2, str3)