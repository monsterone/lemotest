# -*- coding: utf-8 -*-
# @Time     : 2020/4/4 23:26
# @Author   : Monster
# @Email    : 945534456@qq.com
# @File     : class_ddt.py

## ddt  ddt+unittest来进行数据的处理 第三方库
#装饰器 可以自行去了解 会在你函数运行之前运行

import unittest
from ddt import ddt,data,unpack

test_data=[[1,3],[4,5]]   # ---data(*test_data)---> [1,3]、[4,5]
                          # ---unpack---> 1 3  --要用来个参数来接收
                                  # 4 5  --unpack根据(,)拆分
# test_data=[{"no":1,"name":"monster"},{"no":2,"name":"怪兽"}]
@ddt #装饰测试类
class TestMath(unittest.TestCase):

    @data(*test_data)  #装饰测试方法 拿到几个数据 就执行几条用例
    def test_print_data(self,item): #测试用例
        print("item:",item)

    # @data(*test_data)
    # @unpack
    # 如果unpack后的参数 少于5个 推荐用unpack 要注意参数不对等的情况，提供对应个数参数来接收变量
    #如果对字典进行unpack， key与你的字典key对应
    # def test_print_data(self, a,b):
    #     print("item:", a)
    #     print("item:", b)

    # def test_add(self):
    #     a=10
    #     b=20
    #     print(a+b)
