# -*- coding: utf-8 -*-


###先参数化 (在test_suite参数化)
#地址 测试数据 断言期望结果 除了这几个不同 其他的都是高度相识 80%
#参数化 url data expected



#测试数据参数化
#超继承
#1：unittest 测试用例（函数test_） 不能传参；使用for.. 循环只能取到第一条数据
#2：重写unittest初始化函数 def __init__,使得以前方法不能用了
#3： 使用超继承重写unittest初始化函数 def __init__，保留原来的父类方法  --ok
