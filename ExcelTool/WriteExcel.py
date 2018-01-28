#!/usr/bin/env python
# coding:utf-8
# @Date    : 2017-01-01 20:38:38
# @Author  : Smile Hu (smile.hu@sap.com)
# @Link    : http://www.smilehu.com

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import xlwt

wb = xlwt.Workbook(encoding="utf-8")
ws = wb.add_sheet('newSheet', cell_overwrite_ok=True)

#一行一行的写入
for i in xrange(0, 100):
    ws.write(i, 0 , label="ganbadie")
    ws.write(i, 1 , label="ganbadie")

wb.save("/Users/i309929/Desktop/3.csv")


# 还可以改字体,布局
style = xlwt.XFStyle()

font = xlwt.Font()
font.name = 'Times New Roman'
font.bold = True
style.font = font

ws.write(0, 0, label="hhh", style=style)