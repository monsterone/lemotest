# -*- coding: utf-8 -*-
# @Time     : 2020/3/14 22:53
# @Author   : Monster
# @Email    : 945534456@qq.com
# @File     : home_work.py

##
#输入num为四位数，对其按照如下的规则进行加密：
#1）每一位分别加5，然后分别将其替换为该数除以10取余后的结果
#2）将该数的第1位和第4位互换，第2位和第3位互换，
#3）最后合起来作为加密后的整数输出
#优酷笔试题

# num = input("请输入四位数：")
# n=''
# for i in list(num):
#     m=(int(i)+5)%10
#     n+=str(m)
# # print(n)
# num_str=n[::-1]
# num=int(num_str)
# print("加密后：",num)



# num = int(input("请输入四位数："))
#
# n_1 = (int(num/1000)+5)%10
# n_2 = (int(num/100%10)+5)%10
# n_3 = (int(num/10%10)+5)%10
# n_4 = (int(num%10)+5)%10
#
# num_str=str(n_4)+str(n_3)+str(n_2)+str(n_1)
# num=int(num_str)
# print("加密后：",num)


##
# 列如：passwd={"admin":"123321","user1":"123456"}
#1.设计一个登陆程序，不同的用户和对应密码存在一个字典里，输入正确的用户名和密码去登陆
#2.首先输入用户名，如果用户名不存在或者为空，则一直提示输入正确的用户名
#3.当用户名正确的时候，提示去输入密码，如果密码跟用户名不对应，则提示密码错误请重新输入
#4.如果密码输入错误超过三次，中断程序运行
#5.当密码输入错误时，提示还有几次机会
#6.用户名和密码输入成功的时候，提示登录成功！
##万科笔试题

passwd={"admin":"123321","user":"123456"}


count = 3
while True:
    usename = input("请输入用户名：")
    if usename in passwd.keys():
        while count>0:
            pwd = input("请输入密码：")
            if pwd==passwd[usename]:
                print("登录成功！")
                break
            else:
                print("密码错误，请从新输入")
                count-=1#每次错误的时候减除1
                print("你还有输入密码的{0}次机会".format(count))
        break
    elif usename not in passwd.keys() or usename=='':
        print("请输入正确的用户名")
