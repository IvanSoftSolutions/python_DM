# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 13:36:22 2021

@author: ivand

@Escribir un programa que imprima los números pares entre 1 y un número entero
 dado por el usuario
"""

x = int(input('Introduzca numero limite '))
for i in range(x):
    if i % 2 > 0:
        continue
    else:
        print(i)