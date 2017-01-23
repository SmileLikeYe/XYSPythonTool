# coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os
import subprocess
import xlwt
import re

# define
global imgPath
global txtPath
global cleanTxtPath
global xlsPath
global fileName
# assign
imgPath='/Users/i309929/Desktop/3.png'
fileName, ext=os.path.splitext(os.path.basename(imgPath))
txtPath=os.path.dirname(__file__) + '/' + fileName + '.txt'
cleanTxtPath=os.path.dirname(__file__) + '/clean_' + fileName + '.txt'
xlsPath=os.path.dirname(__file__) + '/' + fileName + '.xls'

# step 1:
def img_to_txt(imgPath, plus=''):
    print "Start to convert " + imgPath
    try:
        # plus参数为给tesseract的附加高级参数
        subprocess.check_output('tesseract ' + imgPath + ' ' +
                                fileName + ' ' + plus, shell=True)  # 生成同名txt文件
        print "Convert Successfully! Save txt at: " + txtPath
    except Exception, e:
        print 'Convert Fail: ', e

    def clean_txt():
        print "Start to Clean txt file"
        fr = open(txtPath, 'r')
        fw = open(cleanTxtPath, 'w')

        i = 1
        for line in fr.readlines():
            line = line.strip()
            line = line.replace(',', '.')
            s = line.split()
            # 去除空行
            if len(s) != 0:
                # print s
                temp_s = ''
                for number in s:
                    # 识别是 整数 浮点数 - 的number
                    if re.match(r'^(-?((\d+).(\d+)))|-$', number, re.I):
                        temp_s = temp_s + number + ' '
                    else:
                        print "delete: ", number
                fw.write(temp_s + '\n')
                print len(temp_s.split())
                i = i + 1
        fr.close()
        fw.close()

    def txt_to_xls():
        print "Start to parse " + txtPath
        # 读取文件
        fr = open(cleanTxtPath, 'r')
        wb = xlwt.Workbook()
        ws = wb.add_sheet('newSheet', cell_overwrite_ok=True)

        # handle lines
        i = 0
        for line in fr.readlines():
            s = line.strip().split()
            if len(s) != 0:
                print str(i) + '行： ' + str(len(s))
                for j in xrange(0, len(s)):
                    ws.write(i, j, label=unicode(s[j], 'utf-8'))
                i = i + 1
        wb.save(xlsPath)
        print "Parse Successfully! Save xls ata: " + xlsPath


# img_to_txt(imgPath, '-l eng+deu')
clean_txt()
txt_to_xls()

