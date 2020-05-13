# -*- coding: utf-8 -*-
# @Time     : 2020/3/24 23:28
# @Author   : Monster
# @Email    : 945534456@qq.com
# @File     : class21_object3.py


#【21】 继承

class RobotOne(): #第一代及其人
    def __init__(self,year,name):
        self.year = year
        self.name = name

    def walking_on_ground(self):
        print(self.name+"只能在平地上行走，有障碍物就会摔倒")

    def robot_info(self):
        print("{0}年产生的机器人{1}，是中国研发的".format(self.year,self.name))

#继承
"""
class RobotTwo(RobotOne):  # 第二代机器人继承于第一代机器人的类


    def walking_on_ground(self): #子类里面的函数名与父类函数名重复的时候，就叫重写
        print(self.name + "可以在平地上行走")


    def walkig_avoid_block(self): #拓展
        #我想在子类的函数里面调用父类的某个函数
        self.robot_info()
        print(self.name+"可以避开障碍物")
"""
#第二代机器人
#继承的类 是否要用到初始化函数 请看是否从父类里面继承了
#1：父类有的 继承后 我都可以直接拿来用
#2：父类有的 子类也有重名的函数 那么子类的实例就优先调用子类的函数
"""
r2 = RobotTwo("2000","monster2")
# r2.robot_info()
r2.walking_on_ground()
r2.walkig_avoid_block()
"""

# r1 = RobotOne("1900","monster1")
# r1.robot_info()
# r1.walking_on_ground()


#知识点：多继承 继承多个函数


#为了多继承写的一个第二代机器人
class RobotTwo():  #

    def __init__(self,name):
        self.name = name

    def walking_on_ground(self):
        print(self.name + "可以在平地上行走")


    def walkig_avoid_block(self): #拓展

        print(self.name+"可以避开障碍物")



#第三代机器人
class RobotThree(RobotTwo,RobotOne,): #第三代机器人继承于第一代和第二代机器人的类

    # def __init__(self,year,name): #解决问题S (1)
    #     self.year = year
    #     self.name = name


    def jum(self):
        print(self.name+"可以单膝跳跃")

# r3 = RobotThree("2005","怪兽") #解决问题S (2)

r3 = RobotThree("怪兽")
r3.jum()
r3.walking_on_ground()

#疑问S：没有传递year参数 调用robot_year就会报错 怎么办？
#暂时没法解决，自己写函数时注意；或者 重写初始化函数
r3.robot_info()


#多继承的子类具有两个父类的属性和方法 如果两个父类具有同名的方法的时候
#子类调用函数就近原则 初始化函数也包括在内



# ----------
# 复习点：
#1:如果类里面有初始化函数 创建实例的时候 就必须在实例里面传递对应个数的参数
#2:调用函数的时候 实例调用 请自行去复习下 类函数 静态函数 实例函数



#——————————————————————

#超继承

class MathMethod():

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):
        print("我是父类的加法：",self.a+self.b)

    def sub(self):
        print(self.a-self.b)


class MathMethod_1(MathMethod):

    def dev(self):  #拓展
        print(self.a/self.b)

    def add(self): #重写
        super(MathMethod_1,self).add()  #超继承
        print("我是子类的加法",self.a+self.b+10)


MathMethod_1(5,6).add()
