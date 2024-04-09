# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author:   wsj QQ：3512937625
# @Time:   2021-07-04
# @Copyright：
import requests
from apiframework.api.base_api import BuyerBaseApi

class LoginApi(BuyerBaseApi):
    def __init__(self):
        super().__init__()
        #self.host='http://192.168.200.123:8080' 放到了base_api里面

        self.url=self.host +'/user/login'

        self.data={
            'mobile': '13754327550',
            'password': 'Hmw_9244',
            'channel': 'pc'
        }
        self.session = requests.session()
        self.method = "post"

if __name__ == '__main__':
    buyerapi = LoginApi()
    # 发起请求
    resp = buyerapi.send()
    print(resp.text)