# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 14:14:16 2021

@author: ivand

@Dada una lista llena con strings (crea una lista por tu cuenta), escribe un
 programa que devuelva cuál es el string más largo de la lista.

"""

l = ['asdasd', 'dfgdfgd', 'wtwerwetwerwer', 'tyiuyiyuiyuiyui', 'tyrty']
x = max(l, key=len)
print(x)