# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 06:49:09 2021

@author: ivand

@Dada una lista de tuplas, escribe un programa que ordene cada tupla dentro de
 la lista en orden descendente.
"""

l = [(7, 9, 3, 4), (5, 6, 1, 2), (8, 5, 6)]
x = []
for i in range(len(l)):
    x.append(tuple(sorted(l[i], reverse=True)))
print(x)
