# -*- coding: utf-8 -*-
# @Time     : 2020/3/17 23:58
# @Author   : Monster
# @Email    : 945534456@qq.com
# @File     : class13_function2.py

#【13】 函数

#变量作用域

a=1  #全局变量
def add(b):
    # global a  # 声明这是一个全局变量       全局a变成10
    a=10  #局部变量
    print(a+b)
add(10)
print("a值",a)
#全局变量 和 局部变量
#1：作用范围不一样 全局:模块里都能用 局部：函数的局部变量只能用于函数内
#2：当全局变量 和 局部变量同名且同时存在时 函数优先调用局部变量
#3：当局部变量没有 就优先用全局
#4：global 关键字