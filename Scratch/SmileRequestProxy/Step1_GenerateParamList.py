# coding:utf-8
# !/usr/bin/env python
# coding:utf-8
# @Date    : 2017-03-01 12:38:38
# @Author  : Smile Hu (smile.hu@sap.com)
# @Link    : http://www.smilehu.com

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import codecs
import math
import ast
import json
import smileRequest
import traceback

def getKeyTree(paramList):
    url = 'http://wenshu.court.gov.cn/List/TreeContent?MmEwMD=131I2hlDDV1G9eWZFw1Af.xWbuVR7Iw8RQraIzOPn.swdkWoG_5ulzmcsskoADfE0MAcnw8JFPKJTJgP4tqiHekIIviPYaEMYK0CYCgRn.iCjRtM0pMWTqut3JKkzyqRDHCSQa_AYIVTaA5ci78hJh8DU6rdD7twbznOYqmGsm1hEeKcQh36JL_sLz1MGC8N9uh2C5GNjKcg6AfyMHoony8P5VTrQLf5JyHbs6ZwwxKHt_Fos.vViurWuFBfdJPZbFo66Aw4OOdoXUCx4P8tsAnEL2GMBfR4ywE87EelCkcN1xjzX3QgS84SDLq6rMAQ6xB.gfjcO5uz.KFsemwg7a_PgcCLjpspxYXVAwk3kk4Fh'
    data = constructPostData(paramList)

    html = smileRequest.post(url,data=data)
    result = html.replace('\\', '')[1:-1]
    result = ast.literal_eval(result)
    print json.dumps(result).decode('unicode-escape')

    keyTree = {}
    for por in result:
        Field = por['Key']
        keyTree[Field] = []
        for child in por['Child']:
            if child["Key"] != "":
                keyTree[Field].append(child["Key"])

    # del keyTree["法院层级"]
    # del keyTree["审判程序"]
    print json.dumps(keyTree).decode('unicode-escape')

    return keyTree

def constructPostData(paramDic):
    Param = ''
    for k, v in paramDic.items():
        Param = Param + str(k) + ":" +str(v) +','

    postdata = {
        'Param': Param[:-1],
        'Index': 1,
        'Page': '5',
        'Order': '法院层级',
        'Direction': 'asc',
    }

    print ''
    print ''
    print 'paramdata: ', json.dumps(postdata).decode('unicode-escape')
    return postdata

def getCount(response):
    response = str(response.replace('\\', ''))[1:-1]
    totolNum = ast.literal_eval(response)[0]['Count']
    print "totolNum: ",totolNum

    return int(totolNum)

def handleExceptionParams(parDic):
    key = parDic.keys()[0]
    # 最高人民法院的例外
    if key == '法院地域' and  parDic[key]== '最高人民法院':
        # parDic = {'法院层级': '最高法院'}
        # 这个会出现 年份里面 但是这个和之前的法院层级的key像冲突，是冗余的，会执行两次，故舍弃
        return {}
    return parDic

def generate_genericPL(firstParList):
    try:
        print ''
        fw = codecs.open('generic_ParamList.txt', 'wb', 'utf-8')
        url = 'http://wenshu.court.gov.cn/List/ListContent?MmEwMD=1DcN35G46.LvqUNeekbyWo764zaFs9tdpVyRS2iO0IfIRVrUBEbvDckfBYt_EBxNu6Kxe3wZs0u02lUUObbU6169n2uk0FVjxyoqr5yx6mA61E0EzQi9isZYmCzbndnmyJwWBhEhOjDJ4xbsf.jo_S.bc1uf7yP3858taauT55WZesC0YOKA91g8k7mllZxTA35Np8yB0oRgXqUwunuZNLZl5vR9f4juAvkxBQyfVPQpo3UEv70JKyzl8dsiFwYOicq5x0B4Lh0TYPO9r6tmZt.AlJMjGiL_.OZwpWPgmRB2ouOh8IHT_ueZQrJpeLvk9AYzRDFK5v6Gyi5g2YNqdKEeNciLHAScvA9iadLLEgPyh'

        # 获得对应管检测的keyTree
        keyTree = getKeyTree(firstParList[0])
        for key in keyTree.keys(): print key
        del keyTree['审判程序']
        keys = keyTree.keys()
        # firstParList 是存储之前>2000的搜索条件字典


        i = 0
        while len(firstParList) > 0:
            # secondParTuple 是下一个可用条件的条件字典
            secondParList = []
            for v in keyTree[keys[i]]: secondParList.append({keys[i]: v})

            rpl = []
            for p1 in firstParList:
                paramDic = p1
                for p2 in secondParList:
                    p2= handleExceptionParams(p2)
                    if p2: paramDic.update(p2)
                    else: continue

                    postdata = constructPostData(paramDic)
                    response = smileRequest.post(url, postdata)
                    count = getCount(response)

                    if count > 2000:
                        print json.dumps(paramDic).decode('unicode-escape'), "——————大于2000,添加进去"
                        rpl.append(paramDic.copy())
                    elif count > 0:
                        print json.dumps(paramDic).decode('unicode-escape'), "——————ok"
                        fw.write(str(count) + '\n')
                        fw.write(str(postdata) + '\n')
                    else:
                        print json.dumps(paramDic).decode('unicode-escape'), 'count = 0'

            print 'remian paramter list: ', json.dumps(rpl).decode('unicode-escape')
            firstParList = rpl
            i = i + 1
            # 处理当循环完所有keyTree的条件 还是有>2000的就记录下来
            if i >= len(keys):
                if len(firstParList) > 0:
                    final_remain_param = codecs.open('final_remain_param.txt', 'wb', 'utf-8')
                    for param in firstParList:
                        final_remain_param.write(str(firstParList))
                    final_remain_param.close()
                break

        fw.close()
        print 'generic_ParamList.txt generated successfully!'
        return True
    except Exception as e:
        print 'generate_genericPL 出现意外：',e
        traceback.print_exc()
        return False

# 读出文件里面的参数列表和结果个数
def getParamList(lines):
    paramList = []
    countList = []
    for line in lines:
        line = line.strip()
        if line[0] == "{":
            paramList.append(ast.literal_eval(line.strip()))
        else:
            countList.append(int(line))

    print '从 generic_ParamList.txt 获取参数列表成功'
    return countList,paramList

def generate_detailPL():
    totalCount = 0
    paramListFile = codecs.open('detail_ParamList.txt', 'wb', 'utf-8')
    with codecs.open('generic_ParamList.txt', 'rb', 'utf-8') as fr:
        countList, paramList = getParamList(fr.readlines())
        fr.close()

        for i in xrange(len(countList)):
            count = countList[i]
            paramDic = paramList[i]

            max_index = int(math.ceil(float(count) / 20))
            for index in xrange(max_index):
                paramDic['Index'] = index + 1
                print 'postData: ', json.dumps(paramDic).decode('unicode-escape')
                paramListFile.write(str(paramDic) + '\n')
                totalCount = totalCount + 1

        print '一共参数个数：', totalCount
        paramListFile.close()

if __name__ == '__main__':
    #所有的参数列表
    # {"法院层级": ["最高法院", "高级法院", "中级法院", "基层法院"],
    #  "审判程序": ["一审", "二审", "再审", "复核", "刑罚变更", "非诉执行审查", "再审审查与审判监督", "其他"],
    #  "法院地域": ["最高人民法院", "北京市", "天津市", "河北省", "山西省", "内蒙古自治区", "辽宁省", "吉林省", "黑龙江省", "上海市", "江苏省", "浙江省", "安徽省", "福建省",
    #           "江西省", "山东省", "河南省", "湖北省", "湖南省", "广东省", "广西壮族自治区", "海南省", "重庆市", "四川省", "贵州省", "云南省", "西藏自治区", "陕西省",
    #           "甘肃省", "青海省", "宁夏回族自治区", "新疆维吾尔自治区", "新疆维吾尔自治区高级人民法院生产建设兵团分院"],
    #  "裁判年份": ["2016", "2014", "2015", "2013", "2012", "2017", "2011", "2010", "2009", "2008", "2007", "2003", "2005",
    #           "2004", "2006"],
    #  "文书类型": ["判决书", "裁定书", "调解书", "决定书", "通知书", "其他"],
    #  "一级案由": ["刑事案由", "民事案由", "行政案由", "赔偿案由"],
    #  "关键词"  : ["合同", "利息", "返还", "利率", "非法占有", "鉴定", "赔偿责任", "人身损害赔偿", "交通事故", "程序合法", "误工费", "合同约定", "驳回", "担保", "强制性规定",
    #          "第三人", "交付", "租赁", "给付", "从犯", "清偿", "变更", "民间借贷", "债权", "保证", "借款合同", "违约金", "所有权", "自首", "债务人", "贷款",
    #          "本案争议", "租金", "债权人", "共同犯罪", "减轻处罚", "抵押", "精神损害", "交通事故损害赔偿", "买卖合同", "民事责任", "解除合同", "残疾赔偿金", "票据", "承诺",
    #          "房屋买卖", "违约责任", "夫妻关系", "投资", "合同无效", "合伙", "处分", "赔偿金", "损害赔偿", "追偿", "保险合同", "垫付", "分公司", "传票", "赔偿损失",
    #          "建设工程", "传唤", "房屋租赁", "缺席判决", "婚姻", "股权转让", "连带责任", "不动产", "合同解除", "反诉", "授权", "股权", "法定代表人", "实际履行",
    #          "债权转让", "侵权行为", "挂靠", "代理", "土地使用权", "胁迫", "罚金", "承租人", "股份有限公司", "过失", "保险人", "保人", "故意犯", "房屋所有权",
    #          "补充协议", "主要责任", "被保险人", "查封", "抵押权", "扣押", "财产权", "标的物", "赔偿数额"]}
    #
    # 例子：
    # paramList = [
    # {
    # '全文检索: '贪污',
    # '审判程序':
    # '法院层级': '基层法院',
    # '法院地域': '浙江省'，
    # '裁判年份': '2016',
    # '文书类型': '判决书'
    # '一级案由'：'刑事案由',
    # '关键词'  : "合同",
    # }]



    # 这里用全文关键字搜索演示
    paramList = [{'全文检索': '贪污'}]
    # 根据keyTree遍历得到对应的小于2000返回结果条件的记录文件
    if generate_genericPL(firstParList=paramList):
        generate_detailPL()