# _*_ coding:utf-8 _*_
# 开发团队：
# 开发人员：Administrator
# 开发时间：2019/10/13 21:41
# 文件名称：No8.py
# 开发工具：PyCharm

# 题目：输出9 * 9乘法口诀表。

# 程序分析：分行与列考虑，共9行9列，i控制行，j控制列。

for i in range(1, 10):
    for j in range(1, i + 1):
        print("%d*%d=%d" % (i, j, i * j))
