#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @date: 2020/4/3 15:30 
# @name: JSOption
# @author：wongqin
'''
自动化中，一些操作借助于js，效果比较理想
'''

class JSOption:

    #js_locator指的是js定位,滚动页面到指定元素
    def scroll_to_element(self,driver,js_locator):
        js = '$("'+ js_locator +'")[0].scrollIntoView()'
        driver.execute_script(js)

    #注意，这里传的是js定位集合
    def circular_click(self,driver,js_locators):
        len = driver.execute_script('return $("'+ js_locators +'").length')
        i = 0
        while i < len:
            driver.execute_script('$("'+ js_locators +'")['+ str(i) +'].click()')
            i += 1



