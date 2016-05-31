# -*- coding: utf-8 -*-
"""
Created on Fri May 06 23:36:40 2016

@author: Maharnab
"""

import sys


n = int(raw_input().strip())

for i in range(1, n+1):
    print ' ' * int(n-i) + '#' * int(i)