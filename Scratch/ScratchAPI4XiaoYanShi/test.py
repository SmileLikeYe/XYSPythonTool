#!/usr/bin/env python
# coding:utf-8
# @Date    : 2017-01-01 20:38:38
# @Author  : Smile Hu (smile.hu@sap.com)
# @Link    : http://www.smilehu.com

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from ScrathTableAPI import  ScrathTable
# for i in xrange(1998, 2010):
#     url = 'http://www.transparency.org/research/cpi/cpi_' + str(i) + '/0/'
#     ScrathTable().getExcelFromTable(url,'/'+str(i)+'.xls')
ScrathTable().getExcelFromTable('http://www.transparency.org/news/feature/corruption_perceptions_index_2016','/2016.xls')