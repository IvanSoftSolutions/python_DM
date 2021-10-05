# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 20:56:51 2021

@author: ivand

@Escribe un programa que genere una lista llena con números enteros aleatorios
"""

import random as r
l = []
for i in range(10):
    l.append(r.randint(0, 20))
print(l)