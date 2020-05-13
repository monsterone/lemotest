# -*- coding: utf-8 -*-
# @Author   : Monster
# @File     : run.py

#执行代码入口
from tools.do_excel import DoExcel
from tools.http_request import HttpRequest

data_url=r"D:\ZPython\python_hm\lemotest\API_AUTO2\test_data\test_h1.xlsx"
def run(test_data):

    for item in test_data:
        print("正在测试的用例是{0}".format(item["title"]))
        res = HttpRequest().http_request(item["url"],eval(item["data"]),item["method"])
        print("请求的结果是是{0}".format(res.json()))
        DoExcel(data_url, "python").write_back(item["case_id"]+1,str(res.json()))

test_data=DoExcel(data_url,"python").get_data()

run(test_data)