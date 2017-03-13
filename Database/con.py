#!/usr/bin/env python
# coding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

'''
Inset clean data into database
'''

import sqlite3
import subprocess
import os

sql = "insert into Tanwu('文书ID', '案号', '审判程序', '裁判日期','裁判要旨段原文', '案件类型', '法院名称', '案件名称') values(" + str(count) + ',' + str(
                    user_id) + ',' + str(shop_id) + ', "' + str(time_stamp) + '")'

db_path = 'doubei.sqlite3';
db = sqlite3.connect(db_path)
cursor = db.cursor()

fr = open('shop_info.txt', 'r')
count = 1
for line in fr.readlines():
	print 'count', count
	user_id = "NA"
	shop_id = "NA"
	time_stamp = "NA"
	content = line.split(',')
	user_id = content[0].strip()
	shop_id = content[1].strip()
	time_stamp = content[2].strip()

	print cursor.execute(sql)
	sql = 'insert into user_view(id, user_id, shop_id, time_stamp) values(' + str(count) +',' +  str(user_id) +',' + str(shop_id) + ', "' + str(time_stamp)+'")'

	db.commit()
	count = count + 1



fr.close()
cursor.close()
db.close()
