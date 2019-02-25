# -*- coding:UTF-8 -*-
from selenium.webdriver import Remote
from selenium import webdriver
import time


# 启动浏览器驱动
def browser():
    driver = webdriver.Chrome()
    # host = '127.0.0.1:4444'  # 运行主机:端口号(本机默认:127.0.0.1:4444)
    # dc = {'platform': 'ANY',
    #       'browserName': 'chrome',
    #       'version': '',
    #       'javascriptEnabled': True}  # 指定浏览器('chrome', 'firefox')
    # driver = Remote(command_executor='http://' + host + '/wd/hub',
    #                 desired_capabilities=dc)
    return driver


if __name__ == '__main__':
    dr = browser()
    dr.get("http://release.web.beta.lrwanche.com")
    time.sleep(5)
    dr.quit()
