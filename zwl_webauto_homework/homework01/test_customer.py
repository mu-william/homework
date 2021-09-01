# encoding    : utf-8 -*-                            
# @author     : william                              
# @software   : PyCharm      
# Time        : 2021/7/13 16:20
import json
from selenium import webdriver


class Testwechat():

    def setup_class(self):
        '''
        复用已有浏览器
        1.需要在chrome下打开cmd，运行“chrome --remote-debugging-port=9222”
        2.执行以下代码：“chrome_args = webdriver.ChromeOptions()
                      chrome_args.debugger_address = "127.0.0.1:9222"”
        3.webdriver.Chrome需要加上参数options
        ps：不要打开多个chrome浏览器
        :return:
        '''
        chrome_args = webdriver.ChromeOptions()
        chrome_args.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome()

    # def teardown_class(self):
    #     self.driver.quit()

    def test_Open(self):
        self.driver.get("https://work.weixin.qq.com/")
        self.driver.maximize_window()

    # cookies登录
    def test_cookie(self):
        # 获取当前浏览器页面cookies
        # browser_cookies = self.driver.get_cookies()
        # # 以文件流形式将cookies写进文件中
        # with open("cookies.json","w") as f:
        #     # 将cookies存到json文件
        #     json.dump(browser_cookies,f)

        # 向浏览器具体的页面添加cookies
        self.driver.get("https://work.weixin.qq.com/")
        # 以文件流形式读取json中的cookies
        with open("cookies.json","r") as f:
            # 读取cookies
            cookies = json.load(f)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame")

        # 点击客户联系
        cus_contact = self.driver.find_element_by_id('menu_customer')
        cus_contact.click()









