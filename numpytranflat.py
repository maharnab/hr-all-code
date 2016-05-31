# -*- coding: utf-8 -*-
"""
Created on Tue Apr 05 20:39:11 2016

@author: rNov

Numpy Transpose & flatten operation program
"""

import numpy as np

row_col = raw_input()
insplt = row_col.split(" ", 1)
rows = int(insplt[0])
cols = int(insplt[1])
abr = np.empty([0, cols], int)

for iters in range(0, rows):
    arr = raw_input()
    asp = arr.split(" ", cols)
    mar = np.array(asp)
    b = mar.astype(np.int)
    mar1 = np.array([b])
    abr = np.append(abr, mar1, axis=0)
    
print np.transpose(abr)
print abr.flatten()
