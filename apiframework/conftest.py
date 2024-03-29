# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author:   wsj QQ：3512937625
# @Time:   2021-07-04
# @Copyright：

import jsonpath
import pytest
from apiframework.api.buyer.login_api import LoginApi
from apiframework.api.base_api import BuyerBaseApi
#hook函数f
def pytest_collection_modifyitems(items):

    #item表示每个测试用例，解决用例名称中文显示问题
    for item in items :
        item.name = item.name.encode('utf-8').decode("unicode-escape")
        item._nodeid =item._nodeid.encode("utf_8").decode("unicode-escape")

'''
fixture函数可以实现setup的功能，在测试用例之前执行内容，初始化
功能更强大，可以随便取名字
@pytest.fixture(scope="",autouse=False)
默认autouse是False,需要手动引用
True，自动引用
session:pytest发起请求到结束 只会执行一次
function：函数级别的测试用例和方法级别的测试用例都用这个范围
class:你引用fixture函数的class类，就会执行一次
module: 你引用fixture函数的python文件，就会执行一次

引用:
把fixture装饰的函数的名字当做参数传递到测试用例当中就是调用了
'''

@pytest.fixture(scope='function',autouse=False)
def login():
    #依赖登录接口
    buyerapi=LoginApi()
    resp = buyerapi.send()
    BuyerBaseApi.token = jsonpath.jsonpath(resp.json(),'$data.token')[0]
    print('========login=======')


@pytest.fixture(scope='function',autouse=True)
def seller_login():
    # 登录
    sellerloginapi = LoginApi()
    sellerloginapi.send()
    # 数据提取
    BuyerBaseApi.token = sellerloginapi.extract_expr('$.data.token')