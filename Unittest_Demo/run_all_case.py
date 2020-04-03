#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @date: 2020/3/19 19:50 
# @name: run_all_case
# @author：wongqin

import unittest,os
from Unittest_Demo.common import NameByTime,HTMLTestRunnerNew
from Unittest_Demo.common.SendMail import SendMail

# test_dir = './test_case'
discover = unittest.defaultTestLoader.discover(start_dir='./test_case',pattern='TestP*.py')

if __name__ == "__main__":
    report_dir = './report'
    os.makedirs(report_dir,exist_ok=True)
    html_name = NameByTime.NameByTime().html_name()
    with open(report_dir+ '/' +html_name,'wb+') as f:
        runner =HTMLTestRunnerNew.HTMLTestRunner(stream=f,verbosity=2,title='html测试报告',description='测试报告',tester='trudy')
        runner.run(discover)

    # SendMail().smtplib(os.path.abspath('.') + '/report/' +html_name)#邮件发送，QQ邮箱
    # SendMail().outlook(os.path.abspath('.') + '/report/' +html_name)#邮件发送，outlook邮箱