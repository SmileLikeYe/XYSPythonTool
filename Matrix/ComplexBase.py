#!/usr/bin/env python
# coding:utf-8
# @Date    : 2017-01-01 20:38:38
# @Author  : Smile Hu (smile.hu@sap.com)
# @Link    : http://www.smilehu.com

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from numpy import *
import numpy as np
import scipy as sp

# 矩阵 定义
s0=np.matrix([[2,5],[-3,-7]],dtype=float)
s1=np.array([[1,2,3], [4,5,6], [4,5,6]],dtype=float)
s2=np.array([[1,2,3], [1,2,3], [1,2,3]],dtype=float)
s3=np.array([[2,5],[-3,-7]], dtype=float)
s4=np.matrix([[2,5],[-3,-7]],dtype=float)
s5=np.mat([[2,5],[-3,-7]],dtype=float)
print s5[0:1,0:1]

# 创建常见矩阵
#创建一个3*3的零矩阵，矩阵这里zeros函数的参数是一个tuple类型(3,3)
print np.mat(zeros((3,3)))
#创建一个2*4的1矩阵，默认是浮点型的数据，如果需要时int类型，可以使用dtype=int
print np.mat(ones((2,4)))
#这里的random模块使用的是numpy中的random模块，random.rand(2,2)创建的是一个二维数组，需要将其转换成#matrix
print np.mat(random.rand(2,2))
#生成一个3*3的-1-10之间的随机整数矩阵
print np.mat(random.randint(-1, 10, size=(3,3)))
#产生一个2*2的单位对角矩阵
print np.mat(eye(5,5, dtype=int))
#生成一个对角线为1、2、3的对角矩阵
temp_m = [1,2,3]
print np.mat(diag(temp_m))


# 矩阵 加
print s1+s2
print s3+s4

# 矩阵 减
print s1-s2

# 矩阵 乘
print np.dot(s1,s2)
print np.dot(s3,s4)
# 点积（对应点相乘）
print s1*s2
print s3*s4

# 矩阵 转置
print s1.T
print s1.transpose()

# 矩阵 求逆
print s4.I
print s4**(-1)
print np.linalg.inv(s3)

# 矩阵 行列式
print np.linalg.det(s4)

# 矩阵 伴随
print np.dot(np.linalg.det(s4),np.linalg.inv(s4))

# 矩阵 范数
print np.linalg.norm(s4)





