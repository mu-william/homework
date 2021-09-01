# encoding    : utf-8 -*-                            
# @author     : william                              
# @software   : PyCharm      
# Time        : 2021/7/13 15:09
import pytest

from zwl_pytesthomework.calculator import Calculator
from zwl_pytesthomework.homework1.filemanage import Filemanage


class TestOperation:
    def setup_class(self):
        self.calc = Calculator()
        print("\n开始计算")

    def teardown_class(self):
        self.calc = Calculator()
        print("\n计算结束")

    # 加法
    @pytest.mark.parametrize("a,b,expect,n",Filemanage().OpenFile("add")[0],ids= Filemanage().OpenFile("add")[1])
    def test_add(self,a,b,expect,n):
        try:
            result = self.calc.add(a,b)
            assert  result == expect
            print(f"add运算第{n}条测试用例通过")

        except Exception as e:
            print(f"add运算第{n}条测试用例失败")

    # 减法
    @pytest.mark.parametrize("a,b,expect,n", Filemanage().OpenFile("sub")[0], ids=Filemanage().OpenFile("sub")[1])
    def test_sub(self,a,b,expect,n):
        try:
            result = self.calc.sub(a, b)
            assert result == expect
            print(f"sub运算第{n}条测试用例通过")
        except Exception as e:
            print(f"sub运算第{n}条测试用例失败")

    # 乘法
    @pytest.mark.parametrize("a,b,expect,n", Filemanage().OpenFile("mul")[0], ids=Filemanage().OpenFile("mul")[1])
    def test_mul(self,a,b,expect,n):
        try:
            result = self.calc.mul(a, b)
            assert result == expect
            print(f"mul运算第{n}条测试用例通过")
        except Exception as e:
            print(f"mul运算第{n}条测试用例失败")

    # 除法
    @pytest.mark.parametrize("a,b,expect,n", Filemanage().OpenFile("div")[0], ids=Filemanage().OpenFile("div")[1])
    def test_div(self,a,b,expect,n):
        try:
            result = self.calc.div(a, b)
            assert result == expect
            print(f"div运算第{n}条测试用例通过")
        except Exception as e:
            print(f"div运算第{n}条测试用例失败")