# -*- coding: utf-8 -*-
# @Time     : 2020/3/24 21:48
# @Author   : Monster
# @Email    : 945534456@qq.com
# @File     : class19_object1.py

#【19】 类与对象

#类的概念： 具有某一类共同属性和特性的事物
# 类一般包含 属性及方法
'''
class Teacher:
    pass
'''


class Teacher:
    name = "monster"
    age = 24

    def coding(self):   #实例方法
        print(self.name+"回敲代码")

    def cooking(self):  #实例方法
        print(self.name+"会做饭")

    @classmethod  #类方法
    def swimming(cls):
        print("会游泳")

    @staticmethod #静态方法
    def sing():
        print("会表演唱歌")

#类里面的方法分为三种
#1,实例方法：意味着，这个方法 只能实例来调用

t = Teacher()
t.cooking()

Teacher.cooking(t)  #显示传递实例，不建议使用
# Teacher.cooking()  #TypeError: cooking() missing 1 required positional argument: 'self'

#2,类方法： @classmethod
Teacher.swimming()
t.swimming()

#3,静态方法
Teacher.sing()
t.sing()

#总结
#1:实例方法self 和类方法cls 静态方法（普通方法） 实例和类名都可以直接调用--（实例方法类名调用要传入实例：Teacher.cooking(t) ）
#2:不同点: 静态方法和类方法不可以调用类里面的属性值
#3：什么时候去定义为静态和类方法 当你的某个函数和其他的类的属性、方法没有任和关系时，就可以定义为静态和类方法

