#!/usr/bin/env python
# coding:utf-8
# @Date    : 2017-01-01 20:38:38
# @Author  : Smile Hu (smile.hu@sap.com)
# @Link    : http://www.smilehu.com

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import sqlite3

# Open
sqlite_file = 'WorkerData.db'
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

table = "worker_incident"

# 增

# 删

# 改

# 查
sql = "select * from %s" % table
c.execute(sql).fetchall()
print sql


# close
conn.close()