# coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from bs4 import BeautifulSoup
import requests
from time import  sleep

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/44.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive'}

def getListData(outputfile, *args):
    url = ''.join(args)
    print url
    html = requests.get(url, headers=headers).text
    beautyHtml = BeautifulSoup(html, 'lxml')

    # 第三步：最重要的定制规则
    # 搜索tag
    tag = beautyHtml.find('div', attrs={'class': 'bottom'})
    tags = beautyHtml.find_all('div')
    tags = beautyHtml.find_all(id='html')
    sub_tags = tag.find_all('div')

    # 获取tag的值
    tag_value = tag.div.string  # type: bs4.element.NavigableString 也是一种unicode, 可以用str() 进行转换
    tag_value = tag.head.text  # type: bs4.element.NavigableString 也是一种unicode, 可以用str() 进行转换

    # 获取property的值
    property_value = tag['class'].string


if __name__ == '__main':
    # 第一步：确定好输出文件
    inputfliePath = '/Users/i309929/Desktop/input.txt'
    outputfile = open(inputfliePath, 'w')

    # 第二步：定制url
    url = 'http://www.aqistudy.cn/historydata/index.php'
    getListData(outputfile, url)

    outputfile.close()
