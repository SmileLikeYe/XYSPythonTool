# coding=utf-8
import xlrd

excelFilePath = '/Users/i309929/Desktop/1.xls'

rb = xlrd.open_workbook(excelFilePath)
rs = rb.sheet_by_index(0)

print rs.nrows
print rs.ncols

# -------------常用取值-------------
# 得到某一行的值 -> 得到List
rowList = rs.row_values(1)
# 得到某一列的值 -> 得到List
colList = rs.col_values(1)
# 得到某个cell的值 -> 得到 float（不需要处理）
#                         或者 unicode (string 和 空值 会被当做unicode,要处理encode('utf-8')的处理)
cellValue = rs.cell(0, 0).value
# 如果是string, string会被当做unicode,不可用于string的比较，必须要做如下转换，变成string
cellValue = cellValue.encode('utf-8')

# -------------常用循环-------------
# 循环第 i 行的值
i = 1
for j in xrange(0,rs.ncols):
    print rs.cell(i, j).value

# 循环第 j 列的值
j = 1
for i in xrange(0,rs.nrows):
    print rs.cell(i, j).value

# 循环整个表格
for i in xrange(0, rs.nrows):
    for j in xrange(0, rs.ncols):
        print rs.cell(i, j).value