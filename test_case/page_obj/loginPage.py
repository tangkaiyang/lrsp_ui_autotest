# -*- coding:UTF-8 -*-

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from .base import Page
from time import sleep


class login(Page):
    """
    用户登录页面
    """

    url = '/'

    #Action
    login_user_loc = (By.XPATH, "//*[@id='app']/div/form/div[2]/div/div/input")
    login_button = (By.XPATH, "//*[@id='app']/div/form/button")

    def lrsp_login(self, username):
        self.find_element(*self.login_user_loc).click()
        sleep(1)
        self.find_element(*self.login_button).click()

    login_username_loc = (By.ID, "")