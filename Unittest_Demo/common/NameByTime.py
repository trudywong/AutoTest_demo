#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @date: 2020/3/21 10:44 
# @name: NameByTime
# @author：wongqin

import time,os

class NameByTime:
    def __init__(self):
        self.now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))

    def image_name(self):
        image_name = self.now + '.jpg'
        return image_name

    def log_name(self):
        self.now = time.strftime("%Y-%m-%d",time.localtime(time.time()))
        log_name = self.now + '.log'
        return log_name

    def html_name(self):
        html_name = self.now + '.html'
        return html_name