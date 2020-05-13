# -*- coding: utf-8 -*-
# @Author   : Monster
# @File     : demo_element.py

#元素定位
from selenium import webdriver
driver = webdriver.Chrome()

#id 、classname 、tagname 、name
# link_text、part_link_text
#xpath、css

# xpath
driver.find_element_by_xpath("")
#绝对定位 以 /开头，非常依赖于页面的位置和顺序
#相对定位 以 // 开头 不依赖页面的顺序和位置；只看 整个页面中有没有符合表达式的元素

# //标签名称[@属性名称=值]  //input[@name="phone"]
# 逻辑运算 and or //标签名称[@属性名称=值 and @属性名称=值]  //input[@name="phone" and @datatype="m"]
#层级定位  //div[@id="u1"]/a[@name="tj_login"]

#函数的使用：
#text():元素的text内容
#列：//*[@id="xxx"]//p[text()="xxx"]

# contains(@属性/text(),value):包含函数。
#列：contains(@class,"xxxx")、contains(text(),"xxx")

#逻辑运算
# and 表示条件与
# or 表示条件或
#列：//div[@class="xxx" and contains(@style,"display:visibility")]

#轴定位---截图
#//span[text()=" 烧头啊"]/ancestor::a/following-sibling::div//a
