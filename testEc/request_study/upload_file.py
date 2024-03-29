# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author:   wsj QQ：3512937625
# @Time:   2021-07-04
# @Copyright：
import requests
def upload():
    url = "http://192.168.200.123:8080/file/upload"
    headers = {
        "Accept": "application / json, text / javascript",
        "Content - Type": "multipart / form - data",
        "boundary" : "----WebKitFormBoundarysQDeAXV2tMpe2K8d"
    }
    # 文件参数
    files = {
        "file":('2.png',open(file=r'E:\图片\2.png',mode='rb'),'image/png'),
        # "Content - Disposition":" form - data",
        # "name" :"proxyfile"

    }
    resp = requests.post(url=url,files=files,headers=headers)
    status_code = resp.status_code
    print(f'响应的code：{status_code}')
    # 获取响应body信息的字符串类型数据
    # resp_text = resp.text
    # print(f'body信息的字符串类型数据为：{resp_text}')
    # # 获取响应body信息的json类型数据，对应的就是python里的字典嵌套或者列表嵌套
    # resp_json = resp.json()
    # print(f'取响应body信息的json类型数据:{resp_json}')

if __name__ == '__main__':
    upload()

