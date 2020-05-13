# -*- coding: utf-8 -*-
# @Time     : 2020/3/31 22:02
# @Author   : Monster
# @Email    : 945534456@qq.com
# @File     : http_request.py

import  requests

class HttpRequest():
    '''利用request封装get请求和post请求'''

    def http_request(self,url,data,method,cookie=None):
        """
        :param url: 请求地址http://XX:port
        :param data: 传递的参数 非必填 字典的格式传递参数
        :param method: 请求方式 支持get post 字符串形式的参数
        :param cookie: 请求的时候传递的cookie值
        :return: 返回响应结果的消息实体
        """
        if method.lower() == 'get':
            res = requests.get(url,data,cookies=cookie) #响应结果的消息实体
        else:
            res = requests.post(url,data,cookies=cookie) #响应结果的消息实体
        return res

if __name__ == '__main__':
    # 登录（账号不对，不成功）
    url = "http://120.78.128.25:8765/Index/login.html"
    data = {"mobilephone": "18688773467", "pwd": "123456"}
    res = HttpRequest().http_request(url,data,'post')
    print("登录的结果是：",res.json())  #返回是json（type:str）时采用res.json()解析为字典

    #充值（模拟）
    recharge_url = 'http://...../'
    recharge_data = {"mobilephone": "18688773467", "amount": "1000"}
    recharge_res = HttpRequest().http_request(recharge_url,recharge_data,'get',res.cookies)
    print("充值的结果是：",recharge_res.json())
