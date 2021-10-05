# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 14:55:55 2021

@author: ivand

@Dada una lista con strings, escribe un programa usando una comprensión de
 listas para generar una lista que contenga las longitudes de cada string de la
 lista original.
"""

l = ['sadasfd', 'dfgdfg', 'sdfsgewrwersdfasd', 'gllwer', 'retertwerasda']
x = [len(i) for i in l]
print(x)