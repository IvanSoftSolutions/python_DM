# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 20:51:52 2021

@author: ivand

@Dados dos diccionarios (definidos por ti), escribe un programa que devuelva una
 lista con las llaves que ambos comparten.
"""

x = {1:'uno', 2:'dos', 'tres':'tres', 'cuatro':10, 'cinco':5, 'seis':7}
y = {'uno':'uno', 'dos':'dos', 'tres':'tres', 4:10, 5:2, 'seis':7}
l = []
for k in x:
    if k in y:
        l.append(k)
print(l)