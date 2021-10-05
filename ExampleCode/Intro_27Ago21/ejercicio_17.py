# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 18:28:42 2021

@author: 
    
@El ejercicio anterior, pero seleccionando solo aquellos strings que contengan
 'jpg' o 'png' después del punto (solo esos tres caracteres).
"""

l = ['sadasfd', 'dfg.jpg', 'sdfsgewrwersdfasd', 'gllw.png', 'retertweras.da']
substrings = ['.jpg', '.png']
x = [i for i in l if  any(j in i for j in substrings)]
print(x)