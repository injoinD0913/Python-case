# _*_ coding:utf-8 _*_
# 开发团队：
# 开发人员：Administrator
# 开发时间：2019/11/1123:59
# 文件名称：No24.py
# 开发工具：PyCharm

# 练习函数调用。

def hello_world():
    print('hello world')

def three_hellos():
    for i in range(3):
        hello_world()
if __name__ == '__main__':
    three_hellos()