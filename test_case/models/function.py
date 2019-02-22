# -*- coding:UTF-8 -*-
from selenium import webdriver
import os

# 截图函数
def insert_img(driver, file_name):
    base_dir = os.path.dirname(os.path.dirname(__file__)) #即.../test_case文件夹
    # __file__用来获得模块所在的路径的,如果在控制台下直接使用print(__file__)报错,此时没有脚本执行,未定义__file__
    # dirname 返回当前所在目录
    base_dir = str(base_dir)
    base_dir = base_dir.replace('\\', '/')
    # base = base_dir.split('/test_case/')[0]
    base = os.path.dirname(base_dir)
    file_path = str(base) + "/report/image" + file_name
    driver.get_screenshot_as_file(file_path)

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("http://release.web.beta.lrwanche.com")
    insert_img(driver, 'lisp.png')
    driver.quit()
# dir_name = os.path.dirname(__file__)
# print(os.path.dirname(os.path.dirname(__file__)))
# print(os.path.dirname(__file__))
# print(__file__)
# dir_name1=dir_name.replace('\\', '/')
# print(dir_name+'\n'+dir_name1)
# n = 0
# dir = os.path.dirname(__file__)
# print(dir)
# while n < 5:
#     dir = os.path.dirname(dir)
#     print(dir)
#     n = n + 1