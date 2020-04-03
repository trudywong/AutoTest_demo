#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @date: 2020/3/20 21:10 
# @name: PrintScreen
# @author：wongqin

from PIL import ImageGrab
from Unittest_Demo.common import NameByTime

image_dir = './image'

def printscreent():
    im = ImageGrab.grab()
    im.save(image_dir + '\\' +NameByTime.NameByTime().image_name())