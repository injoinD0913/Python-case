# _*_ coding:utf-8 _*_
# 开发团队：
# 开发人员：Administrator
# 开发时间：2019/11/1315:51
# 文件名称：No28.py
# 开发工具：PyCharm

# 某个公司采用公用电话传递数据，数据是四位的整数，在
# 传递过程中是加密的，加密规则如下：
# 每位数字都加上5,然后用和除以10的余数代替该数字，
# 再将第一位和第四位交换，第二位和第三位交换。

if __name__ == '__main__':
    a = int(input('请输入四个数字：'))
    aa = []
    aa.append(int(a % 10))
    aa.append(int(a % 100 / 10))
    aa.append(int(a % 1000 / 100))
    aa.append(int(a / 1000))

    def exchange(a, b):
        a, b = b, a
        return (a, b)

    for i in range(4):
        aa[i] += 5
        aa[i] %= 10
    for i in range(2):
        aa[i], aa[3 - i] = exchange(aa[3 - i], aa[i])
    print(aa)










  #  for i in range(2):
 #       aa[i], aa[3 - i] = aa[3 - i], aa[i]
  #  for i in range(3, -1, -1):
   #     print(str(aa[i]))