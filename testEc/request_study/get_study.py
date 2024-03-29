# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author:   wsj QQ：3512937625
# @Time:   2021-07-04
# @Copyright：
import requests

def get():
    # 针对接口发起调用，需要知道接口有哪些信息
    #接口地址，请求头信息，请求参数，接口请求方式
    url = ""
    #这个接口没有特殊的头信息，所以不写

    #查询参数，通常可以使用params来代表，将其定义成字典
    params ={

    }

    #发起接口调用，得到响应结果
    #resp是响应对象，包括了响应头信息，响应状态码，响应body体信息
    resp = requests.get(url=url,params=params)

    #获取响应状态码
    status_code = resp.status_code
    print(f'响应状态码是：{status_code}')
    #获取响应body信息的字符出纳类型数据
    resp_text=resp.text
    print(f'响应body信息的字符出纳类型数据：{resp_text}')

    #获取响应body信息的json类型数据，对应的就是python里的字典嵌套或者列表嵌套
    resp_json =resp.json()
    print(f'取响应body信息的json类型数据:{resp_json}')


if __name__ == '__main__':
    get()

