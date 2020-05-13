# -*- coding: utf-8 -*-
# @Time     : 2020/3/27 21:59
# @Author   : Monster
# @Email    : 945534456@qq.com
# @File     : http_request1.py

# python 来完成http请求 get post
#requests 第三方库

import requests

"""
#get 请求
url = "http://120.78.128.25:8765/Index/login.html"
res = requests.get(url) #返回一个消息实体
print(res)

# 响应头 响应状态码 响应报文
print("响应头:",res.headers)
print("响应状态码:",res.status_code)
print("响应正文:",res.text) #html、json、xml
"""

#post请求
url = "http://120.78.128.25:8765/Index/login.html"
header = {'User-Agent':'Mozilla/5.0'} #这个是伪装的
data = {"mobilephone":"18688773467","pwd":"123456"}
res = requests.post(url,data)  #返回一个消息实体
print(res)
print("响应头:",res.headers)
print("响应状态码:",res.status_code)
# print("响应正文1:",res.text,type(res.text)) # str    json
# print("响应正文2:",res.json(),type(res.json())) #dict   json  #如果返回是json格式，可用res.json()解析为字典
# print("**cookies**:",res.cookies)
# print("**cookies**:",res.cookies['JSESSIONID']) #类字典形式  ，可用取到值

print("请求头：",res.request.headers)



#图片 短信
#1：屏蔽他
#2：万能的
#3： 数据库查实时的
#4：手动填


#https 验证忽略
# requests.get(url,data,verify=False)









