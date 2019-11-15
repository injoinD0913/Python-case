# _*_ coding:utf-8 _*_
# 开发团队：
# 开发人员：Administrator
# 开发时间：2019/11/1523:52
# 文件名称：No32.py
# 开发工具：PyCharm

# 求输入数字的平方，如果平方运算后小于 50 则退出。


TRUE = 1
FALSE = 0
def sq(x):
    return x * x


print('如果输入的数字小于 50，程序将停止运行。')

again = 1
while again:
    num = int(input('请输入一个数字：'))
    print('运算结果为: %d' % (sq(num)))
    if sq(num) >= 50:
        again = TRUE
    else:
        again = FALSE
