# _*_ coding:utf-8 _*_
# 开发团队：
# 开发人员：Administrator
# 开发时间：2019/10/16 13:36
# 文件名称：No13.py
# 开发工具：PyCharm

# 题目：利用条件运算符的嵌套来完成此题：学习成绩 >= 90分的同学用A表示，60 - 89分之间的用B表示，60分以下的用C表示。

# 程序分析：程序分析：(a > b)?a: b这是条件运算符的基本例子。

score = int(input('输入分数:\n'))
if score >= 90:
    grade = 'A'
elif score >= 60:
    grade = 'B'
else:
    grade = 'C'
print('%d 属于 %s' % (score, grade))