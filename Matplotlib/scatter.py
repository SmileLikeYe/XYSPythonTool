#!/usr/bin/env python
# coding:utf-8
# @Date    : 2017-01-01 20:38:38
# @Author  : Smile Hu (smile.hu@sap.com)
# @Link    : http://www.smilehu.com

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#导入必要的模块
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
#产生测试数据
x = np.arange(1,10)
y = x
fig = plt.figure()
ax1 = fig.add_subplot(111)
#设置标题
ax1.set_title('Scatter Plot')
#设置X轴标签
plt.xlabel('X')
#设置Y轴标签
plt.ylabel('Y')
#画散点图
ax1.scatter(x,y,c = 'b',marker = 'o')
#设置图标
plt.legend('x1')
#设置每个点的文字
for i in xrange(0 , len(x)):
    plt.text(x[i], y[i], str(y[i]) + "     ", family='serif', style='italic', ha='right', size=10)
#显示所画的图
plt.show()
#保存图片
picPath = os.path.join(os.path.dirname(__file__), "result.png")
print picPath
plt.savefig(picPath)