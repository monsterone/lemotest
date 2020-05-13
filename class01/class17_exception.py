# -*- coding: utf-8 -*-
# @Time     : 2020/3/21 17:18
# @Author   : Monster
# @Email    : 945534456@qq.com
# @File     : class17_exception.py
import os
#【17】
#两个问题
#类与对象--调试
#异常处理--抓了之后 要raise出来呢？（单元测试）

#异常处理 & 调试（类与对象再去讲调试）
#异常：你在运行代码过程中遇到的任何错误 带有error字样的 都是异常
#异常处理：我们对代码中所以可能出现的异常 进行处理
#疑问：我们为什么要去进行处理？

#异常
# os.mkdir("monster")  #FileExistsError

# os.rmdir("monster")  #OSError

# print(a)  #NameError

# def add(a,b):  #TypeError
#     print(a+b)
# add(3)

#异常后面的正常代码也不会执行
# print("就是这么牛逼！")

#-----------

#处理
#1:处理某个错误 #2：处理某种类型错误 #3：有错就抓
"""
try:
    os.mkdir("monster")  #FileExistsError
except FileExistsError:
# except NameError:
# except Exception:
    print("捕获成功，等待进一步处理")
"""
# print("就是这么牛逼！")




#既要抓 还要有处罚措施
#1:try...except
"""
try:
    os.rmdir("monster")
except OSError as e:  #把错误存在变量e
    print("捕获成功，等待进一步处理")
    print(e)
    print("错误为：{0}".format(e))
    #记下错误（数据库、日志、文件）
    file = open("error.txt","a+",encoding="utf-8")
    file.write(str(e))
    file.close() #关闭文件
"""

#2:try ....except...finally
"""
try:
    os.rmdir("monster")
    print("hahah1")
except OSError as e:  #把错误存在变量e
    print("捕获成功，等待进一步处理")
    print("错误为：{0}".format(e))
finally:  #无论是否异常最后都要执行
    print("就是这么牛逼！")
"""

#3:try ....except...else  （不常用）

try:
    os.rmdir("monster")
    print("hahah1")
except OSError as e:  #把错误存在变量e
    print("捕获成功，等待进一步处理")
    print("错误为：{0}".format(e))
else:  #跟try一起，没有异常执行else，有异常不执行else
    print("就是这么牛逼！")

