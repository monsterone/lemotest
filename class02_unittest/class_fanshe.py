# -*- coding: utf-8 -*-
# @Time     : 2020/4/2 22:15
# @Author   : Monster
# @Email    : 945534456@qq.com
# @File     : class_fanshe.py

#反射
class GetData:
    Cookie = "atm"

if __name__ == '__main__':

    setattr(GetData,"Cookie","monster") #可以直接把类里面的属性值做修改
    print(getattr(GetData,"Cookie")) #获取属性值 attribute
    print(hasattr(GetData,"Cookie"))  #判断是否有这个属性值
    delattr(GetData,"Cookie")  #删除属性值
    # print(GetData.Cookie)

