# _*_ coding:utf-8 _*_
# 开发团队：
# 开发人员：Administrator
# 开发时间：2019/10/11 19:05
# 文件名称：No4.py
# 开发工具：PyCharm

# 题目：输入某年某月某日，判断这一天是这一年的第几天？

# 程序分析：将当前月份之前的天数加上本月已经度过的天数；特殊情况，闰年且输入月份大于2时需考虑多加一天：

year = int(input('year:\n'))
month = int(input('month:\n'))
day = int(input('day:\n'))

months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
if 0 < month <= 12:
    sum = months[month - 1]
else:
    print
    'data error'
sum += day
leap = 0
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    leap = 1
if (leap == 1) and (month > 2):
    sum += 1
print('it is the %dth day.' % sum)