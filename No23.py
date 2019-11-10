# _*_ coding:utf-8 _*_
# 开发团队：
# 开发人员：Administrator
# 开发时间：2019/11/5 23:56
# 文件名称：No23.py
# 开发工具：PyCharm

# 题目：两个变量值互换。

def exchange(a, b):
    a, b = b, a
    return (a, b)
x = int(input('val1:'))
y = int(input('val2:'))
print('x = %d,y = %d' % (x, y))
x, y = exchange(x, y)
print('x = %d,y = %d' % (x, y))