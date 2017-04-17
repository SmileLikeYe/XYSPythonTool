# coding:utf-8
import requests
import ast
import json

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/44.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive'}

#
url = ""
postdata= {
}

# 请求
result = requests.get(url,headers=headers).text
result = requests.post(url,data=postdata, headers=headers).text

# 对返回的string进行按照 自己的 需求进行清洗
result = result.replace('\n','')[4:]
result = result.replace('null,', '')

# 将list  dic 类型的string转成 list dic
clean_result = ast.literal_eval(result)

print json.dumps(clean_result).decode("unicode-escape")