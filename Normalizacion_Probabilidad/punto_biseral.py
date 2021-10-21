# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 22:58:33 2021

@author: ivand
"""

import pandas as pd
import math as mt

def var_std(values):
    n = len(values)
    md = sum(values)/n
    num = [(x - md)**2 for x in values]
    num = sum(num)
    var = num/(n-1)
    std = mt.sqrt(var)
    return std

def point_biseral(values_1, values_2, lab):
    n = len(values_1)
    n0 = n1 = m0 = m1 = 0        
    for l, v in zip(values_1, values_2):
        if l == lab[0]:
            n0 += 1
            m0 += v
        else:
            n1 += 1
            m1 += v
    sy = var_std(values_2)
    m0 /= n0
    m1 /= n1
    t1 = (m0 - m1)/sy
    t2 = mt.sqrt((n0/n)*(n1/n))
    rpd = t1*t2
    return rpd

w_d = 'C:/Users/ivand/Desktop/Universidad/Ago-Dic2021/MineriaDatos/Data/'
i_f = w_d + 'info_students.csv'

df = pd.read_csv(i_f)

#Lista de variables intervalo/razon
l_v = ['age', 'height', 'weight', 'semester', 'courses_taken']
l_v = ['courses_taken']

#Lista de variables nominales
sex = df['sex'].tolist()
con = df['videogame_console'].tolist()
pet = df['pet'].tolist()
pet = ['y' if m != 'n' else m for m in pet]

#Para la variable genero
for v in l_v:
    values = df[v].tolist()
    rpd = point_biseral(sex, values, ['h', 'm'])
    print(f'Point biseral correlation [sex, {v}] = {rpd:.3f}')
    
#Para la variable consola de videojuegos
for v in l_v:
    values = df[v].tolist()
    rpd = point_biseral(con, values, ['y', 'n'])
    print(f'Point biseral correlation [video game console, {v}] = {rpd:.3f}')

#Para la variable genero
for v in l_v:
    values = df[v].tolist()
    rpd = point_biseral(pet, values, ['y', 'n'])
    print(f'Point biseral correlation [pet, {v}] = {rpd:.3f}')

