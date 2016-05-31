# -*- coding: utf-8 -*-
"""
Created on Fri May 06 23:04:07 2016

@author: Maharnab
"""

import sys

n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

pcount = 0
ncount = 0
zcount = 0

for item in arr:
    if (item > 0):
        pcount = pcount + 1
    if (item == 0):
        zcount = zcount + 1
    if (item < 0):
        ncount = ncount + 1
        
print round(pcount/float(n), 6)
print round(ncount/float(n), 6)
print round(zcount/float(n), 6)
