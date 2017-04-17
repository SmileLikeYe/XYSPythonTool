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
url = ""
postdata= {
}

result = requests.get(url,headers=headers).text
result = requests.post(url,data=postdata, headers=headers).text

result = result.replace('\n','')[4:]
result = result.replace('null,', '')
# 这里一定还有剩下的null要处理，因为单独的null是不是python的变量

clean_result = ast.literal_eval(result)

print json.dumps(clean_result).decode("unicode-escape")