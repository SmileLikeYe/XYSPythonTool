# encoding=utf-8
import os
# pelease install:
# sudo install xlrd
# sudo install xlutils
import xlrd
import xlwt
from xlutils.copy import copy

class XYSExcelTool():
    def OpenExcelByPath(self, filePath):
        if os.path.exists(filePath):
            rb = xlrd.open_workbook(filePath)
            return rb
        else:
            raise "Your Excle File Path is not valid, please check again."

    def EditExcelByPath(self, filePath):
        if os.path.exists(filePath):
            rb = xlrd.open_workbook(filePath)
            wb = copy(rb)
            return wb
        else:
            raise "Your Excle File Path is not valid, please check again."

    def CreateExcel(self):
        wb = xlwt.Workbook()
        return wb

    def SaveExcel(self, wb, filePath):
        wb.save(filePath)