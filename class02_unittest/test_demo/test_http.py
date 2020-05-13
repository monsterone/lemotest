# -*- coding: utf-8 -*-
# @Time     : 2020/4/4 17:09
# @Author   : Monster
# @Email    : 945534456@qq.com
# @File     : test_http.py

import unittest
from API_AUTO.tools.http_request import HttpRequest  #引入工具类requests

class TestHttp(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_normal(self):  #登录
        url = 'http://httpbin.org/get'
        data = {'user': 'zxw', 'password': '666'}
        res = HttpRequest().http_request(url,data,'get')
        print(res.json())

if __name__ == '__main__':
    pass