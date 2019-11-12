# _*_ coding:utf-8 _*_
# 开发团队：
# 开发人员：Administrator
# 开发时间：2019/11/1222:59
# 文件名称：No25.py
# 开发工具：PyCharm

# for 循环语句

for letter in 'Python':  # 第一个实例
    print('当前字母 :', letter)

fruits = ['banana', 'apple', 'mango']
for fruit in fruits:  # 第二个实例
    print('当前水果 :', fruit)

print("Good bye!")

# for 循环也可以通过索引来进行遍历

fruits = ['banana', 'apple', 'mango']
for index in range(len(fruits)):
    print('当前水果 :', fruits[index])

print("Good bye!")

# for 循环中使用for...else...语句进行条件选择

for num in range(10, 20):  # 迭代 10 到 20 之间的数字
    for i in range(2, num):  # 根据因子迭代
        if num % i == 0:      # 确定第一个因子
            j = num/i          # 计算第二个因子
            print('%d 等于 %d * %d' % (num, i, j))
            break            # 跳出当前循环
    else:                  # 循环的 else 部分
        print(num, '是一个质数')
