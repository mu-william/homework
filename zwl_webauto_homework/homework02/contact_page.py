# encoding    : utf-8 -*-                            
# @author     : william                              
# @software   : PyCharm      
# Time        : 2021/7/15 11:15
from zwl_webauto_homework.homework02.add_department_page import addDepartMentPage
from zwl_webauto_homework.homework02.basepage import BasePage


class ConTactPage(BasePage):
    def ConTact(self):

        return addDepartMentPage(self.driver)

    def dept_list(self):
        return True
