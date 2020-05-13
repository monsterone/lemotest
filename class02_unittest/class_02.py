# -*- coding: utf-8 -*-
# @Time     : 2020/3/31 23:15
# @Author   : Monster
# @Email    : 945534456@qq.com
# @File     : class_02.py

import unittest
from class02_unittest.class_01 import TestMathMethod
import HTMLTestRunner
suite = unittest.TestSuite()  #存储用例
#方法一：
#只执行一条 两个正数相加
# suite.addTest(TestMathMethod('test_add_two_positive'))
# suite.addTest(TestMathMethod('test_add_two_zero'))

#方法二： TestLoader
loader = unittest.TestLoader()  #创建一个加载器
#从测试类去找
suite.addTest(loader.loadTestsFromTestCase(TestMathMethod))
#从模块中去找
# from class02_unittest import class_01  #具体到模块
# suite.addTest(loader.loadTestsFromModule(class_01))

#执行
'''
file = open("test.txt","w+",encoding="UTF-8")
runner = unittest.TextTestRunner(stream=file,verbosity=2) #0 1 2是最详细的
runner.run(suite)
# file.close()


#执行 上下文管理器 --原始的
with open("test.txt","w+",encoding="UTF-8") as file:
    runner = unittest.TextTestRunner(stream=file,verbosity=2) #0 1 2是最详细的
    runner.run(suite)
'''


#新鲜 html
with open("test_report.html","wb") as file:
    runner = HTMLTestRunner.HTMLTestRunner(stream=file,
                                           verbosity=2,
                                           title="单元测试报告",
                                           description="单元测试报告描述")
    runner.run(suite)