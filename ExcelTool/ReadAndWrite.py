#!/usr/bin/env python
# coding=utf-8

import sys
reload(sys)
sys.setdefaultencoding = ('utf8')

import xlrd
import xlwt

excelFilePath = '/Users/i309929/Desktop/sougou.xls'

rb = xlrd.open_workbook(excelFilePath)
rs = rb.sheet_by_index(0)

wb = xlwt.Workbook()
ws = wb.add_sheet('newSheet', cell_overwrite_ok=True)

# -------------常用读循环-------------
# 循环第 i 行 j列的值
for i in xrange(0,rs.nrows):
    for j in xrange(0, rs.ncols):
        print rs.cell(i, j).value

ws.write(0, 0, label='id')
ws.write(0, 1, label='doc_id_last_appear')
ws.write(0, 2, label='Edu')
ws.write(0, 3, label='Age')
ws.write(0, 4, label='gender')

wb.save("/Users/i309929/Desktop/1_sougou.xls")

