# _*_ coding:utf-8 _*_
# 开发团队：
# 开发人员：Administrator
# 开发时间：2019/11/109:19
# 文件名称：No6.py
# 开发工具：PyCharm

# 题目：斐波那契数列。

# 程序分析：斐波那契数列指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
# 可以以递归的方法来定义：
# F0 = 0(n=0)
# F1 = 1(n=1)
# Fn = F[n - 1] + F[n - 2](n= > 2)

# 使用递归
i = int(input())
def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)
print(fib(i))
