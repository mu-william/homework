# encoding    : utf-8 -*-                            
# @author     : william                              
# @software   : PyCharm      
# Time        : 2021/7/15 11:15
from zwl_webauto_homework.homework02.home_page import HomePage


class TestAddDepartMent():
    # 实现部门添加测试
    def test_addDepartment(self):
        # 实例化首页(HomePage类)
        home = HomePage()
        result = home.homePage().ConTact().addDepartMent().dept_list()
        assert result == True
