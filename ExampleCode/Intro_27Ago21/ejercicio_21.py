# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 20:15:20 2021

@author: ivand

@Escribe un programa que solicite un string de solo letras al usuario y que
 determine si el string es un heterograma, es decir un string en el que cada
 letra solo ocurre una vez.
"""

x = str(input('Introduzca un string: '))
def isHeterogram():
    hash = [0] * 26
    for i in range(len(x)):
        if x[i] != ' ':
            if hash[ord(x[i]) - ord('a')] == 0:
                hash[ord(x[i]) - ord('a')] = 1
            else:
                return False
    return True

print('Si' if isHeterogram() else 'No')