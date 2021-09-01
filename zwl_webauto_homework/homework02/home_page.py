# encoding    : utf-8 -*-                            
# @author     : william                              
# @software   : PyCharm      
# Time        : 2021/7/15 11:14
from zwl_webauto_homework.homework02.basepage import BasePage
from zwl_webauto_homework.homework02.contact_page import ConTactPage


class HomePage(BasePage):

    def homePage(self):

        return ConTactPage(self.driver)
