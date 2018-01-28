# !/usr/bin/env python
# coding:utf-8
# @Date    : 2017-03-01 12:38:38
# @Author  : Smile Hu (smile.hu@sap.com)
# @Link    : http://www.smilehu.com

# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

import smileRequest

url = "http://www.jianshu.com/p/f654f9895555"

a = smileRequest.get(url)
print(a.text)