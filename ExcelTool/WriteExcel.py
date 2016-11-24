# coding=utf-8
import xlwt

wb = xlwt.Workbook()
ws = wb.add_sheet('newSheet', cell_overwrite_ok=True)

# 还可以改字体,布局
style = xlwt.XFStyle()

font = xlwt.Font()
font.name = 'Times New Roman'
font.bold = True
style.font = font

ws.write(0, 0, label="hhh", style=style)
wb.save("/Users/i309929/Desktop/3.xls")