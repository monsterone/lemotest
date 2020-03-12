# -*- coding: utf-8 -*-
# @Time     : 2020/3/12 21:46
# @Author   : Monster
# @Email    : 945534456@qq.com
# @File     : class8_if.py

#【8】  控制语句 分支分流 循环语句  for while
#判断语句 if..elif ..else 关键字
#（1）if  条件语句: 1:（比较 逻辑 成员 均可）
           # 2:空数据==False 非空数据==True
           #3:直接用布尔值控制（鸡肋）
# s=''
# s='hello'
# if 'o' in s:  #当if后面的语句 满足条件 运算结果是True 那就会执行他的子语句
#     print("恭喜，成年！")


#（2）：一个条件语句里面 只能有一个if和一个else （else后面不能添加条件语句）
# if 条件语句：
    #子语句
#else:
    # 子语句
'''
age=20
if age>18:
    print("恭喜，成年！2")
else:
    print("加油长大，小屁孩")
'''

#（3）：if 和elif后面可以加条件语句
# if 条件语句：
    #子语句
# elif 条件语句：
    #子语句
#else:
    # 子语句

'''
#input()函数 从控制台获取一个数据 获取的数据都是字符串类型
age=int(input("请输入你的年龄：")) #如果输入为字符串等非数字，报错
#自己解决：isdigit()
# Python isdigit() 方法检测字符串是否只由数字组成。
# age.isdigit()

# age=16
if age>18:
    print("恭喜，成年！3")
elif 18>age>0:
    print("加油长大，小屁孩")
else:
   print("你的年龄输入有误，不能为负数！")
'''

#拓展：
# isdigit()方法检测字符串是否只由数字组成。
# 三个函数的区别和注意点：#https://www.cnblogs.com/chenglei0520/p/9431353.html
# isdigit() #纯数字、 S1 = '12345'、S2 = '①②'
# isalpha() #汉字+字母、S1 = 'abc汉字'
# isalnum() #字母+汉字+数字  S1 = 'abc汉字1'

