# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author:   wsj QQ：3512937625
# @Time:   2021-07-04
# @Copyright：
from apiframework.keywords.keywords_run import run
from apiframework.common.client import RequestsClient
from apiframework.keywords.keywords_util import get_cases_infos, get_global_variables, get_all_cases,get_api_infos
import pytest
import allure

client=RequestsClient()
#获取所有api信息
get_api_infos()

#获取所有变量信息
get_global_variables()

#获取所有测试用例
all_cases = get_all_cases()

@allure.title('{casename}')
@pytest.mark.parametrize('casename',all_cases)
def test_run(casename):
    # 调用核心的run方法
    run(client,casename)
