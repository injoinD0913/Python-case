# _*_ coding:utf-8 _*_
# 开发团队：
# 开发人员：Administrator
# 开发时间：2019/11/1421:41
# 文件名称：No29.py
# 开发工具：PyCharm

# 学习使用按位取反~。

# ~0=1; ~1=0;
# (1)先使a右移4位。
# (2)设置一个低4位全为1,其余全为0的数。可用~(~0<<4)
# (3)将上面二者进行&运算。

if __name__ == '__main__':
    a = 234
    b = ~a
    print('The a\'s 1 complement is %d' % b)
    a = ~a
    print('The a\'s 2 complement is %d' % a)