# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 14:40:12 2021

@author: ivand

@Dada una lista llena con enteros y strings mezclados (crea una lista por tu
 cuenta), escribe un programa que separe en dos listas los strings de los
 enteros.
"""

l = ['asdasd', 2, 1, 'asdasd', 'fgfd', 4, 6, 8, 9]
x = [i for i in l if isinstance(i, int)]
y = [i for i in l if isinstance(i, str)]
print(x)
print(y)