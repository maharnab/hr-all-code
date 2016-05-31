# -*- coding: utf-8 -*-
"""
Created on Mon Apr 04 13:38:55 2016

@author: Maharnab

Dictionary Program
"""

N = int(raw_input('N:\t'))
dct = dict()
if N >= 2 and N <= 100:
    for i in range(0, N):
        name_marks = raw_input('Name & Marks:\t')
        in_splt = name_marks.split(" ", 1)
        dct[in_splt[0]] = in_splt[1]        
else:
    print 'error'

in_name = raw_input('Name:\t')
s = dct.get(in_name)
p, c, m = (float(marks) for marks in s.split())
avg_m = (p + c + m)/3.00
print '%0.2f' % avg_m