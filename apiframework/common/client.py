# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author:   wsj QQ：3512937625
# @Time:   2021-07-04
# @Copyright：
'''封装请求对象'''
import jsonpath
import requests
from apiframework.common.logger import GetLogger

class RequestsClient:
    # token =None
    # uuid=None
    # pid= None
    # adress_id=None
    #这个类作为所有单接口测试的基类出现，因此在类中定义好接口需要的各个字段
    def __init__(self):
        #创建日志对象
        self.logger=GetLogger.get_logger()
        #创建session对象
        self.session=requests.session()
        self.host=None
        self.url=None
        self.method=None
        self.headers=None
        self.params=None
        self.json=None
        self.data=None
        self.files=None
        self.resp=None

    #因为对于一个请求有很多不确定的参数，因此采用可变参数进行传递
    #如果init里面定义了一些属性，那么子类可以进行继承+重新进行传递，如果init里面没有
    #定义的属性，那么可以通过send（）里面的kwargs这个不定长参数进行传递
    def send(self,**kwargs):
        if kwargs.get('url')==None:
            kwargs['url']=self.url
        if kwargs.get('method')==None:
            kwargs['method']=self.method
        if kwargs.get('headers')==None:
            kwargs['headers']=self.headers
        if kwargs.get('params')==None:
            kwargs['params']=self.params
        if kwargs.get('data')==None:
            kwargs['data']=self.data
        if kwargs.get('json')==None:
            kwargs['json']=self.json
        if kwargs.get('files') == None:
            kwargs['files'] = self.files
            # 日志 -查看请求的各个值是多少
            for item in kwargs.items():
                self.logger.info('接口信息是:{}'.format(item))
            self.logger.info('准备开始发起请求')
            # 发送请求 获取响应值
            self.resp = self.session.request(**kwargs)
            self.logger.info('接口响应状态码是:{}'.format(self.resp.status_code))
            self.logger.info('接口的响应内容是:{}'.format(self.resp.text))
            return self.resp

    def extract_expr(self, jsonpath_express, index=0):
        '''

        :param index: 代表想要获取目标结果中的第几个数据
        index=0  默认获取第一个数据
        index=1,2... 正常的索引值的获取
        index=-1      想要获取所有的数据，返回一个列表
        :return:
        '''

        if self.resp != None and self.resp != '':
            if index >= 0:
                print("=====")
                print(self.resp.json())
                print(jsonpath_express)
                print(index)
                extract_data = jsonpath.jsonpath(self.resp.json(), jsonpath_express)[index]
                self.logger.info('接口的提取出来的响应内容是:{}'.format(extract_data))
                return extract_data
            elif index == -1:
                extract_data = jsonpath.jsonpath(self.resp.json(), jsonpath_express)
                self.logger.info('接口的提取出来的响应内容是:{}'.format(extract_data))
                return extract_data


if __name__=='__main__':
    #host = "http://192.168.200.123:8080"
    url ='http://192.168.200.123:8080/user/login'
    data = {
        'mobile': 13399321748,
        'password': 'W123456',
        'channel': 'pc'
    }
    kwargs={
        'url':url,
        'method':'post',
         'data':data
    }
    client =RequestsClient()
    resp=client.send(**kwargs)
    print(f'响应状态码是{resp.status_code}')
    print(f'相应的内容是{resp.text}')




