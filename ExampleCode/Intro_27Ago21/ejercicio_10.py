# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 14:10:22 2021

@author: ivand

@Dado un string (defínelo tú), escribe un programa que remueva el enésimo
 caracter de ese string (definir n tú mismo). Comprobar que el string tiene más
 de n caracteres.
"""

x = 'mineria de datos'
y = ''
n = 8
if len(x) > n:
    y = x[n]
else:
    print('Not enough characters')
print(y)