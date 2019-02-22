# -*- coding:UTF-8 -*-

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from test_case.page_obj.base import Page
from time import sleep


class login(Page):
    """
    用户登录页面
    """

    url = '/'

    #Action
    username_input_loc = (By.XPATH, """//*[@id="app"]/div/form/div[2]/div/div/input""") # 用户名输入框
    password_input_loc = (By.XPATH, """//*[@id="app"]/div/form/div[3]/div/div/input""") # 密码输入框
    login_button_loc = (By.XPATH, """//*[@id="app"]/div/form/button""") # 登录按钮

    # 输入用户名
    def login_username(self, username):
        self.find_element(*self.username_input_loc).send_keys(username)

    # 输入密码
    def login_password(self, password):
        self.find_element(*self.password_input_loc).send_keys(password)

    # 点击登录按钮
    def login_button(self):
        self.find_element(*self.login_button_loc).click()

    # 定义统一登录入口
    def lrsp_login(self, username="13121907110", password="123456"):
        """获取的用户名和密码登录"""
        self.open()
        self.login_username(username)
        self.login_password(password)
        self.login_button()
        sleep(1)
    # # 登录错误提示弹窗
    # def login_error_hint(self):
    #     return self.switch_to.alert