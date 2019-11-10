# _*_ coding:utf-8 _*_
# 开发团队：
# 开发人员：Administrator
# 开发时间：2019/11/1 0:13
# 文件名称：No20.py
# 开发工具：PyCharm

# 题目：列表使用实例。

# list
# 新建列表
testList = ['西安工程大学', 124, [1, 2, 4, 5]]
# 访问列表长度
print(len(testList))
# 到列表结尾
print(testList[:])
# 向列表添加元素
testList.append('i\'m new here!')
print(len(testList))
print(testList[-1])
# 弹出列表的最后一个元素
print(testList.pop(1))
print(len(testList))
print(testList)