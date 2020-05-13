# -*- coding: utf-8 -*-
# @Time     : 2020/3/14 14:40
# @Author   : Monster
# @Email    : 945534456@qq.com
# @File     : class9_for.py

#【9】 循环 for 、while 关键字
#python for循环语法：
# for item in 某个数据类型：(数据类型包含：字符串 列表 元祖 字典 集合等)
     #代码块
# in? 成员运算符 in 、not in

# (1)for循环的的循环次数 由数据的元素个数决定
"""
s='hello'
L=[1,2,3]
d={"age":18,"name":"怪兽"} #字典遍历返回的是key
for item in s:  #遍历s里面每一个元素，然后赋值给item
    print(item)
    # print("hahhaha")
"""

# (2)利用for循环 完成列表里面所有数据的相加
"""
L=[5,6,9,3,7]
sum=0
for item in L:
    sum+=item
print(sum)
"""

# (3)字典key、value
"""
d={"age":18,"name":"怪兽"}
print(d.values())  #dict_values([18, '怪兽']) #获取字典里面的所有value值
print(d.keys())  #dict_keys(['age', 'name'])  #获取字典里面的所有key值

print(type(d.values())) #<class 'dict_values'>

for item in d.values(): #遍历字典值
    print(item)
"""


# (4) range函数  生成整数序列
"""
# range(m,n,k) m头 n尾 k步长-默认为1 ，取头不取尾
range(1,5,1)  # 1 2 3 4
range(1,6,2) #1 3 5
range(8)  #头默认为0    #0 1 2 3 4 5 6 7

for item in range(3): # 0 1 2
    print("循环次数")
"""
#range()练习
"""
#利用for循环 根据L的索引值，打印出每个元素的值
L=[5,6,9,3,7]
for i in range(len(L)):
    print(L[i])

#利用for循环和range函数 完成1-100整数相加和（包含1，和100）
sum = 0
for i in range(1,101):
    sum+=i
print(sum)
"""

# (5)嵌套循环
"""
#请把列表里面的每一个元素单独打印出来
L=[["nkhik","fgrfg","硅谷"],["哈哈","uguo","回顾"]]
for b in L:
    for a in b:
        print(a)

#请利用嵌套for循环生成一个直角三角形
#*
#**
#***
#****
#*****
for i in range(5):
    for j in range(i+1):
        print("*",end="")
    print()
"""
#等腰三角形
#xxxx*xxxx
#xxx* *xxx
#xx* * *xx
#x* * * *x
#* * * * *

'''
for i in range(1,6):
   for j in  range(1,6-i):
       print(" ",end="")
   for k in range(1,i+1):
        print("* ",end="")

   print()
'''