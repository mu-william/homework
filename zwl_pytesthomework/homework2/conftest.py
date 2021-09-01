# encoding    : utf-8 -*-                            
# @author     : william                              
# @software   : PyCharm      
# Time        : 2021/7/13 15:23
import pytest
import yaml
from zwl_pytesthomework.calculator import Calculator


@pytest.fixture(scope="module")
def get_ope():
    print("开始计算")
    operation = Calculator()
    yield operation
    print("结束计算")


def filemanage(model):
    # 获取当前所在文件目录的路径
    File_yaml_path = "F:\py\workplace\hgwz-homework\zwl_pytesthomework\param.yaml"

    with open(File_yaml_path) as f:
        Datas = yaml.safe_load(f)
        Datas_set = Datas[model]
        myids = Datas["myids"]
        return [Datas_set, myids]


@pytest.fixture(params=filemanage("add")[0], ids=filemanage("add")[1])
def get_Adddata(request):

    data = request.param
    # print(data)
    yield data



@pytest.fixture(params=filemanage("sub")[0], ids=filemanage("sub")[1])
def get_Subdata(request):
    data = request.param
    # print(data)
    yield data


@pytest.fixture(params=filemanage("mul")[0], ids=filemanage("mul")[1])
def get_Muldata(request):
    data = request.param
    # print(data)
    yield data



@pytest.fixture(params=filemanage("div")[0], ids=filemanage("div")[1])
def get_Divdata(request):
    data = request.param
    # print(data)
    yield data
