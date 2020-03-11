# -*- coding: utf-8 -*-
# @Time     : 2020/3/11 22:43
# @Author   : Monster
# @Email    : 945534456@qq.com
# @File     : class7_operator.py

#【7】 运算符 5大类
#（1）算术运算符  + - * / %
 #模运算 取余运算 (用在：判断某个数 是偶数 还是奇数)
 # a=4  # print(a%2)

#（2）赋值运算 = += -= *=
a=5   #赋值运算
a+=1 #a=a+1
# print(a)

#（3）比较运算符 > 、 >= 、 < 、<= 、!= 、 == 6种比较关系
#返回的结果是布尔值：Ture False
a=10
b=5
# print(a>b)  #True
# print("get"=="GET") #False

#（4）逻辑运算符 and or 拓展：not
#返回的结果是布尔值：Ture False
a=10
b=5
#and and左右两边结果都为真才为真 只要有一个为假 就为假 (真真尾真 and)
#or or左右两边结果都为假才为假 只要有一个为真 就为真 （假假为假）
# print(a>11 and b>4) #False
# print(a>11 or b>4) #True

#（5）成员运算符 in 、not in
#返回的结果是布尔值：Ture False
s='hello'  # print('o'in s)  #True
l=[1,2,3]  # print(2 in l) #True
d={"age":18,"name":"怪兽"} # print("age" in d) #True #判断key,不判断value





