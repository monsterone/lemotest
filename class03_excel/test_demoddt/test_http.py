# -*- coding: utf-8 -*-
# @Time     : 2020/4/4 17:09
# @Author   : Monster
# @Email    : 945534456@qq.com
# @File     : test_http.py

import unittest
from ddt import ddt,data
from API_AUTO.tools.http_request import HttpRequest  #引入工具类requests
from class03_excel.do_config.read_config import ReadConfig
from class03_excel.test_demo.get_data import GetData
from class03_excel.test_demoddt.do_excel import DoExcel

# 从配置文件读取mode值
mode = ReadConfig().read_config('case.config', 'MODE', 'mode')
test_data=DoExcel(r"C:\Users\asus\Desktop\test_header.xlsx","python").get_data(mode)

print(test_data)
@ddt
class TestHttp(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @data(*test_data)
    def test_api(self,item):  #接口用例

        res = HttpRequest().http_request(item['url'],eval(item['data']),item['method'],getattr(GetData,"Cookie"))
        if res.cookies: #如果cookie有的话 那么就更新COOKIE(反射) #这里添加只是练习，具体无实际意义
            setattr(GetData,"Cookie",res.cookies)
        try:
            self.assertEqual(item['expected'],res.json()['code'])
        except AssertionError as e:
            print("出错了{}".format(e))
            raise e

if __name__ == '__main__':
    unittest.main()
