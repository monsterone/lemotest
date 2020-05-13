# -*- coding: utf-8 -*-
# @Author   : Monster
# @File     : log_demo.py

import logging

class MyLog():

    def my_log(self,msg,level):
        #定义一个日志收集器my_Logger
        my_logger=logging.getLogger('python')

        #设置级别
        my_logger.setLevel('DEBUG')

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
        if level=='DEBUG':
            my_logger.debug(msg)
        elif level=='INFO':
            my_logger.info(msg)
        elif level=='WARNING':
            my_logger.warning(msg)
        elif level=='ERROR':
            my_logger.error(msg)
        elif level=='CRITICAL':
            my_logger.critical(msg)

        #关闭渠道
        my_logger.removeFilter(ch)
        my_logger.removeFilter(fh)

    def debug(self,msg):
        self.my_log(msg,'DEBUG')

    def info(self,msg):
        self.my_log(msg,'INFO')

    def error(self, msg):
        self.my_log(msg,'ERROR')

if __name__ == '__main__':
    pass