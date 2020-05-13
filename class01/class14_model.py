# -*- coding: utf-8 -*-
# @Time     : 2020/3/18 21:51
# @Author   : Monster
# @Email    : 945534456@qq.com
# @File     : class14_model.py


# 【14】模块
# 怎样看函数
#怎么引入不同的模块
#为什么学python 非常丰富的库

# a=[1,2,3,4]
# print(a.pop())

#---------------->>>>>>>>>分割线<<<<<<<<<<<<<--------------
##第一步安装：
# a:在线安装。打开cmd
# 1)pip install 模块名
# 2）使用国内源进行安装  pip install 国内源地址 模块名
# 3）file-setting-project interpreter -->+---

# b:离线安装
#自己去python官网或者是网上找到离线安装包
#1：解压：2：拷贝解压后的文件到python安装路径
#3：在cmd 里面利用cd 一级一级进入到安装包文件路径  安装文件 setup.py
#python setup.py install


#---------------->>>>>>>>>分割线<<<<<<<<<<<<<--------------

## 我的文件安装到哪里去了？
# Lib(自带) /lib-->site packages(第三方库)


#---------------->>>>>>>>>分割线<<<<<<<<<<<<<--------------

##怎么用?
#1:自己写的 怎么导入  #一层一层使得拨开

# import class01.class11_function
# a = class01.class11_function.add(1,101)
# print(a)

# from class01 import class11_function
# a = class11_function.add(1,101)
# print(a)

# if __name__ == '__main__':   #mian的使用 ->class11
#引入模块，会执行该模块下的其他（如测试）代码，所以在要引入的模块下用上面的mian，
# 要执行的测试代码写在mian下面，这样引入后就不会执行其他多余代码


#2：Python自带的 或者是后面安装的第三方库 怎么引用 -->简单点
# 1） import  2) from ......import....
import email.mime.base  #一层一层使得拨开

from email.mime import base  #推荐使用
#from ..import 至少具体到模块名
