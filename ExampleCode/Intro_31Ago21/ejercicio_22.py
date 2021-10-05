# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 20:35:53 2021

@author: ivand

@Escribe un programa que tome un diccionario con llaves string y valores strings
 y números (definido por ti) y que devuelva la suma y promedio de todos los
 valores que son numéricos.
"""

x = {'uno':'uno', 'dos':'dos', 'tres':'tres', 'cuatro':10, 'cinco':5, 'seis':7}
y = x.items()
suma = 0
aux = 0
for k, v in y:
    if isinstance(v, int):
        suma += v
        aux += 1
print(suma)
print(suma/aux)