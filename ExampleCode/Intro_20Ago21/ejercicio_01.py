# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 14:19:55 2021

@author: ivand

@Solicitar n calificaciones flotantes, encontrar las calificaciones menor y mayor
"""

n = int(input('Enter number of grades: '))
l = []
if(n > 0):
    for i in range(n):
        x = float(input('Enter grade: '))
        l.append(x)
x = max(l)
y = min(l)
        
print('El valor maximo es: ', x, 'y el valor minimo es: ', y)        
        