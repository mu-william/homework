# encoding    : utf-8 -*-                            
# @author     : william                              
# @software   : PyCharm      
# Time        : 2021/7/13 15:25
import pytest


class TestOperation:
    # 加法
    @pytest.mark.run(order=1)
    def test_add(self,get_ope,get_Adddata):
        result = get_ope.add(get_Adddata[0],get_Adddata[1])
        if isinstance(result,float):
            result = round(result,2)
        pytest.assume(result == get_Adddata[2])

    # 除法
    @pytest.mark.run(order=4)
    def test_div(self, get_ope, get_Divdata):
        result = get_ope.div(get_Divdata[0], get_Divdata[1])
        if isinstance(result,float):
            result = round(result,2)
        pytest.assume(result == get_Divdata[2])

    # 减法
    @pytest.mark.run(order=2)
    def test_sub(self, get_ope, get_Subdata):
        result = get_ope.sub(get_Subdata[0], get_Subdata[1])
        if isinstance(result,float):
            result = round(result,2)
        pytest.assume(result == get_Subdata[2])

    # 乘法
    @pytest.mark.run(order=3)
    def test_mul(self, get_ope, get_Muldata):

        result = get_ope.mul(get_Muldata[0], get_Muldata[1])
        if isinstance(result,float):
            result = round(result,2)
        pytest.assume(result == get_Muldata[2])