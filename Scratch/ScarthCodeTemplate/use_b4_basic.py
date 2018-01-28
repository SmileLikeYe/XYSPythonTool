# coding:utf-8
from bs4 import BeautifulSoup
import requests


headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/44.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive'
}

url = ""
html = requests.get(url, headers=headers).text
print html

beautyHtml = BeautifulSoup(html, 'lxml')
div_list = beautyHtml.find_all('div', attrs={'class': 'feeds-item'})
for div in div_list:
    print div.text


#扩展： 字标签， 内部属性的获取， 字符的编码，正则搜索

# import re
# if div_list:
#     for item in div_list:
#         # 取得tag属性的值
#         href = item.div.h3.a['href']
#         # 取得tag的值
#         name = item.div.h3.a.text.encode('utf-8')
#         reg = '201\d年\d+月'
#         regResul = re.findall(reg, name, re.S)
#         if len(regResul) != 0:
#             print '___Name:', name
#             print '___ADD', href
#             result.append(href)
