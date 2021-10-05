# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 14:23:15 2021

@author: ivand

@Dado un string (defínelo tú), escribe un programa que genere otro string en
 donde todas las repeticiones del primer caracter son reemplazadas por el
 caracter $, excepto el primer caracter.
"""

x = 'mineria de datos'
y = '$'
z = x[0] + x[1:].replace(x[0], y)
print(str(z))