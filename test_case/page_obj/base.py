# -*- coding:UTF-8 -*-
class Page(object):
    """
    页面基础类,用于所有页面的继承
    """

    lrsp_url = 'http://release.web.beta.lrwanche.com'

    def __init__(self, selenium_driver, base_url=lrsp_url, parent=None):
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout = 30
        self.parent = parent

    def _open(self, url):
        url = self.base_url + url
        self.driver.get(url)
        # assert self.on_page(), 'Did not land on %s' % url
        # assert关键字assert 表达式[,参数]

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

    def open(self):
        self._open(self.url)
        # 外部通过调用open()调用类内部的_open()

    # def on_page(self):
    #     return self.driver.current_url == (self.base_url + self.url)
        # 判断是否在当前页面

    def script(self, src):
        return self.driver.execute_script(src)
        # 调用JavaScript代码的函数
