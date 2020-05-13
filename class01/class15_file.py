# -*- coding: utf-8 -*-
# @Time     : 2020/3/20 23:51
# @Author   : Monster
# @Email    : 945534456@qq.com
# @File     : class15_file.py

#【15】文件处理
#file txt xml html --->


#mode 打开这个文件的模式
#r w a
#r+  w+ a+
#rb rb+ wb wb+ ab ab+  做单元测试的时候
"""
file=open("class15.txt","r+")
res = file.read()  #进行完一次读写操作后，光标到了文末
# file.write("summer")
print(res)
"""
#1：file文件open之后默认是r 只读模式 如果你要写内容报错
#2：r+ 可读、可写  先写的话从头开始覆盖写 读光标之后的内容  读写跟着光标走
#3：如果要写入中文要注意编码格式 #decode encode

# 注意：读写最好分开操作，不要合在一起操作

#4: w 只写 硬要去读 就会报错
#5：w+ 可读、可写
# 不管是w还是w+ 如果文件存在 就直接清空 再重写 ，如果文件不存在则新建一个再从写
#拓展：怎么移动光标，可以指定行数吗
file=open("class15.txt","w+")
res = file.read()
# file.write("summer")
print(res)

#6： a追加写 a+  追加写，不会清空
#如果文件存在 就直接写在后面 ，如果文件不存在则新建一个文件进行结果写入
file=open("class15.txt","a")
res = file.write("madah")
# res = file.write("\nmadah")  #换行

#重点掌握两种 r  a

file=open("class15.txt","r")
res = file.read()      #读全部
res1 = file.readline()  #读一行
res2 = file.readlines()  #读取多行，返回列表

file=open("class15.txt","a")
file.writelines(["888\n","999"]) #写多行


#说明：感觉这个讲得不太好，没有抓住重点，讲得有点乱（课下自己补充总结）