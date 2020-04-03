#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @date: 2020/4/2 18:46 
# @name: Wait
# @author：wongqin

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Unittest_Demo.common.Logger import Logger
from Unittest_Demo.common.PrintScreen import printscreent

class OptionElement:

    #判断元素存在时，则点击
    def click_when_element_clickable(self,driver,by,locator):
        try:
            if WebDriverWait(driver,5).until(EC.element_to_be_clickable((by,locator))):
                driver.find_element(by,locator).click()
        except:
            Logger().error("元素：" + str(locator) + "，操作:当元素出现就点击失败！" )
            printscreent()

    #判断元素存在时，则点击并输入内容
    def sendkeys_when_element_contains(self,driver,by,locator,text):
        try:
            if WebDriverWait(driver,5).until(EC.element_to_be_clickable((by,locator))):
                driver.find_element(by,locator).click()
                driver.find_element(by,locator).send_keys(text)
        except:
            Logger().error("元素：" + str(locator) + "，操作:当元素出现就点击并输入内容失败！" )
            printscreent()

    #循环点击,注意一下：如果页面刷新了，这个就不适用（url发生变化）
    def circular_click_elements(self,driver,by,locators):
        els = driver.find_elements(by,locators)
        if(len(els)>0):
            for el in els:
                el.click()
        else:
            Logger().error("元素集：" + str(locators) + "，操作:长度小于1，无法操作！" )
            printscreent()


