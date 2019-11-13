# _*_ coding:utf-8 _*_
# 开发团队：
# 开发人员：Administrator
# 开发时间：2019/11/1315:06
# 文件名称：No27.py
# 开发工具：PyCharm

# 列表排序及连接。

# 排序可使用sort()方法，连接可以使用 + 号或extend()方法。

if __name__ == '__main__':
    a = [1, 3, 2]
    b = [3, 4, 5]
    a.sort()  # 对列表a排序
    print(a)

    print(a+b)  # 将列表a.b连接

    a.extend(b)
    print(a)   # 将列表 a.b 利用 extend 函数连接