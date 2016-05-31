# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 02:23:53 2016

@author: Maharnab
"""

n, d = map(int,raw_input().strip().split(' '))
a = map(int,raw_input().strip().split(' '))

ad = map(lambda x:x+d, a)
adr = set(ad) & set(a)
adr = sorted(list(adr))
add = map(lambda x:x+d, adr)
a2dr = set(add) & set(a)
a2dr = sorted(list(a2dr))
print len(a2dr)


