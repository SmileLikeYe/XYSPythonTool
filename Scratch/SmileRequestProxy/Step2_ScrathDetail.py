# coding:utf-8
# !/usr/bin/env python
# coding:utf-8
# @Date    : 2017-03-01 12:38:38
# @Author  : Smile Hu (smile.hu@sap.com)
# @Link    : http://www.smilehu.com

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import smileRequest
import codecs
import ast
import sqlite3
import json
import traceback

fr = codecs.open('detail_ParamList.txt', 'rb', 'utf-8')
httpLog = codecs.open('procced_paramList.txt', 'wb', 'utf-8')
# sqlLog = codecs.open('sqlLog.txt', 'wb', 'utf-8')

# 读出文件里面的参数列表和结果个数
def getParamList(lines):
    paramList = []
    count = 0
    for line in lines:
        paramList.append(ast.literal_eval(line.strip()))
        count = count +1

    print '从 validParm1.txt 获取参数列表成功，个数：',count
    return paramList

# 构造爬取Post请求的参数
def constructPostData(index,paramDic):
    paramDic['Index'] = index
    print 'postData', json.dumps(paramDic).decode('unicode-escape')
    return paramDic

def cleanResponse(response):
    try:
        response = str(response.replace('\\', ''))[1:-1]
        data = ast.literal_eval(response)[1:]
        print 'cleandata: ', data
        return data
    except :
        print "Error: "
        return []

def processData(data):
    # 定义数据存储结构
    content = {
        '1': "",  # DocumentID = ''
        '2': "",  # CaseNumber = ''
        '3': "",  # JudicialProcess = ''
        '4': "",  # TrialDate = ''
        '5': "",  # TraiContent = ''
        '6': "",  # CaseType = ''
        '7': "",  # CourtName = ''
        '8': "",  # CaseName = ''
        '9': "",  # UnpublicReason = ''
    }

    index = ['文书ID', '案号', '审判程序', '裁判日期', '裁判要旨段原文', '案件类型', '法院名称', '案件名称', '不公开理由']
    # 写入数据到数据库
    for case in data:
        for k, v in case.items():
            if k in index:
                content[str(index.index(k) + 1)] = v
            else:
                print "No Key Field: ", k

        sql = "insert into Tanwu('DocumentID', 'CaseNumber', 'JudicialProcess', 'TrialDate','TraiContent', 'CaseType', 'CourtName', 'CaseName', 'UnpublicReason') values(" + '"' + \
              str(content['1']) + '", "' + \
              str(content['2']) + '", "' + \
              str(content['3']) + '", "' + \
              str(content['4']) + '", "' + \
              str(content['5']) + '", "' + \
              str(content['6']) + '", "' + \
              str(content['7']) + '", "' + \
              str(content['8']) + '", "' + \
              str(content['9']) + '")'
        cursor.execute(sql)
        db.commit()
        # print 'sql:', sql
        # log for track
        # sqlLog.write(sql + '\n')

    print '插入数据库成功！'
    print "这一页结束"
    print "\n"

def mainwork(param):
    # log for track
    print 'postData: ', json.dumps(param).decode('unicode-escape')
    httpLog.write(str(param) + '\n')
    responses = smileRequest.post(url, param)
    data = cleanResponse(responses)
    processData(data)


if __name__ == '__main__':
    # index = ['id', 'DocumentID', 'CaseNumber', 'JudicialProcess', 'TrialDate', 'TraiContent', 'CaseType', 'CourtName', 'CaseName', 'UnpublicReason']

    # 第一步：连
    db_path = '/Users/i309929/Desktop/tanfu.db3'
    db = sqlite3.connect(db_path)
    cursor = db.cursor()

    # 第二步：爬
    url = 'http://wenshu.court.gov.cn/List/ListContent?MmEwMD=1OZ9hajeLBZMtDPo0bZ.HAv6EE_Pc9u26vBhSKJRQAebpgPZirAEjK.yeLzZ5eHuFG5yQbaC0RgCMCKRYSXTfDz9Kz3590phd0mog3gM.IJQm.u1DV7HG2lMAn9O4dzNl0V8qpbsuVAGFfBFdkgXiIcQdZSopvA.WJgYM9v1Zqvdw_e6xF7pYf.nlqeSYPltTEYzubY3kQ2o.tFuNfDut321ab.JroNLlW_dVY_cUT7IIKXwV8nX3eAVLd1RIwOuM3O7.LZuKfv5mf3b39nr6OX1qB1mhNMOi4EXNiRGTM1GJ5ohcIagE0u8JT6jiUKy2HGuRifgRtQc07wxkgKHDrK06aK0jsZEbakq9qhugg_J_HGe6UpdXOkQymt19xJliPP'
    paramList = getParamList(fr.readlines())
    fr.close()
    # 一定要clone 不能copy
    remain_paramList = list(paramList)

    try:
        for param in paramList:
            mainwork(param)
            remain_paramList.remove(param)

        # 第三步：关
        cursor.close()
        db.close()

        httpLog.close()
        # sqlLog.close()
    except Exception, e:

        paramLog = codecs.open('detail_ParamList.txt', 'wb', 'utf-8')
        for i in xrange(len(remain_paramList)):
            paramLog.write(str(remain_paramList[i]) + '\n')
        paramLog.close()
        print 'Update  detail_ParamList.txt Successfully!'

        cursor.close()
        db.close()

        httpLog.close()
        # sqlLog.close()

        # 出现意外也得关闭
        print '出现意外！', e
        traceback.print_exc()







