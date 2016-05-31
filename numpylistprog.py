# -*- coding: utf-8 -*-
"""
Created on Mon Apr 04 22:58:47 2016

@author: Maharnab
"""

import numpy as np

inp_nums = raw_input()
insplt = inp_nums.split(" ")
insplt.reverse()
a = np.array(insplt)
b = a.astype(np.float)
print b