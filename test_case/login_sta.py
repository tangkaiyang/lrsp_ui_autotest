# -*- coding:UTF-8 -*-

from time import sleep
import unittest, random, sys
from test_case.models import myunit, function
from test_case.page_obj.loginPage import login


class LoginTest(myunit.MyTest):
    """林润审批系统登录测试"""

    # 测试用户登录
    def user_login_verify(self, username="", password=""):
        login(self.driver).lrsp_login(username, password)

    def test_login(self):
        """用户名密码正确"""
        self.user_login_verify(username="13121907110", password="123456")
        sleep(2)
        po = login(self.driver)
        function.insert_img(self.driver, "登录")


if __name__ == '__main__':
    unittest.main()
