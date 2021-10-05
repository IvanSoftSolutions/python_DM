# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 13:40:39 2021

@author: ivand

@Dada una lista de tres números enteros (crea una lista por tu cuenta), escribe
 un programa que determine si la lista está ordenada en orden ascendente o 
 descendente.
"""

l = [3, 2, 1]
if(l[0] > l[1] and l[1] > l[2]):
    print('Descendente')
elif(l[0] < l[1] and l[1] < l[2]):
    print('Ascendente')