# -*- coding: utf-8 -*-
# @Time     : 2020/3/14 22:07
# @Author   : Monster
# @Email    : 945534456@qq.com
# @File     : class10_while.py

#【9】while 控制循环
#语法：
#while 条件表达式：#逻辑 成员 比较 空数据 布尔值
    #代码块

#执行规律：首先判断while后面的条件表达式是否成立
#如果True 那就执行代码块，执行完毕之后，继续判断-->如果True那就执行代码块，执行完毕之后->
# 否则不进入代码块

#防止代码进入死循环：加一个变量来控制循环次数
# a = 1 #初始值
# while a<=10:
#     print("第{}次".format(a))
#     a+=1


#利用while循环 实现1-100相加
a = 1
sum = 0
while a<=100:
    sum+=a
    a+=1
print("求和的结果是：",sum)


#while 与 if语句搭配使用 break continue
