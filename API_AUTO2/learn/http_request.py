# -*- coding: utf-8 -*-
# @Author   : Monster
# @File     : http_request.py

import requests

register_url='http://120.78.128.25:8080/futureloan/mvc/api/member/register'
register_data={"mobilephone":"15096096666","pwd":"123456","regname":"haha"}

res=requests.get(register_url,register_data)
print("text解析的结果:",res.text)
print("json解析的结果:",res.json())
print("请求头：",res.request.headers)

login_url='http://120.78.128.25:8080/futureloan/mvc/api/member/login'
login_data={"mobilephone":"15096096666","pwd":"123456"}

res=requests.get(login_url,login_data)
print("text解析的结果:",res.text)
print("json解析的结果:",res.json())