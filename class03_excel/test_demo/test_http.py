# -*- coding: utf-8 -*-
# @Time     : 2020/4/4 17:09
# @Author   : Monster
# @Email    : 945534456@qq.com
# @File     : test_http.py

import unittest
from API_AUTO.tools.http_request import HttpRequest  #引入工具类requests
from class03_excel.test_demo.get_data import GetData


class TestHttp(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    #超继承用法
    def __init__(self,methodName,method,url,data,expected):
        super(TestHttp,self).__init__(methodName) #超继承 ，父类的方法保留了
        self.url = url
        self.data = data
        self.method = method
        self.expected = expected



    def test_api(self):  #接口用例

        res = HttpRequest().http_request(self.url,self.data,self.method,getattr(GetData,"Cookie"))
        if res.cookies: #如果cookie有的话 那么就更新COOKIE(反射) #这里添加只是练习，具体无实际意义
            setattr(GetData,"Cookie",res.cookies)
        try:
            self.assertEqual(self.expected,res.json()['code'])
        except AssertionError as e:
            print("出错了{}".format(e))
            raise e

if __name__ == '__main__':
    pass