# _*_ coding:utf-8 _*_
# 开发团队：
# 开发人员：Administrator
# 开发时间：2019/10/15 19:48
# 文件名称：No11.py
# 开发工具：PyCharm

# 题目：打印出所有的"水仙花数"

# 程序分析：利用for循环控制100 - 999个数，每个数分解出个位，十位，百位。

for n in range(100, 1000):
    i = int(n / 100)
    j = int((n / 10) % 10)
    k = int(n % 10)
    if n == i ** 3 + j ** 3 + k ** 3 :
        print(n)
