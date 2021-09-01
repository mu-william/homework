# encoding    : utf-8 -*-                            
# @author     : william                              
# @software   : PyCharm      
# Time        : 2021/7/15 11:15
import json

from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage():

    def __init__(self, base_driver=None):
        base_driver: WebDriver
        if base_driver is None:
            self.driver = webdriver.Chrome()
            self._cookies_login()
        else:
            self.driver = base_driver

    # 获取cookie
    def _get_cookie(self):
        # 获取页面cookie
        cookies = self.driver.get_cookies()
        # 将cookies写进cookies.json文件中
        with open("cookies.json", "w") as f:
            json.dump(cookies, f)

    # 将cookie写入浏览器
    def _cookies_login(self):
        # 对声明需要加入cookies的网址
        self.driver.get("https://work.weixin.qq.com/")
        # 将cookie.json文件写入浏览器
        with open("cookies.json", "r") as f:
            cookies = json.load(f)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            # 登录已加入cookies的网址
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame")

    # # 判断元素是否存在
    # def isElementExit(self):
    #     self.driver.find_element(by)
