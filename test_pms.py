#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/8/27 15:22
# @Author : shlu
# @Site : 
# @File : test_pms.py
# @Software: PyCharm

from config.load_yaml_data import get_yaml_data
from selenium import webdriver
import time
import pytest

class TestPMS():

    def setup(self):
        # 加载浏览器驱动
        self.dr = webdriver.Chrome(r'E:\接口自动化\tools\chromedriver_win32\chromedriver.exe')
        time.sleep(2)
        self.dr.get("https://crm2.ysservice.com.cn/#/userlogin")
        self.dr.maximize_window()
        time.sleep(2)

    def teardown(self):
        time.sleep(2)
        self.dr.close()

    @pytest.mark.parametrize("user_account",get_yaml_data("login.yaml"))
    def test_login(self,user_account):
        print(user_account)
        self.dr.find_element_by_name("userName").send_keys(user_account['uname'])
        time.sleep(1)
        self.dr.find_element_by_name("password").send_keys(user_account['upass'])
        time.sleep(2)
        self.dr.find_element_by_class_name("loginbtnStyle").click()

