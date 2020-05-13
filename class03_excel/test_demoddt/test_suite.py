# -*- coding: utf-8 -*-
# @Time     : 2020/4/4 18:04
# @Author   : Monster
# @Email    : 945534456@qq.com
# @File     : test_suite.py

import unittest
import HTMLTestReportCN
from class03_excel.test_demoddt import test_http #模块名



suite = unittest.TestSuite()

# ddt 通过loader方式来加载用例
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromModule(test_http))

#执行
with open("test_summer.html","wb") as file:
    runner = HTMLTestReportCN.HTMLTestRunner(stream=file,verbosity=2,title=None,description=None,tester=None)
    runner.run(suite)