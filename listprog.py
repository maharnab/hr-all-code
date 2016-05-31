# -*- coding: utf-8 -*-
"""
Created on Mon Apr 04 17:29:52 2016

@author: Maharnab
"""

L = []
command_list  = ['append', 'insert', 'remove', 'pop'] 
command_list += ['index', 'count', 'sort', 'reverse', 'print']

N = int(raw_input())
for i in range(0, N):
    command = raw_input()
    in_splt = command.split(" ", 1)
    if in_splt[0] == command_list[0]:
        in_splt_2 = command.split(" ", 1)
        L.append(int(in_splt_2[1]))
    if in_splt[0] == command_list[1]:
        in_splt_2 = command.split(" ", 2)
        L.insert(int(in_splt_2[1]), int(in_splt_2[2]))
    if in_splt[0] == command_list[2]:
        in_splt_2 = command.split(" ", 1)
        L.remove(int(in_splt_2[1]))
    if in_splt[0] == command_list[3]:
        L.pop()
    if in_splt[0] == command_list[4]:
        in_splt_2 = command.split(" ", 1)
        L.index(int(in_splt_2[1]))
    if in_splt[0] == command_list[5]:
        in_splt_2 = command.split(" ", 1)
        L.count(int(in_splt_2[1]))
    if in_splt[0] == command_list[6]:
        L.sort()
    if in_splt[0] == command_list[7]:
        L.reverse()
    if in_splt[0] == command_list[8]:
        print L