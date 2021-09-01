# encoding    : utf-8 -*-                            
# @author     : william                              
# @software   : PyCharm      
# Time        : 2021/7/15 11:15
from zwl_webauto_homework.homework02.basepage import BasePage


class addDepartMentPage(BasePage):
    def addDepartMent(self):
        from zwl_webauto_homework.homework02.contact_page import ConTactPage
        return ConTactPage(self.driver)
