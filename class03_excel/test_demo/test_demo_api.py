# -*- coding: utf-8 -*-
# @Time     : 2020/4/4 18:55
# @Author   : Monster
# @Email    : 945534456@qq.com
# @File     : test_demo_api.py

import requests

r = requests.get("http://127.0.0.1:5000/")
result = r.json()
print(result)