# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 13:54:27 2021

@author: ivand

@Dada una lista llena con números enteros (crea una lista por tu cuenta),
 escribe un programa que devuelva la lista original sin elementos duplicados.
"""

l = [1, 2, 3, 4, 2, 2, 1, 4, 5, 2, 4, 5]
x = list(set(l))
print(x)