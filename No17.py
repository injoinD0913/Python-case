# _*_ coding:utf-8 _*_
# 开发团队：
# 开发人员：Administrator
# 开发时间：2019/10/21 23:44
# 文件名称：No17.py
# 开发工具：PyCharm

# 题目：输入3个数a, b, c，按大小顺序输出。

if __name__ == '__main__':
    n1 = int(input('n1 = :\n'))
    n2 = int(input('n2 = :\n'))
    n3 = int(input('n3 = :\n'))
    def swap(p1, p2):
        return p2, p1
    if n1 > n2:
        n1, n2 = swap(n1, n2)
    if n1 > n3:
        n1, n3 = swap(n1, n3)
    if n2 > n3:
        n2, n3 = swap(n2, n3)
    print(n1, n2, n3)