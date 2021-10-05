# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 13:49:08 2021

@author: ivand

@Dada una lista llena con números flotantes (crea una lista por tu cuenta),
 escribe un programa que calcule la suma y el promedio de todos los elementos.
"""

l = [1, 2, 3, 4, 30 ,6, 7, 8, 9, 10, 20]
length = len(l)
suma = 0
for i in range(length):
    suma += l[i]
promedio = suma/length
print('Suma: ', suma, ' Promedio: ', promedio)