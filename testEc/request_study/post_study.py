# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author:   wsj QQ：3512937625
# @Time:   2021-07-04
# @Copyright：


import requests

# 登录接口为例
def login_ec():
    # 针对接口发起调用，需要知道接口有哪些信息
    # 接口地址，请求头信息，请求参数，接口请求方式
    url = "http://192.168.200.123:8080/user/login"
    # 接口头信息
    headers = {'Content-Type':'application/x-www-form-urlencoded'}
    # 表单参数
    body = {
        "mobile" : "15117905676",
        "password" : "Wsj@123456",
        "channel" : "pc"

    }
    #发起接口调用，拿到响应结果
    resp = requests.post(url=url, data=body,headers=headers)
    #得到响应状态码
    stats_code = resp.status_code
    print(f'返回响应的状态码为：{stats_code}')
    #获取响应body信息的字符串类型数据
    resp_text = resp.text
    print(f'body信息的字符串类型数据为：{resp_text}')
    # 获取响应body信息的json类型数据，对应的就是python里的字典嵌套或者列表嵌套
    resp_json = resp.json()
    print(f'取响应body信息的json类型数据:{resp_json}')

if __name__ == '__main__':
    login_ec()