# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 17:40:04 2021

@author: ivand
"""

import pandas as pd
import matplotlib.pyplot as plt
import math as mt

def trim_data(values, a):
    n = len(values)
    k = int(a/100*n)
    print(f'Valores a recortar: {k}')
    return values[k:n-k]

def var_std(values):
    n = len(values)
    md = sum(values)/n
    num = [(x - md)**2 for x in values]
    num = sum(num)
    var = num/(n - 1)
    std = mt.sqrt(var)
    return var, std

def outliers(values, fq, tq):
    iqr = tq - fq
    uif = tq + 1.5 * iqr
    lif = fq - 1.5 * iqr
    for i in values:
        if i >= lif:
            lw = i
            break
    for i in values[::-1]:
        if i <= uif:
            uw = i
            break
    outs = []
    for i in values:
        if i < lw or i > uw:
            outs.append(i)
    return iqr, lif, uif, lw, uw, outs

def percentil(values, p):
    pos = (len(values) - 1) * p
    pl = mt.floor(pos)
    pu = mt.floor(pos)
    return values[pl] + (values[pu] - values[pl]) * p

def summary(values, var): 
    n = len(values)
    index = list(range(n))
    
    #Dispersion natural
    plt.figure()
    plt.scatter(index, values)
    plt.title(f'{var}')
    
    #Dispersion ordenada
    values.sort()
    plt.figure()
    plt.scatter(index, values)
    plt.title(f'{var}')
    
    #Resumen de los cinco numeros
    mi = values[0]
    mx = values[-1]
    fq = percentil(values, 0.25)
    med = percentil(values, 0.50)
    tq = percentil(values, 0.75)
    print(f'Mínimo = {mi:.2f}')
    print(f'Máximo = {mx:.2f}')
    print(f'1er cuartil = {fq:.2f}')
    print(f'Mediana = {med:.2f}')
    print(f'3er cuartil = {tq:.2f}')
    
    #Mean
    md = sum(values)/len(values)
    print(f'Media/promedio = {md:.2f}')
    
    #Varianze and standard deviation
    vari, std = var_std(values)
    print(f'Varianza = {vari:.2f}')
    print(f'Desviación estándar {std:.2f}')
    
    #Boxplot
    plt.figure()
    plt.boxplot(values)
    plt.title(f'{var}')
    
    #Find outliers
    iqr, lif, uif, lw, uw, outs = outliers(values, fq, tq)
    print(f'IQR = {iqr:.2f}')
    print(f'LIF = {lif:.2f}')
    print(f'UIF = {uif:.2f}')
    print(f'LW = {lw:.2f}')
    print(f'UW = {uw:.2f}')
    print(f'Outliers = {outs}')
    print(f'Total outliers = {len(outs)}')
    
    # #Generate a histogram
    # n_bins = 5
    # bins = get_bins(values, n_bins)
    # plt.figure()
    # plt.hist(values, n_bins)
    # plt.title(f'{var}')
    # print(f'Bins = {bins}')
    
w_d = 'C:/Users/ivand/Desktop/Universidad/Ago-Dic2021/MineriaDatos/Code/Practica_past/'
i_f = w_d + 'survey_results.csv'

df = pd.read_csv(i_f)

l_v_nominal = ['name', 'sex', 'pet', 'city_origin', 'videogame_console']
l_v_inter = ['age', 'height', 'weight', 'semester', 'courses_taken']
l_v = ['Age']

for v in l_v:
    print(f'**************** {v} *****************')
    print('---------------- Valores completos -----------------')
    values = df[v].tolist()
    summary(values, v)
    print('----------------------------------------------------')
    
    print('++++++++++++++++ Valores recortados +++++++++++++++')
    values = trim_data(values, 10)
    summary(values, v)
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print('*********************************')