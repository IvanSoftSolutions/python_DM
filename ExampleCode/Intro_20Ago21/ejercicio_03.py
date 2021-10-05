# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 02:24:20 2021

@author: ivand

@ Una persona empieza a ahorrar 2 centavos el 1 de enero, 4 centavos el 2 de
 enero, 8 centavos el 3, 16 el 4 y así sucesivamente hasta el 31 de diciembre.
 Calcular cuánto habrá ahorrado en PESOS al final del año (año no bisiesto).
"""

x = 1
for i in range(365):
    x *= 2
    print(x)
x /= 100
print(x)