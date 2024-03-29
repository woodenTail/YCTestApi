# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author:   wsj QQ：3512937625
# @Time:   2021-07-04
# @Copyright：
import requests
import jsonpath
from apiframework.api.buyer.login_api import LoginApi
from apiframework.api.buyer.getShopProductList import GetShopProduct
from apiframework.api.buyer.selectUser_address import SelectUserAddress
from apiframework.api.base_api import BuyerBaseApi


#发布求购接口
class AddWantToBuy(BuyerBaseApi):
    def __init__(self):
        super().__init__()
        #self.host='http://192.168.200.123:8080'

        self.url=self.host +'/shop/product/addWantToBuy'
        self.data={
            'productId': BuyerBaseApi.pid,
            'minBuy': '556',
            'unit': '吨',
            'deliveryStyle': '1',
            'effectiveTime': 'Tue Nov 29 2021 23:59:59 GMT+0800',
            'quality': '测试',
            'companyName': '宝鸡有一群怀揣着梦想的少年相信在牛大叔的带领下会创造生命的奇迹网络科技有限公司',
            'addressId': BuyerBaseApi.adress_id,
            'contactTel': '151179056765',
            'status':'1' ,
            'uid': BuyerBaseApi.uuid,
            'type':'1'
    }
        self.session = requests.session()
        self.method = "post"

if __name__ == '__main__':
    buyerapi = LoginApi()
    # 发起请求
    resp = buyerapi.send()
    print(resp.text)
    token = jsonpath.jsonpath(resp.json(), "$.data.token")[0]  # 获取的是列表，因此用[0]得到具体的值
    uuid = jsonpath.jsonpath(resp.json(), "$.data.uid")[0]
    BuyerBaseApi.token = token
    BuyerBaseApi.uuid = uuid
    # print(f'token的值是{token}')
    print(f'token的值是{BuyerBaseApi.token}')
    print(f'uuid的值是{BuyerBaseApi.uuid}')

    # 调用获取商品接口
    selectproduct = GetShopProduct()
    resp = selectproduct.send()
    pid = jsonpath.jsonpath(resp.json(), "$.data[4].pid")[0]
    BuyerBaseApi.pid = pid
    print(f'获取的商品pid是：{BuyerBaseApi.pid}')

    # 获取地址接口

    selecadress = SelectUserAddress()
    resp = selecadress.send()
    address_id = jsonpath.jsonpath(resp.json(), "$.data[1].id")[0]
    BuyerBaseApi.adress_id = address_id
    print(f'获取的地址address_id是{BuyerBaseApi.adress_id}')

    resp=AddWantToBuy().send()
    print(resp.text)