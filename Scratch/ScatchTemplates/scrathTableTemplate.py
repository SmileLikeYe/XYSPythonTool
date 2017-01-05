#!/usr/bin/env python
# coding:utf-8
# @Date    : 2017-01-01 20:38:38
# @Author  : Smile Hu (smile.hu@sap.com)
# @Link    : http://www.smilehu.com

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from bs4 import BeautifulSoup
import requests
import xlwt as ExcelWrite
import string
from time import  sleep

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/44.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive'}


start_row = 0

def getExcelFromWebTable(outputSheet, *keyword):
    url = ''.join(keyword)
    print url
    html = requests.get(url, headers=headers).text
    beautyHtml = BeautifulSoup(html, 'lxml')

    tables = beautyHtml.find_all('table')
    if tables:
        print "一共找到 " + str(len(tables)) + " 表格"
        print "默认选取第一个表格......."
        first_table = tables[0]
        trs = first_table.find_all('tr')

        if trs:
            row_count = len(trs)
            # print "行数：" + str(row_count)
            for i in xrange(0, row_count):
                global  start_row
                tr = trs[i]
                tds = tr.find_all('td')
                if tds==None:
                    tds = tr.find_all('th')
                col_count = len(tds)
                # print "列数" + str(col_count)
                for j in xrange(0, col_count):
                    td = tds[j]
                    text = td.text
                    outputSheet.write(start_row, j + 1, label=text)
                start_row = start_row + 1
        else:
            print "表格tr中没有数据"
    else :
        print url + " 中没有表格格式数据"

if __name__ == '__main__':
    '''
    ------------------------------------------------------------------------------------------------
    从text文件中中每一行读取关键字变量进行遍历
    '''
    # inputFilePath = '/Users/i309929/Desktop/cities.txt'
    # queryKeywords = open(inputFilePath, 'r')
    #
    # outputFile = ExcelWrite.Workbook(encoding='utf-8')
    # outputSheet = outputFile.add_sheet("output_sheet", cell_overwrite_ok=True)
    #
    # for keyword in queryKeywords:
    #     global start_row
    #     start_row = start_row + 1
    #     outputSheet.write(start_row, 0, label=keyword)
    #     keyword = string.rstrip(keyword)
    #     print '-------------keyword: ' + str(keyword) + ' ----: '
    #     baseURL = 'http://www.aqistudy.cn/historydata/monthdata.php?city='
    #     getExcelFromWebTable(outputSheet, baseURL, str(keyword))
    #     sleep(1)
    #
    # queryKeywords.close()
    # outputFile.save('/Users/i309929/Desktop/output.xls')

    '''
    ------------------------------------------------------------------------------------------------
    直接进行遍历
    '''
    outputFile = ExcelWrite.Workbook(encoding='utf-8')
    outputSheet = outputFile.add_sheet("output_sheet", cell_overwrite_ok=True)

    getExcelFromWebTable(outputSheet, 'http://tianqihoubao.com/weather/top/beijing.html')

    outputFile.save('/Users/i309929/Desktop/output.xls')
