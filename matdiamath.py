# -*- coding: utf-8 -*-
"""
Created on Sun May 01 21:42:52 2016

@author: rNov

Matrix diagonal operations program
"""

n = int(raw_input().strip())
a = []
for a_i in xrange(n):
   a_temp = map(int,raw_input().strip().split(' '))
   a.append(a_temp)
   
pri_ar = []
sec_ar = []
for pdiael in xrange(n):
    pdiael_temp1 = a[pdiael][pdiael]
    pdiael_temp2 = a[pdiael][-pdiael-1]
    pri_ar.append(pdiael_temp1)
    sec_ar.append(pdiael_temp2)
    
val = sum(pri_ar) - sum(sec_ar)
print abs(val)
