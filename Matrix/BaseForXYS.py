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

'''----------矩阵 创建----------'''
# 矩阵 创建 基本矩阵
s1=np.mat([[2,5],[-3,-7]],dtype=float)
s2=np.mat('2 5; -3 -7')
# 矩阵 创建 常见实用矩阵
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

'''----------矩阵 取值----------'''
# 矩阵 取值 某个元素
print s1[0,0]
# 矩阵 取值 第一行
print s1[0]
# 矩阵 取值 第一列
print s1[:,0]
# 矩阵 取值 第一行+第一列
print s1[0:1,0:1]

'''----------矩阵 运算----------'''
# 矩阵 运算 加
print s1+s2
# 矩阵 运算 减
print s1-s2
# 矩阵 运算 乘
print np.dot(s1,s2)
# 矩阵 运算 点积（对应点相乘）
print s1*s2
# 矩阵 运算 转置
print s1.T
# 矩阵 运算 求逆
print s1.I
# 矩阵 运算 行列式
print np.linalg.det(s1)
# 矩阵 运算 伴随
print np.dot(np.linalg.det(s1),np.linalg.inv(s1))
# 矩阵 运算 范数
print np.linalg.norm(s1)





