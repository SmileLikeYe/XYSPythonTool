#!/usr/bin/env python
# coding:utf-8
# @Date    : 2017-01-01 20:38:38
# @Author  : Smile Hu (smile.hu@sap.com)
# @Link    : http://www.smilehu.com

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# Init
l = ['hah',13]

# Add
l.append(1)
l.append('2')

# Delete
del l[1]

# Loop
for ele in l:
    print ele

# Len
print len(l)

# solve chinese messy code
import json
print json.dumps(["中国", "美国"]).decode("unicode-escape")