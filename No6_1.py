# _*_ coding:utf-8 _*_
# 开发团队：
# 开发人员：Administrator
# 开发时间：2019/10/12 20:34
# 文件名称：No6_1.py
# 开发工具：PyCharm

# 题目：斐波那契数列。

# 程序分析：斐波那契数列指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
# 可以以递归的方法来定义：
# F0 = 0(n=0)
# F1 = 1(n=1)
# Fn = F[n - 1] + F[n - 2](n= > 2)

# 输出指定个数的斐波那契数列
i = int(input())
def fib(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    fibs = [1, 1]
    for i in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs
print(fib(i))