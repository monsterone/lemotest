# -*- coding: utf-8 -*-
# @Time     : 2020/3/10 22:45
# @Author   : Monster
# @Email    : 945534456@qq.com
# @File     : class6_dict.py

#【6】: 字典 dict 符号{}  无序（py3.7后打印顺序一致）
# 1：可以存在空字典a={} #print(type(a))
# 2:字典里面数据存储的方式： key:value
# 3:字典里面的元素 根据逗号来进行分割  #print(len(a))
# 4:字典里面的key是惟一的

#---------------->>>>>>>>>分割线<<<<<<<<<<<<<--------------

a={"class":"python",
   "student":119,
   "teacher":"girl",
   "t_age":20,
   "score":[99,88.8,100.5]}

#（1）字典取值：字典[key]   # print(a["score"])

#（2）删除：pop(key)指明删除的值的key
# a.pop("teacher")
# res = a.pop("teacher")  #girl #返回删除的值

#（3）新增: a[新key]=value 字典里面不存在的key
# a["name"] = "怪兽"  #print(a)

#（4）修改 a[已经存在的key]=新value 字典里面已经存在的key
# a["t_age"]=18  #print(a)



