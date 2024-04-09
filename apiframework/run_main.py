# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author:   wsj QQ：3512937625
# @Time:   2021-07-04
# @Copyright：


import pytest
import os
if __name__ == '__main__':
    # 目的:把命令行输入的命令封装到python脚本中(思考)
    #1.pytest在python文件中执行
    pytest.main()
    # 2.allure generate .\reports\shop   -o ./reports/html --clean
    # python中执行命令行参数 os.system()
    # os.system('allure generate .\\reports\\shop   -o ./reports/html --clean')
    #-sv  --alluredir ./reports/shop --clean-alluredir