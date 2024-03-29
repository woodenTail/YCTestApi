# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author:   wsj QQ：3512937625
# @Time:   2021-07-04
# @Copyright：
import requests
import jsonpath
from apiframework.api.buyer.login_api import LoginApi
from apiframework.api.base_api import BuyerBaseApi

#获取地址接口
class SelectUserAddress(BuyerBaseApi):
    def __init__(self):
        super().__init__()
        #self.host='http://192.168.200.123:8080'

        self.url=self.host +f'/user/address/selectUserAddressByUid?uid={BuyerBaseApi.uuid}&token={BuyerBaseApi.token}&addressType=2'

        self.data={
             'uid':BuyerBaseApi.uuid,
             'token':BuyerBaseApi.token,
             'addressType':'2'
        }
        self.session = requests.session()
        self.method = "post"

if __name__ == '__main__':
    buyerapi = LoginApi()
    # 发起请求
    resp = buyerapi.send()
    print(resp.text)
    token=jsonpath.jsonpath(resp.json(),"$.data.token")[0]  #获取的是列表，因此用[0]得到具体的值
    uuid = jsonpath.jsonpath(resp.json(), "$.data.uid")[0]
    BuyerBaseApi.token=token
    BuyerBaseApi.uuid=uuid
    #print(f'token的值是{token}')
    print(f'token的值是{BuyerBaseApi.token}')
    print(f'uuid的值是{BuyerBaseApi.uuid}')
    print(SelectUserAddress().data)
    resp = SelectUserAddress().send()
    print(resp.status_code)
    print(SelectUserAddress().url)
    address_id = jsonpath.jsonpath(resp.json(), "$.data[1].id")[0]
    print(address_id)
    print(resp.text)