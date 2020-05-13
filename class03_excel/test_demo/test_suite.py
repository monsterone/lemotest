# -*- coding: utf-8 -*-
# @Time     : 2020/4/4 18:04
# @Author   : Monster
# @Email    : 945534456@qq.com
# @File     : test_suite.py

import unittest
import HTMLTestReportCN
from class02_unittest.test_demo import test_http #模块名

from class03_excel.test_demo.test_http import TestHttp


test_data=[{"url":"http://127.0.0.1:5000/search/","data":{"q": "selenium"},"expected":"10200","method":"get"},
           {"url": "http://127.0.0.1:5000/login","data":{"username": "admin", "password": "a123456"}, "expected": "10200", "method": "post"},
           {"url": "http://127.0.0.1:5000/login", "data": {"username": "", "password": "a123456"},"expected": "10103", "method": "post"},
           {"url": "http://127.0.0.1:5000/login", "data": {"username": "admin666", "password": "a123456"},"expected": "10104", "method": "post"}]


suite = unittest.TestSuite()

for item in test_data: #创建实例
    suite.addTest(TestHttp("test_api",item['url'],item['data'],item['method'],eval(item['expected'])))  #实例的方法去加载
#实例化方法去加载用例 url,data,method,expected


# #通过loader方式来加载用例
# loader = unittest.TestLoader()
# suite.addTest(loader.loadTestsFromModule(test_http))

#执行
with open("test_summer.html","wb") as file:
    runner = HTMLTestReportCN.HTMLTestRunner(stream=file,verbosity=2,title=None,description=None,tester=None)
    runner.run(suite)