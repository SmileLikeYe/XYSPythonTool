#!/usr/bin/env python
# coding:utf-8
# @Date    : 2018-01-26 00:49:08
# @Author  : Smile Hu (www.smilehu.com)
# @Link    : http://www.smilehu.com

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import pandas



def writeToCSVSmile(dataList):
	adjustedList = []
	
	for data in dataList:
		if data:
			sourrondingLoupanList = data['sourrondingLoupan']			
			i = 1 
			for sl in sourrondingLoupanList:
				for k,v in sl.items():
					data["ssl" + str(i) + "_" + k] = v
				i = i +1
		adjustedList.append(data)
	pprint(adjustedList)
	return adjustedList
		
	
from pprint import pprint
yourlist = [
  {
	"k1": "v1", 
	"k2": "v2", 
	"sourrondingLoupan": [
		{"k11": "v11", "k12":"v12"},
		{"k11": "v11", "k12":"v12"}
	]
  },
  {
	"k1": "v1haha", 
	"k2": "v2", 
	"sourrondingLoupan": [
		{"k11": "v11", "k12":"v12"},
		{"k11": "v11", "k12":"v12"},
		{"k11": "v11", "k12":"v12"}
	]
  }
]
pd = pandas.DataFrame(writeToCSVSmile(yourlist))
pd.to_csv("mylist.csv")
print pandas.read_csv("mylist.csv",usecols=['k1', 'k2', 'sourrondingLoupan'])



