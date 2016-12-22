# coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from ScratchAPI4XiaoYanShi import ScrathTableAPI
from ScratchAPI4XiaoYanShi import  ScrathListAPI

st = ScrathTableAPI.ScrathTable()
# s.getExcelFromTable('http://tianqihoubao.com/weather/top/beijing.html')
st.getExcelFromTable('http://r.qidian.com/')

sl = ScrathListAPI.ScrathList()
sl.getExcelFromList("http://r.qidian.com/")