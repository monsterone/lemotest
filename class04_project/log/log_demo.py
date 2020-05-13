# -*- coding: utf-8 -*-
# @Author   : Monster
# @File     : log_demo.py

import logging

#Logger 收集日志 debug info error
#handdler 输出日志 指定的文件  还是控制台 （默认控制台）
# logging.debug("111")
# logging.info("222")
# logging.warning("333")
# logging.error("444")
# logging.critical("555")


#定义一个日志收集器my_Logger
my_logger=logging.getLogger('python')


#设置级别
my_logger.setLevel('DEBUG')

# #收集日志
# my_logger.debug("one......")
# my_logger.error("three.........")


#设置输出格式：
formatter=logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(message)s')

#创建一个我们自己的输出渠道（控制台）
ch=logging.StreamHandler()
ch.setLevel("DEBUG")
ch.setFormatter(formatter)
#创建一个文本输出渠道
fh=logging.FileHandler('logtest.txt',encoding='utf-8')
fh.setLevel("DEBUG")
fh.setFormatter(formatter)
#两者对接---指定输出渠道（文本）
my_logger.addHandler(ch)
my_logger.addHandler(fh)


#收集日志
my_logger.debug("one......")
my_logger.error("three.........")