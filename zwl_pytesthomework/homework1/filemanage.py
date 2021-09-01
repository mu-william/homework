# encoding    : utf-8 -*-                            
# @author     : william                              
# @software   : PyCharm      
# Time        : 2021/7/13 15:10
import yaml


class Filemanage():
    def OpenFile(self,model):
        # 获取当前需要的yaml文件
        File_yaml_path = "F:\py\workplace\hgwz-homework\zwl_pytesthomework\param.yaml"
        # print(File_yaml_path)

        with open(File_yaml_path) as f:
            datas = yaml.safe_load(f)
            # 获取对应运算规则的数据集
            datas_set = datas[model]
            # 每个运算规则都包含整型运算和浮点型运算
            ids = datas["myids"]
            return [datas_set,ids]