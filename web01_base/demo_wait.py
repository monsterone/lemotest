# -*- coding: utf-8 -*-
# @Author   : Monster
# @File     : demo_wait.py
from selenium import webdriver
import time
driver = webdriver.Chrome()

#等待

#sleep

#隐性

#显性


##iframe
#切换一：切换iframe
driver.switch_to.frame("login_frame_qq")
driver.switch_to.frame(driver.find_element_by_xpath('//iframe[@name="login_frame_qq"]'))
time.sleep(0.5)
driver.find_element_by_id("switch_plogin")

#方式二：iframe 切换
# WebDriverWaite()

#从iframe当中回到默认的页面中
driver.switch_to.default_content()

# driver.switch_to.parent_frame()#回到父级页面（上一级）


#切换二：切换窗口