# _*_ coding:utf-8 _*_
# 开发团队：
# 开发人员：Administrator
# 开发时间：2019/11/1223:09
# 文件名称：No26.py
# 开发工具：PyCharm

# 利用递归方法求5!。

#  递归公式：fn = fn_1 * 4!


def fact(j):
    sum = 0
    if j == 0:
        sum = 1
    else:
        sum = j * fact(j - 1)
    return sum


print(fact(5))