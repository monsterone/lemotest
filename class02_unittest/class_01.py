# -*- coding: utf-8 -*-
# @Time     : 2020/3/31 22:36
# @Author   : Monster
# @Email    : 945534456@qq.com
# @File     : class_01.py

#接口测试的本质 就是测试类里面的函数  (通过数据驱动)
#单元测试的本质 测试函数 代码级别  （通过代码级别）

# 单元测试框架 unittest+ 接口   pytest+WEB
#pytest + jenkins + allure

#功能测试
#1：写用例  TestCase
#2：执行用例  1：TestSuite 存储用例 2：TestLoader 找用例，加载用例，存到1的TestSuite
#3：对比实际结果 期望结果 判断用例是否通过 #断言 Assert
#4：出具测试报告 #TextTestRunner

import unittest
from class02_unittest.math_method import MathMethod  #测试的目标类
#写一个测试类 对我们自己写的math method 模块里面的类 进行单元测试

class TestMathMethod(unittest.TestCase):  #继承了unittest里面的TestCase 专门来写用例
    #编写测试用例
    #1：一个用例就是一个函数 不能传参 只能有self关键字
    #2：所有的用例（所有的函数 都是test 开头 test_）

    def setUp(self):#重写
        print("我要开始执行用例了")

    def tearDown(self):
        print("我已经执行完毕测试用例了")

    #1：可以不写吗？ 可以 爱写不写 必要的时候写
    #2：什么时候执行 setUp 执行，没一条测试用例之前执行setUp
    #tearDown 每一条测试用例执行完毕之后都会执行tearDown
    #3：如果说 你有操作必须在执行用例之前准备好 那就放到 setUp里面
    # 如果说 你有操作必须在执行用例完毕之后要清除掉 那就放到 tearDown里面 （如数据库连接断开操作）


    def test_add_two_positive(self):  #两个正数相加 1+1
        res = MathMethod(1,1).add()
        print("1+1的结果值是：",res)
        #加一个断言：判断期望值与实际值的比对结果 一致就算通过 不一致 就算失败
        try:
            self.assertEqual(2,res)
        except AssertionError as e:
            print("出错啦！断言错误是{0}".format(e))
            raise e #异常处理完后记得要抛出去

    def test_add_two_zero(self):  # 两个0相加 0+0
        res = MathMethod(0,0).add()
        print("0+0的结果值是：", res)
        self.assertEqual(0,res,"两个0相加出错了") #断言里msg是用例执行失败的时候 会显示的提示


    def test_add_two_negative(self):  # 两个负数相加 -1 + -2
        res = MathMethod(-1,-2).add()
        print("-1+-2的结果值是：", res)
        self.assertEqual(-3,res)



class TestMulit(unittest.TestCase):  #继承了unittest里面的TestCase 专门来写用例
    #编写测试用例
    #1：一个用例就是一个函数 不能传参 只能有self关键字
    #2：所有的用例（所有的函数 都是test 开头 test_）
    def test_mulit_two_positive(self):  #两个正数相乘 1*1
        res = MathMethod(1,1).multi()
        print("1*1的结果值是：",res)

    def test_mulit_two_zero(self):  # 两个0相乘0*0
        res = MathMethod(0,0).multi()
        print("0*0的结果值是：", res)

    def test_mulit_two_negative(self):  # 两个负数相乘 -1*-2
        res = MathMethod(-1,-2).multi()
        print("-1*-2的结果值是：", res)

if __name__ == '__main__':
    unittest.main()



#用例执行顺序
#ASCI
#abcdefg.....z
# test_add_two_positive #2
# test_add_two_zero    #3
# test_add_two_negative  #1

#鼠标位置 对执行用例影响
#放在哪儿执行哪个 放最后执行全部 ，或修改unittest的py文件名

#注意 （） 、TestSuite()  （不是TestCase()，没有suite.addTest()方法）
# suite = unittest.TestSuite()  #存储用例
# suite.addTest(TestMathMethod('test_add_two_zero'))