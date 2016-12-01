#!/usr/bin/env python
# coding=utf-8

import sys
reload(sys)
sys.setdefaultencoding = ('utf8')

# Init
dic = {'id':1, 'username':'smile', 'password':'1234'}

# Add
dic['gender'] = 'male'

# Delete
del dic['gender']

# Loop
for k, v in dic.items():
    print k, v

for k in dic.keys():
    print k

for v in dic.values():
    print v

# length
print len(dic)