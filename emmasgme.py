# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 21:38:00 2016

@author: rNov

Emma's game challenge from HackerRank
"""

import sys

n = int(raw_input().strip())
c = map(int,raw_input().strip().split(' '))
c_ind = [0]
for i, val in enumerate(c):
    if val == 1:
        c_ind.append(i)
summ = 0
c_ind.insert(len(c_ind), n)
for i, item in enumerate(c_ind[:-1]):
    k = c[item:c_ind[i+1]]
    if k.count(1) == 0:
        summ = summ + (len(k) // 2)
    else:
        summ = summ + (-(-(len(k)) // 2))
    
print summ
