#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @date: 2020/4/2 14:59 
# @name: Test_PCdemo
# @author：wongqin

import unittest,time
from selenium import webdriver
from selenium.webdriver.common.by import By
from Unittest_Demo.common.OptionElement import OptionElement
from Unittest_Demo.common.JSOption import JSOption

class Test_PCdemo(unittest.TestCase):

    def setUp(self):
        #初始化一个浏览器，并最大化
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()

    def tearDown(self):
        #关闭浏览器
        self.browser.close()

    def test_pc_demo(self):
        url = 'https://www.ly.com/'
        self.browser.get(url)
        # OptionElement().sendkeys_when_element_contains(self.browser,By.ID,'pt__search_text','1')
        # JSOption().scroll_to_element(self.browser,'.prop3')
        # OptionElement().circular_click_elements(self.browser,By.CSS_SELECTOR,'.prop3 .menuTab>a')
        JSOption().circular_click(self.browser,'#menuNav>li>a')
        time.sleep(1)
