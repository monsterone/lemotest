# -*- coding: utf-8 -*-
# @Time     : 2020/3/21 13:11
# @Author   : Monster
# @Email    : 945534456@qq.com
# @File     : class16_file1.py

#【16】
#相对路径  绝对路径
#D:\ZPython\python_hm\lemotest\class01\class15_file.py  #绝对路径

#疑问：如果我们要打开操作一个文件 是用相对路径好 还是用绝对路径好？
#都可以，做项目的时候会分析

#lib下的模块直接 import比较好
import os

#新建
#新建一个目录/新建一个文件夹
# os.mkdir("monster")

#跨级新建目录,用/符号来代表路径的不同层级
#必须确保上面的层级是存在的，monster目录必须先存在
# os.mkdir("monster/mest2") #相对路径

# os.mkdir("D:\\test_python") #绝对路径
# os.mkdir(r"D:\test_python")
#转义字符： \n \r ,我们可以通过加\ 还有 r R 来让转义字符失效(只要不是转义字符 / 、\ 、 \\没有区别)

#删除
#删除文件也是一级一级的删除 不推荐一次性删除

# os.mkdir("monster/mest2")

# os.rmdir("monster/mest2") #删除bbb
# os.rmdir("monster")  #（目录结构是：monster/mest2） #OSError: [WinError 145] 目录不是空的。: 'monster'


#拓展一:Python 可否强制删除
#拓展二:怎么去新建文件 open 删除文件？
#---------------->>>>>>>>>分割线<<<<<<<<<<<<<--------------

#路径的获取1  获取当前目录  （具体到最后一级目录）
path = os.getcwd()   #获取当前的工作路径
# print("1获取到的当前路径是：{0}".format(path))
#D:\ZPython\python_hm\lemotest\class01

#路径的获取2  获取当前文件所在的绝对路径  （具体到模块名）
path_2 = os.path.realpath(__file__)  #realpath = abspath
# print("2获取到的当前路径是：{0}".format(path_2))
# D:\ZPython\python_hm\lemotest\class01\class16_file1.py

#————

#如何拼接路径  +

new_path_1 = os.getcwd()+"\python66"
# print(new_path_1)
# os.mkdir(new_path_1)


#如何拼接路径 join

new_path_2 = os.path.join(os.getcwd(),"python111")
# print(new_path_2) #D:\ZPython\python_hm\lemotest\class01\python111
# os.mkdir(new_path_2)

#多级拼接
#跨级拼接新建目录，确保最后一级前面的目录是存在的  （新建）
# new_path_2 = os.path.join(os.getcwd(),"python111","study666")
# new_path_2 = os.path.join(os.getcwd(),"python111\study666")
# os.mkdir(new_path_2)

#————

#判断是文件还是目录 (返回布尔值)
print(os.path.isfile(__file__))  #True
print(os.path.isfile(os.getcwd())) #False
print(os.path.isdir(__file__)) # False
print(os.path.isdir(os.getcwd())) #True

#判断文件是否存在 (返回布尔值)
print(os.path.exists(r"D:\ZPython\python_hm\lemotest\class01\class13_function2.py"))

#罗列出当前路径下的所有文件 (返回列表)
print(os.listdir(os.getcwd()))

#拓展题：
#给定一个路径，请打印所有的路径 （直至这个路径下没有目录为止）
#思路：递归函数 写成一个函数

# for path in os.listdir(os.getcwd()):
#     if os.path.isdir(path):
#         os.listdir(os.path.join(os.getcwd(),path))
#         print("{0}还需要做进一步处理".format(path))
#     else:
#         print("这个是已经穷尽的路径",os.path.join(os.getcwd(),path))

def dir_list(now_path):
    for path in os.listdir(now_path):
        if os.path.isdir(os.path.join(now_path, path)):
            # os.listdir(os.path.join(now_path, path))
            dir_list(os.path.join(now_path, path))
            # print("{0}还需要做进一步处理".format(path))
        else:
            print("这个是已经穷尽的路径", os.path.join(now_path, path))


dir_list(os.getcwd())