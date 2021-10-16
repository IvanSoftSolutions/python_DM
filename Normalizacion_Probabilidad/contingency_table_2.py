# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 19:13:48 2021

@author: ivand
"""

import pandas as pd

def contingency_table(values_1, values_2):
    d_s = {}
    for i, j in zip(values_1, values_2):
        if i not in d_s:
            d_s[i] = {}
        d_s[i][j] = d_s[i].get(j, 0) + 1
    return d_s

def grouping(values, n):
    mn = min(values)
    rang = max(values) - mn
    inter = rang / n
    ul = mn +inter
    d = {}
    for i in range(n):
        d[ul] = i
        ul += inter
    l = []
    for v in values:
        for t in d:
            if v <= t:
                l.append(d[t])
                break
    return l, d

w_d = 'C:/Users/ivand/Desktop/Universidad/Ago-Dic2021/MineriaDatos/Data/'
i_f = w_d + 'info_students.csv'

df = pd.read_csv(i_f)

#Lista de variables intervalo/razon
l_v = ['age', 'height', 'weight', 'semester', 'courses_taken']
l_v = ['age', 'height']

for i in range(len(l_v) - 1):
    for j in range(i+1, len(l_v)):
        values_1 = df[l_v[i]].tolist()
        values_2 = df[l_v[j]].tolist()
        values_1, r_1 = grouping(values_1, 3)
        values_2, r_2 = grouping(values_2, 3)
        c_t = contingency_table(values_1, values_2)
        print(r_1)
        print(r_2)
        print(f'[{l_v[i]}], [{l_v[j]}]:', c_t)
    