# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author:   wsj QQ：3512937625
# @Time:   2021-07-04
# @Copyright：
import requests
import json
import hashlib
import jsonpath
host = "http://192.168.200.123:8080"

#登录接口
def login():
    #url
    url =host+'/user/login'

    #请求参数
    #请求参数构造成字典的形式进行传递
    data={
        'mobile': '13399321748',
        'password': 'W123456',
        'channel': 'pc'
    }
    resp =requests.post(url=url,data=data)
    json_resp=resp.json()   #字典
    print(f'登录接口返回的值为：{json_resp}')
    acce_token =jsonpath.jsonpath(resp.json(),"$.data.token")[0]
    uuid=jsonpath.jsonpath(json_resp,"$.data.uid")[0]

    return acce_token,uuid


#新增商品_获取商品接口
def select_shopproduct(acce_token,uuid):
    url=host+'/shop/product/selectAuthProductListByUid'
    # headers = {
    #         'Content - Type': 'application / x - www - form - urlencodedcharset = UTF - 8',
    #         'token':'49af2262a37f450ba13e2ecd8599f7d2'
    #     }
    params={
        'uid':'uuid[1]' ,
        'token':'acce_token[0]'

    }
    res=requests.post(url=url,params=params)
    json_res=res.json()

    print(f'获取商品返回的值为：{json_res}')
    #$print(res.status_code)
    return res
    # pid=jsonpath.jsonpath(json_res,"$.data[4].pid")[0]
    # return pid



#新增商品_获取地址接口
def select_address(acce_token,uuid):
    url = host+f'/user/address/selectUserAddressByUid?uid={uuid[1]}&token={acce_token[0]}&addressType=2'
    data = {
        'uid': uuid[1],
        'token': acce_token,
        'addressType':2
    }
    resp=requests.session().request(method='post',url=url,data=data)
    resp_json=resp.json()
    address_id=jsonpath.jsonpath(resp_json,"$.data[3].id")[0]
    return address_id
    print(resp_json)


#新增商品
def add_shopproduct(acce_token,uuid,pid,adress_id):
    url =host+'/shop/product/addShopProduct'
    headers={
        'Content - Type': 'application / x - www - form - urlencodedcharset = UTF - 8',
        'token':'49af2262a37f450ba13e2ecd8599f7d2'
    }
    data={
        'productId': pid,
        'stock': '55',
        'unit': '吨',
        'price': '5',
        'effectiveTime': 'Sat Aug 14 2021 23:59:59 GMT+0800',
        'quality': '测试',
        'contactTel': '6666666',
        'minBuy': '6',
        'addressId': adress_id,
        'shipmentDate': '6',
        'deliveryStyle': '1',
        'payStayle': '2',
        'status':'0' ,
        'uid': uuid[1],
        'token': acce_token,
        'type':'2'
    }
    res=requests.post(url=url,data=data)
    json_res = res.json()
    print(f'新增商品接口返回的值为：{json_res}')


if __name__=='__main__':
    login()
    acce_token =login()
    uuid=login()
    print(f'提取的值为：{acce_token}')
    print("uuid:",uuid[1])
    select_shopproduct(acce_token,uuid)
    pid=select_shopproduct(acce_token,uuid)
    print(f'获取的商品pid为：{pid}')
    select_address(acce_token, uuid, )
    adress_id=select_address(acce_token, uuid)
    print(f'获取的地址id为：{adress_id}')
    add_shopproduct(acce_token,uuid,pid,adress_id)

