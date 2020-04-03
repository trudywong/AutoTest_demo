#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @date: 2020/3/20 20:39 
# @name: Logging
# @author：wongqin

import logging
from Unittest_Demo.common.NameByTime import NameByTime

log_dir = './logs'

class Logger:

    def __init__(self,clevel = logging.DEBUG,Flevel = logging.DEBUG):
        path = log_dir +'\\' + NameByTime().log_name()
        self.logger = logging.getLogger(path)
        self.logger.setLevel(logging.DEBUG)
        fmt = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
        #设置CMD日志
        sh = logging.StreamHandler()
        sh.setFormatter(fmt)
        sh.setLevel(clevel)
        #设置文件日志
        fh = logging.FileHandler(path)
        fh.setFormatter(fmt)
        fh.setLevel(Flevel)
        self.logger.addHandler(sh)
        self.logger.addHandler(fh)

    def debug(self,message):
        self.logger.debug(message)

    def info(self,message):
        self.logger.info(message)

    def war(self,message):
        self.logger.warn(message)

    def error(self,message):
        self.logger.error(message)

    def cri(self,message):
        self.logger.critical(message)
