# -*- coding: utf-8 -*-
# @Time     : 2020/3/24 22:27
# @Author   : Monster
# @Email    : 945534456@qq.com
# @File     : class20_object2.py

#【20】 类与对象

class Teacher:

    def __init__(self,name,age):  #初始化函数/方法（java:构造函数）
        self.name = name
        self.age = age

    #没有return 返回值


    def coding(self,lange="python"):   #实例方法
        # self.cooking()
        print(self.name+"回敲{0}代码".format(lange))

    def cooking(self):  #实例方法
        print(self.name+"会做饭")

    @classmethod  #类方法
    def swimming(cls):
        print("会游泳")

    @staticmethod #静态方法
    def sing():
        print("会表演唱歌")

t = Teacher("monster","18")
t1 = Teacher("monster1","19")
t2 = Teacher("monster2","20")

t.coding("java")
t1.coding()

#什么时候用初始化函数？
#想用就用
#如果某个属性值是多个函数共用的 就可以用初始化函数