# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 13:23:26 2021

@author: ivand
"""
from scipy.stats import chi2
import pandas as pd

def contingency_table(values_1, values_2):
    d_s = {}
    for i, j in zip(values_1, values_2):
        if i not in d_s:
            d_s[i] = {}
        d_s[i][j] = d_s[i].get(j, 0) + 1
    return d_s

def chi_square(c_t, lab_1, lab_2):
    total = sum([sum([v1 for k1, v1 in v.items()]) for k, v in c_t.items()])
    chi = 0
    for r in lab_1:
        s_r = sum([sum([v1 for k1, v1 in v.items()])
                  for k, v in c_t.items() if k == r])
        for c in lab_2:
            s_c = sum([sum([v1 for k1, v1 in v.items() if k1 == c])
                  for k, v in c_t.items()])
            ev = s_r*s_c/total
            ov = c_t[r][c]
            chi += ((ov - ev)**2)/ev
    return chi

w_d = 'C:/Users/ivand/Desktop/Universidad/Ago-Dic2021/MineriaDatos/Data/'
i_f = w_d + 'info_students.csv'

df = pd.read_csv(i_f)

# [sex, videogame_console]
sex = df['sex'].tolist()
con = df['videogame_console'].tolist()
c_t = contingency_table(sex, con)
print('[sex, videogame_console]:', c_t)
phi = chi_square(c_t, ['h', 'm'], ['y', 'n'])
print(f'Chi square [sex, videogame_console]: {phi:.3f}')
print()

# [sex, pet]
pet = df['pet'].tolist()
pet = ['y' if m != 'n' else m for m in pet]
c_t = contingency_table(sex, pet)
print('[sex, pet]:', c_t)
phi = chi_square(c_t, ['h', 'm'], ['y', 'n'])
print(f'Chi square [sex, pet]: {phi:.3f}')
print()

# [videogame_console, pet]
c_t = contingency_table(con, pet)
print('[videogame_console, pet]:', c_t)
phi = chi_square(c_t, ['y', 'n'], ['y', 'n'])
print(f'Chi square [videogame_console, pet]: {phi:.3f}')

#Nivel de confianza, comunmente 0.05 o 0.01. Entre mas pequeno
#mayor confianza de rechazar la hipotesis nula
p = 0.01       
n_r = len(c_t)
n_c = len(c_t['y'])
df = (n_r-1)*(n_c-1)
#Calcula el valor de la distribucion chi^2 en tablas (o con la ecuacion)
#p, grados de libertad
chi_dist = chi2.isf(p, df)
print('====================================================')
print(f'Valor de la distribucion chi^2 con {df} grados de libertad y {p} nivel de confianza = {chi_dist}')