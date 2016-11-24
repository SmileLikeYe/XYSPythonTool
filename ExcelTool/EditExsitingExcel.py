# coding=utf-8
import xlrd
from xlutils.copy import copy

excelFilePath = '/Users/i309929/Desktop/1.xls'

rb = xlrd.open_workbook(excelFilePath)
wb = copy(rb)
ws = wb.get_sheet(0)

ws.write(0, 0, 'test')
wb.save('/Users/i309929/Desktop/2.xls')

# Easy for remembering the menaing of varians:
# rb : readWorkBook
# wb : writeWorkBook    (This is to be saved by flie path)
# ws : writeSheet   ( this is to be written bu value)

# This the demo code of how to Edit Exsiting Excel file.
# Xiao Yanshi can follow this code demo to write.
