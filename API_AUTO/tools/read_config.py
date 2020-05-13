# -*- coding: utf-8 -*-
# @Time     : 2020/4/8 23:58
# @Author   : Monster
# @Email    : 945534456@qq.com
# @File     : read_config.py

import configparser

class ReadConfig(object):
    def read_config(self,file_name,section,option):
        cf = configparser.ConfigParser()
        cf.read(file_name,encoding='utf-8')
        return cf.get(section,option)

if __name__ == '__main__':
    res = ReadConfig().read_config('case.config','MODE','mode')
    print(res)