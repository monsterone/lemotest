# -*- coding: utf-8 -*-
# @Time     : 2020/3/24 21:02
# @Author   : Monster
# @Email    : 945534456@qq.com
# @File     : class18_object.py

#【18】 类与对象

# python类的语法 关键字 class     def 函数名(参数）:  函数的关键字
# class 类名： #类名的规范，标识符规范+首字母大写  驼峰命名
    #类的属性
    #类的方法

class BoyFried:  #模板
    #类属性
    heigh = 175
    weight = 120
    money = "500万"

    #类函数（实际：实例方法）
    def cooking(self):  #会做饭
        print(self)
        print("会做饭")

    def earn(self): #会zz
        print("3w")


#实例/对象---具体的一个例子：  类名()
bf = BoyFried()
print(bf)
bf.cooking()
# print(bf.money)


#实例/对象具有类里面的所以属性和方法的使用权限
#调用属性： 实例.属性名
#调用方法： 实例.方法名()




