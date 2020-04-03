#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @date: 2020/3/20 15:07 
# @name: seng_mail
# @author：wongqin

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
import win32com.client as win32
from Unittest_Demo.config import setting
import datetime
from Unittest_Demo.common.Logger import Logger

class SendMail:

    def __init__(self):
        self.Subject = str(datetime.datetime.now())[0:19] + ' 自动化测试报告'          #邮件主题

    '''outlook直接调用本机的outlook邮箱进行发送邮件，所以，无需配置邮箱的登录名和密码，直接发送'''
    def outlook(self,filename):
        try:
            outlook = win32.Dispatch('Outlook.Application')
            mail = outlook.CreateItem(0) # 0: olMailItem
            mail.To = setting.mail_date['addr'] #收件人
            # mail.CC = setting.mail_date['cc']   #抄送对象
            mail.Subject = self.Subject
            mail.BodyFormat = 2          # 2: Html format
            mail.Attachments.Add(filename)
            htmlf = open(filename,'r',encoding='utf-8')
            htmlcont = htmlf.read()
            mail.HTMLBody  = htmlcont
            htmlf.close()
            mail.Send()
            Logger().info('Success:outlook邮件发送成功！')
        except BaseException:
            Logger().error('Error:outlook邮件发送失败！')

    ''' 调用其他类型邮件，例如qq'''
    def smtplib(self,filename):
        try:
            smtpObj = smtplib.SMTP_SSL(setting.mail_date['server'],setting.mail_date['port'])#配置服务器
            smtpObj.login(setting.mail_date['sender'],setting.mail_date['code'])
            htmlf = open(filename,'r',encoding='utf-8')
            htmlcont = htmlf.read()
            mail_body = htmlcont #邮件正文内容
            htmlf.close()
            #邮件发送者，接受者，主题
            message = MIMEMultipart()#邮件内容,中间一个参数控制发送邮件格式
            message['From'] = Header('自动化测试报告：<' + setting.mail_date['sender'] +'>','utf-8')
            message['To'] = Header('Pyhon接受邮件<' + setting.mail_date['addr2'] + '>','utf-8')
            message['Subject'] = Header(self.Subject,'utf-8') #邮件主题
            message.attach(MIMEText(mail_body,'html','utf-8'))
            # 构造附件1，传送当前目录下的 test.txt 文件
            att1 = MIMEText(open(filename,'rb').read(), 'base64', 'utf-8')
            att1["Content-Type"] = 'application/octet-stream'
            # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
            att1["Content-Disposition"] = 'attachment; filename="test_report.html"'
            message.attach(att1)
            smtpObj.sendmail(setting.mail_date['sender'],setting.mail_date['addr2'],message.as_string())
            Logger().info('Success:QQ邮件发送成功！')
        except smtplib.SMTPException:
            Logger().error('Error:QQ邮件发送失败！')
