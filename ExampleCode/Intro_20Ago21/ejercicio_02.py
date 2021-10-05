# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 01:51:58 2021

@author: ivand

@Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó
 $10, el segundo $20, el tercero $40 y así sucesivamente. Calcular cada pago
 mensual y el total de lo que pagó después de los 20 meses.
"""

x = int(input('Introduzca el primer pago: '))
y = 0
for i in range(21):
    y += x
    x *= 2
    print(x)
print(y)