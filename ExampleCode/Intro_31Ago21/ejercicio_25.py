# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 20:59:46 2021

@author: ivand

@Dado un string (definido por ti), escribe un programa que genere un diccionario
 en donde la llave es la posición de cada caracter del string y el valor el
 propio caracter.
"""

x = 'mineria de datos'
y = list(x)
z = {k:v for k, v in enumerate(y)}
print(z)