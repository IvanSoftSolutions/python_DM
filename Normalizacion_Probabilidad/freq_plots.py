# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 00:42:14 2021

@author: ivand
"""

import pandas as pd
import matplotlib.pyplot as plt

def summary(df, var):    
    dataList = df[var].tolist()
    dataLen = len(dataList)
    index = list(range(dataLen))
    d = {}
    n = 0
    for val in dataList:
        for v in val.split('/'):
            v = v.lower().strip()
            d[v] = d.get(v, 0) + 1
            n += 1
    
    freqs = []
    for v, f in d.items():
        freqs.append((f, f/n*100, v))
        
    freqs.sort(reverse=True)
    lab = []
    val = []
    for f, p, v in freqs:
        print(f'{v}:{f}:{p:.2f}%')
        lab.append(v)
        val.append(f)
        
    plt.figure()    
    plt.pie(val, labels=lab)
    plt.title(f'{var}')
    plt.figure()
    plt.bar(lab, val)
    plt.title(f'{var}')
    plt.figure()
    plt.scatter(index, dataList)
    plt.title(f'{var}')
    plt.figure()
    dataList.sort()
    plt.scatter(index, dataList)
    plt.title(f'{var}')

w_d = 'C:/Users/ivand/Desktop/Universidad/Ago-Dic2021/MineriaDatos/Data/'
i_f = w_d + 'info_students.csv'

df = pd.read_csv(i_f)

l_v_nominal = ['name', 'sex', 'pet', 'city_origin', 'videogame_console']
l_v_inter = ['age', 'height', 'weight', 'semester', 'courses_taken']

for v in l_v_inter:
    print(f'**************** {v} *****************')
    summary(df, v)
    print('*********************************')
