# -*- coding: utf-8 -*-
# @Time     : 2020/4/4 18:04
# @Author   : Monster
# @Email    : 945534456@qq.com
# @File     : test_suite.py

import unittest
import HTMLTestReportCN
from class02_unittest.test_demo import test_http #模块名


from class03_excel.test_demo.test_http import TestHttp

##通过do_excel ,Excel表格加载测试数据
from class03_excel.test_demo3.do_excel2 import DoExcel

t=DoExcel(r"C:\Users\asus\Desktop\test.xlsx","python")

suite = unittest.TestSuite()

for i in range(1,t.max_row+1): #创建实例
    suite.addTest(TestHttp("test_api",t.get_data(i,1),t.get_data(i,2),eval(t.get_data(i,3)),t.get_data(i,4))) #实例的方法去加载



# #通过loader方式来加载用例
# loader = unittest.TestLoader()
# suite.addTest(loader.loadTestsFromModule(test_http))

#执行
with open("test_summer.html","wb") as file:
    runner = HTMLTestReportCN.HTMLTestRunner(stream=file,verbosity=2,title=None,description=None,tester=None)
    runner.run(suite)