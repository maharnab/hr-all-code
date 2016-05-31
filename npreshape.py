# -*- coding: utf-8 -*-
"""
Created on Tue Apr 05 00:23:49 2016

@author: Maharnab
"""

import numpy as np

inp_nums = raw_input()
insplt = inp_nums.split(" ")
a = np.array(insplt)
a = np.reshape(a,(3,3))
b = a.astype(np.int)
print b