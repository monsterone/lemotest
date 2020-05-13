# -*- coding: utf-8 -*-
# @Time     : 2020/3/23 23:01
# @Author   : Monster
# @Email    : 945534456@qq.com
# @File     : home_work1.py


#请利用嵌套for循环生成一个直角三角形
#*
#**
#***
#****
#*****
"""
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

#输出99乘法表

#1*1=1
#1*2=2 2*2=4
#1*3=3 2*3=6 3*3=9
# .......

"""
for i in range(1,10):
    for j in range(1,i+1):
        # print(str(j)+"*"+str(i)+"="+str(i*j),end="\t")
        print("{0}*{1}={2}".format(j,i,i*j),end="\t")
    print()
"""

#冒泡排序
# 利用for循环，完成a=[1,7,4,89,32,2]的冒泡排序
# 冒泡排序:小的排在前面,大的排在后面
#冒泡的概念 关系到你接下来怎么写程序
#相邻的两个元素一次比较

a=[1,7,4,89,34,2]  #冒泡算法 一般最多比较n-1趟，就完成
# 1 4 7 34 2 89 第一趟
# 1 4 7 2 34 89 第二趟
# 1 4 2 7 34 89 第三趟
# 1 2 4 7 34 89 第四趟

for i in range(0,len(a)-1): # 0 1 2 3 4
    for j in range(0,len(a)-1-i):
        if a[j]>a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
    # print(a)
print(a)


