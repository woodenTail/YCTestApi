# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author:   wsj QQ：3512937625
# @Time:   2021-07-04
# @Copyright：
import jsonpath
import pytest
from apiframework.api.buyer.getShopProductList import GetShopProduct
from apiframework.api.buyer.addShopProduct import AddShopProduct
from apiframework.common.file_load import read_yaml,read_excel



#读取yaml里面的参数化值
data =read_yaml('/data/ecshop.yml')['addshopproduct']
# print(data)

#读取Excel中参数化的值
# data=read_excel('/data/buyer.xlsx','立即购买')
class TestAddShopProduct:
    # def setup_class(self):##  调用几次登录？？？
    # 	# 依赖登录接口
    # 	buyerapi = LoginApi()
    # 	# 发起请求
    # 	resp = buyerapi.send()
    # 	# 生成token
    # 	BuyerBaseApi.buyer_token = jsonpath.jsonpath(resp.json(), '$.data.token')[0]
    #     BuyerBaseApi.uuid=jsonpath.jsonpath(resp.json(), '$.data.uid')[0]
    #     print(f'获取的uuid值是：{BuyerBaseApi.uuid}')

    @pytest.mark.parametrize('casename,params_name,status_assert,business_assert', data)
    def test_addshopproduct(self, casename, params_name, status_assert, business_assert):
        shopproduct = AddShopProduct()
        shopproduct.data = params_name
        resp = shopproduct.send()  # headers调用token在底层已经调用了

        print(resp.status_code)
        print(resp.text)
        # 断言
        pytest.assume(resp.status_code == status_assert)
        if resp.status_code != 200:
            pytest.assume(jsonpath.jsonpath(resp.json(), '$.errorMsg')[0] == business_assert)


