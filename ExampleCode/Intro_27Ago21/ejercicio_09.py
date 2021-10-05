# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 14:00:07 2021

@author: ivand

@Dado un string (defínelo tú), escribe un programa que genere otro string
 compuesto por las dos primeras y las dos últimas letras del string original.
 Si la longitud del string original es menor que 2, que devuelva la leyenda
 "Empty string".
"""
x = 'mineria de datos'
y = ''
if len(x) > 2:
    y = x[:2] + x[-2:]
else:
    print('Empty string')
print(y)