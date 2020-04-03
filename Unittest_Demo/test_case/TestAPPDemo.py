#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @date: 2020/4/2 16:57 
# @name: Test_AppDemo
# @author：wongqin
#pip install Appium-Python-Client

from appium import webdriver
import unittest,time
'''
ChromeAPP     com.android.chrome，com.google.android.apps.chrome.Main
微信app       com.tencent.mm,com.tencent.mm.ui.LauncherUI
同程旅游app   com.tongcheng.android,com.tongcheng.android/.LoadingActivity
获取apk方法：https://blog.csdn.net/zw1_csdn/article/details/95105457

'''

class Test_AppDemo(unittest.TestCase):

    def setUp(self):
        desired_caps = {
            'platformName': 'Android', # 平台名称
            'platformVersion': '9.0.0',  # 系统版本号
            'deviceName': '10.101.54.105:15893',  # 设备名称。如果是真机，在'设置->关于手机->设备名称'里查看
            'appPackage': 'com.tongcheng.android',  # apk的包名
            'appActivity': '.LoadingActivity', # activity 名称
            'chromeOptions': {'androidProcess':'com.android.browser'},#平台
            'unicodeKeyboard' : True,#设置编码格式为unicode
            'resetKeyboard' : True,#隐藏手机键盘
            'noReset' : True #非初始化
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps) #连接appium

    def tearDown(self):
        self.driver.quit()#停止

    def test_app_demo(self):
        time.sleep(5)