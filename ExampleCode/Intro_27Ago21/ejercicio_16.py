# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 18:13:42 2021

@author: ivand

@ Dada una lista con strings, escribe un programa usando una comprensión de
 listas para generar una lista que contenga aquellos strings que contengan un
 punto
"""

l = ['sadasfd', 'dfg.dfg', 'sdfsgewrwersdfasd', 'gllw.er', 'retertweras.da']
x = [i for i in l if '.' in i]
print(x)