# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 07:21:04 2021

@author: ivand

@ Escribe un programa para encontrar los elementos repetidos dentro de una tupla
 y que genere una lista con ellos. 
 Dado un número entero, escribe un programa que lo escriba con letras. 123 -->
 uno dos tres
"""

# =============================================================================
# t = (1,3,4,32,1,1,1,31,32,12,21,2,3)  
# l = []
# for i in t:
#     if i not in l:
#         if t.count(i) > 1:
#             l.append(i)
# print(l)
# =============================================================================

x = {1:'uno', 2:'dos', 3:'tres', 4:'cuatro', 5:'cinco', 6:'seis', 7:'siete',
     123:'uno dos tres'}
z = int(input('Introduzca un numero: '))
print(x[z])