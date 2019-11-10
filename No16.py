# _*_ coding:utf-8 _*_
# 开发团队：
# 开发人员：Administrator
# 开发时间：2019/10/20 20:40
# 文件名称：No16.py
# 开发工具：PyCharm

# 题目：求100之内的素数。

# 输出指定范围内的素数

# 输入数据范围
# 此代码具有普适性，不局限在100之内，可以任意限定范围
lower = int(input("输入区间最小值: "))
upper = int(input("输入区间最大值: "))

for num in range(lower, upper + 1):
    # 素数大于 1
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)