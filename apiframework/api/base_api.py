# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author:   wsj QQ：3512937625
# @Time:   2021-07-04
# @Copyright：

from apiframework.common.client import RequestsClient
from apiframework.common.file_load import read_yaml

class BuyerBaseApi(RequestsClient):
    token = None
    uuid = None
    pid = None
    adress_id =None
    ids = None
    rannum=None
    def __init__(self):
        #继承有两种方式
        #RequestsClient().__init__()
        super().__init__()
        # self.host = 'http://192.168.200.123:8080'
        self.host = read_yaml('/config/http.yml')['host']


