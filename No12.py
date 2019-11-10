# _*_ coding:utf-8 _*_
# 开发团队：
# 开发人员：Administrator
# 开发时间：2019/10/15 20:02
# 文件名称：No12.py
# 开发工具：PyCharm

# 题目：判断101-200之间有多少个素数，并输出所有素数。

# 程序分析：判断素数的方法：用一个数分别去除2到i(这个数)，如果能被整除，则表明此数不是素数，反之是素数。
for i in range(101 , 201):
    for j in range(2 , i):
        if i % j == 0 : break
    else:
        print(i)