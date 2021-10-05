# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 07:12:22 2021

@author: ivand

@Dadas tres listas llenas con números enteros, escribe un programa que encuentre
 todos los elementos que comparten las tres listas.
"""

l1 = [1, 2, 3, 4, 5]
l2 = [2, 3, 5, 8, 9]
l3 = [1, 3, 5, 7, 10, 9]
x = set(l1)
y = set(l2)
z = set(l3)
aux = x.intersection(y)
resultado = aux.intersection(z)
print(list(resultado))