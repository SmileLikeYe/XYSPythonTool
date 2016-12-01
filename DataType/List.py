#!/usr/bin/env python
# coding=utf-8

import sys
reload(sys)
sys.setdefaultencoding = ('utf8')

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