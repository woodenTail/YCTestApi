# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author:   wsj QQ：3512937625
# @Time:   2021-07-04
# @Copyright：

import pymysql

from apiframework.common.file_load import read_yaml
from apiframework.setting import DIR_NAME
class DB:
    def __init__(self,db_env):
        # 调用读取yml文件的方法，读取对应的配置文件
        self.dbinfo = read_yaml('/config/db.yml')[db_env]
        # 连接数据库 配置文件的内容
        self.db=pymysql.connect(
            host=self.dbinfo['host'],
            port=self.dbinfo['port'],
            user=self.dbinfo['user'],
            password=self.dbinfo['pwd'],
            charset='utf8mb4',
            # 返回的数据类型-字典
            cursorclass = pymysql.cursors.DictCursor
            )
  # 查询 返回数据
    def select(self,sql):
        '''

        :param sql: 原生的查询语句
        :return:
        '''
        # 创建游标
        cursor = self.db.cursor()
        cursor.execute(sql)  # 执行sql
        data = cursor.fetchall()  # 获取查询得到的所有数据
        self.db.commit()  # 一次连接多次查询时会有问题
        cursor.close()
        return data

    # 增加 删除 修改
    def update(self,sql):
        '''

        :param sql: 原生的sql(修改，删除，增加语句)
        :return:
        '''
        cursor = self.db.cursor()
        cursor.execute(sql)  # 执行sql
        self.db.commit()  # 但凡有更新语句都是要提交
        cursor.close()
    def close(self):
        '''
        对数据库进行关闭
        :return:
        '''
        if self.db != None:
            self.db.close()

if __name__ == '__main__':
    db = DB('test')
    # mtxshop_trade库.es_order表
    # sql = 'SELECT * FROM hg.device_goods where class_id="15";'
    sql='SELECT * FROM hg.device_goods WHERE class_id =15'
    data = db.select(sql)
    print(data)
    # [
    # {'order_id': 10323, 'trade_sn': '20210711000005',
    # 'seller_id': 20, 'seller_name': '沙陌的店',
    # 'member_id': 72, 'member_name': 'yaoyao',
    # 'order_status': 'CONFIRM',
    # 'pay_status': 'PAY_NO', 'ship_status': 'SHIP_NO', 'shipping_id': 0, 'comment_status': 'UNFINISHED', 'shipping_type': None, 'payment_method_id': None, 'payment_plugin_id': None, 'payment_method_name': None, 'payment_type': 'COD', 'payment_time': None, 'pay_money': None, 'ship_name': 'yaoyao', 'ship_addr': '北京霍营', 'ship_zip': None, 'ship_mobile': '18729399607', 'ship_tel': None, 'receive_time': '仅工作日', 'ship_province_id': 1, 'ship_city_id': 72, 'ship_county_id': 2799, 'ship_town_id': 0, 'ship_province': '北京', 'ship_city': '朝阳区', 'ship_county': '三环以内', 'ship_town': '', 'order_price': Decimal('180.00'), 'goods_price': Decimal('180.00'), 'shipping_price': Decimal('0.00'), 'discount_price': Decimal('0.00'), 'disabled': 0, 'weight': Decimal('1.00'), 'goods_num': None, 'remark': '', 'cancel_reason': None, 'the_sign': None, 'items_json': '[{"seller_id":20,"seller_name":"沙陌的店","goods_id":688,"sku_id":891,"sku_sn":"100101","cat_id":83,"num":1,"goods_weight":1.0,"original_price":180.0,"purchase_price":180.0,"subtotal":180.0,"name":"这是炒锅","goods_image":"http://www.mtxshop.com:7000/statics/attachment/goods/2021/3/27/20/37137422.jpeg_300x300.jpeg","spec_list":null,"point":null,"snapshot_id":10730,"service_status":"NOT_APPLY","complain_status":"NO_APPLY","complain_id":null,"single_list":[],"group_list":[],"goods_operate_allowable_vo":null,"promotion_tags":[],"purchase_num":0,"actual_pay_total":180.0}]', 'warehouse_id': None, 'need_pay_money': Decimal('180.00'), 'ship_no': None, 'address_id': 404, 'admin_remark': None, 'logi_id': None, 'logi_name': None, 'complete_time': None, 'create_time': 1625982097, 'signing_time': None, 'ship_time': None, 'pay_order_no': None, 'service_status': 'NOT_APPLY', 'bill_status': None, 'bill_sn': None, 'client_type': 'PC', 'sn': '20210711000005',
    # 'need_receipt': 0, 'order_type': 'NORMAL', 'order_data': None
    # }
    # ]