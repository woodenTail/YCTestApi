
# !/usr/bin python3
# encoding: utf-8 -*-
# @author:   wsj QQ：3512937625
# @Time:   2021-07-04
# @Copyright：
'''读取yaml和读取excel'''

import json
import yaml
import pandas
from apiframework.setting import DIR_NAME
def read_yaml(filename):
	'''
	读取yaml文件
	pip install pyyaml
	:return:
	路径:绝对路径
	相对路径:相对的是哪个文件？？
	相对的是你运行的那个文件
	'../data/mtxshop.yml' 相对file_load.py
	'./data/mtxshop.yml' 相对run.py
	动态生成绝对路径
	解决方案:
	动态生成绝对路径
	1.获取当前项目的绝对路径
	2.跟读取的数据进行拼接
	'''
	with open(DIR_NAME+filename,'r',encoding='utf-8') as f:
		# 读取yml文件
		content =yaml.load(f,Loader=yaml.FullLoader)
		return content


def read_excel(filename,sheet_name):
	'''
	pip install pandas
	pip install openpyxl
	pip install xlrd
	:param filename: 你要读取的文件的名字
	:return:
	'''
	pd=pandas.read_excel(DIR_NAME+filename,sheet_name=sheet_name,
					  # 如果碰到空的单元格，默认是返回nan,python没有办法解析
					  # 所以让keep_default_na=False就会返回空字符串，
					  keep_default_na=False,
					  engine='openpyxl')
	# 总行数
	lines_count = pd.shape[0]  # 获取总的行数(不包含头部)
	# 总列数
	col_count = pd.columns.size # 获取总列数
	# 获取单元格的方法的索引值是从0开始的
	data=[]
	# 父循环控制行数
	for row in range(lines_count):  # 遍历行
		line = []  # 存放同一行中不同列的数据
		# 子循环控制列数
		for col in range(col_count): # 遍历列
			text=pd.iloc[row,col]  # 行和列组合交叉定位到一个单元格，可以拿到其内容
			# 判断  如果列数==1的时候  请求参数  text正常读取是字符串 text转换成字典
			if col == 1:
				text=json.loads(text)  # 将json格式的字符串转换成字典
			line.append(text)
		data.append(line)
	return data
if __name__=='__main__':
        # print(read_yaml('/config/db.yml')['test'])
        # print(read_yaml('/data/ecshop.yml')['getshopproduct'])
        data = read_excel('/data/buyer.xlsx','立即购买')
        print(data)
