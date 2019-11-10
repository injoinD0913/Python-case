# _*_ coding:utf-8 _*_
# 开发团队：
# 开发人员：Administrator
# 开发时间：2019/10/16 19:26
# 文件名称：No15.py
# 开发工具：PyCharm

# 题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。几个数相加由键盘控制。

Tn = 0
Sn = []
n = int(input('n = '))
a = int(input('a = '))
for count in range(n):
    Tn = Tn + a
    a = a * 10
    Sn.append(Tn)
    print(Tn)
# Sn = reduce(lambda x, y: x + y, Sn)
ans = sum(Sn)
print("计算和为：", ans)