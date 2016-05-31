# -*- coding: utf-8 -*-
"""
Created on Fri May 06 23:50:05 2016

@author: Maharnab
"""

import sys

time = raw_input().strip()

if "AM" in time:
    newtime1 = time.replace("AM", "")
    arr1 = newtime1.split(':')
    if arr1[0] == "12":
        arr1[0] = "00"
        print ':'.join(arr1)
    else:
        print newtime1

if "PM" in time:
    newtime2 = time.replace("PM", "")
    arr2 = newtime2.split(':')
    el1 = int(arr2[0]) + 12
    if arr2[0] == "12":
        print ':'.join(arr2)
    else:
        arr2[0] = str(el1)
        print ':'.join(arr2)

    