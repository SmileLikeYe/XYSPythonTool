# coding:utf-8
from bs4 import BeautifulSoup
import requests
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/44.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive'}

def getMobileInfo(base_url, page):
    result = []

    for i in range(0,page,1):
        url = ''.join([base_url, str(i), '.html'])
        html = requests.get(url, headers=headers).text
        beautyHtml = BeautifulSoup(html, 'lxml')

        div_list = beautyHtml.find_all('div', attrs={
            'class': 'feeds-item'})

        if div_list:
            for item in div_list:
                href = item.div.h3.a['href']
                name = item.div.h3.a.text.encode('utf-8')
                reg = '201\d年\d+月'
                regResul = re.findall(reg, name, re.S)
                if len(regResul) != 0:
                    print '___Name:', name
                    print '___ADD', href
                    result.append(href)
    return result


if __name__ == '__main__':
    base_url = 'http://www.pc841.com/tags/newmobile-'
    page = 12
    getMobileInfo(base_url, page)