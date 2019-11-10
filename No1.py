# _*_ coding:utf-8 _*_
# 开发团队：
# 开发人员：Administrator
# 开发时间：2019/10/10 7:49
# 文件名称：No1.py
# 开发工具：PyCharm

#题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
#程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去掉不满足条件的排列。

for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if (i!=k)and(i!=j)and(j!=k):
                print(i,j,k)