#-*-coding:utf8-*-

import re
import string
import sys
import os
import urllib
import urllib2
from bs4 import BeautifulSoup
import requests
from lxml import etree

reload(sys)
sys.setdefaultencoding('utf-8')
if(len(sys.argv)>=2):
    user_id = (int)(sys.argv[1])
else:
    user_id = 2763499375
    # user_id = (int)(raw_input(u"请输入user_id: "))

cookie = {"Cookie": "_T_WM=5dff09aaa244d0dfc3f18995a7826868; SCF=ArjaKzih3kJpBrmWutKqyyF0PMnrfggPnbEcFs8BG1H63YuZ7HrNG2MB7_u-GQkguJJn86awoXdcz81wkWN0aIs.; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5CVihL4c0H8irDPwVze05j5JpX5o2p5NHD95Q0ehn4So.Reh5pWs4Dqc_oi--fi-z7iKysi--ciK.RiKLsi--ciK.RiKLsi--Ri-2ciKnpi--fiKyWi-8Wi--fiKyWiKLFi--fiKysiK.pi--fiKnfiKn4i--ciKLWiK.ci--NiKLsi-z0i--fi-2Xi-zX; H5_INDEX=3; H5_INDEX_TITLE=%E5%B0%8F%E6%98%9F%E6%98%9F%E8%A6%81%E5%8A%AA%E5%8A%9B%E5%8F%91%E5%85%89%E6%9A%96%E7%9F%B3%E5%A4%B4; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D102803_ctg1_8999_-_ctg1_8999_home%26fid%3D102803_ctg1_8999_-_ctg1_8999_home%26uicode%3D10000011; SUB=_2A251d17xDeRxGeVO41sX-SbMyz2IHXVWmGK5rDV6PUJbkdAKLWbVkW177QLf_1GqBDhwNvPwVf334JfNfw..; SUHB=0jBI1p45OEFTmu; SSOLoginState=1483943585"}
url = 'http://weibo.cn/u/%d?filter=1&page=1'%user_id

html = requests.get(url, cookies = cookie).content
selector = etree.HTML(html)
pageNum = (int)(selector.xpath('//input[@name="mp"]')[0].attrib['value'])

result = ""
urllist_set = set()
word_count = 1
image_count = 1

print u'爬虫准备就绪...'

for page in range(1,pageNum+1):

  print "page:" + str(page)

  #获取lxml页面
  url = 'http://weibo.cn/u/%d?filter=1&page=%d'%(user_id,page)
  lxml = requests.get(url, cookies = cookie).content

  #文字爬取
  selector = etree.HTML(lxml)
  content = selector.xpath('//span[@class="ctt"]')
  for each in content:
    text = each.xpath('string(.)')
    if word_count>=4:
      text = "%d :"%(word_count-3) +text+"\n\n"
    else :
      text = text+"\n\n"
    result = result + text
    word_count += 1

  #图片爬取
  soup = BeautifulSoup(lxml, "lxml")
  urllist = soup.find_all('a',href=re.compile(r'^http://weibo.cn/mblog/oripic',re.I))
  first = 0
  for imgurl in urllist:
    urllist_set.add(requests.get(imgurl['href'], cookies = cookie).url)
    image_count +=1

desktopPath = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')

fo = open(desktopPath + "/%s"%user_id, "wb")
fo.write(result)
word_path=os.getcwd()+'/%d'%user_id
print u'文字微博爬取完毕'

link = ""
fo2 = open(desktopPath +"/%s_imageurls"%user_id, "wb")
for eachlink in urllist_set:
  link = link + eachlink +"\n"
fo2.write(link)
print u'图片链接爬取完毕'

if not urllist_set:
  print u'该页面中不存在图片'
else:
  #下载图片,保存在当前目录的pythonimg文件夹下
  image_path=os.getcwd()+'/weibo_image'
  if os.path.exists(image_path) is False:
    os.mkdir(image_path)
  x=1
  for imgurl in urllist_set:
    temp= image_path + '/%s.jpg' % x
    print u'正在下载第%s张图片' % x
    try:
      urllib.urlretrieve(urllib2.urlopen(imgurl).geturl(),temp)
    except:
      print u"该图片下载失败:%s"%imgurl
    x+=1

print u'原创微博爬取完毕，共%d条，保存路径%s'%(word_count-4,word_path)
print u'微博图片爬取完毕，共%d张，保存路径%s'%(image_count-1,image_path)