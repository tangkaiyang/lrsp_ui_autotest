# -*- coding:UTF-8 -*-

from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import unittest
import time
import os

# ============定义发送邮件=============
def send_mail(file_new):
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()

    send = "m17757989076@136.com"
    send_pwd = "tangkaiyang123"
    receive = "945541696@qq.com"

    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['Subject'] = Header("自动化测试报告", 'utf-8')
    msg['from'] = send
    msg['to'] = receive

    smtp = smtplib.SMTP()
    smtp.connect("smtp.163.com")
    smtp.login(send, send_pwd)
    smtp.sendmail(send, receive, msg.as_string())
    smtp.quit()
    print("email has send out!")

# =================查找测试报告目录,找到最新的测试报告文件===============
def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key = lambda fn: os.path.getmtime(testreport + "\\" + fn))
    file_new = os.path.join(testreport, lists[-1])
    print(file_new)
    return  file_new

if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = './report/' + now + 'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='林润审批系统自动化测试报告',
                            description='环境: windows7 浏览器:chrome')
    discover = unittest.defaultTestLoader.discover('./test_case',
                                                   pattern='*_sta.py')
    runner.run(discover)
    fp.close() # 关闭生成的报告
    file_path = new_report('./report/') # 查找新生成的报告
    send_mail(file_path) # 调用发邮件模块
