# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 21:37:05 2021

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

def odds_ratio(c_t, lab_1, lab_2):
    #Agregar condicion para valor de la tabla igual a 0. Hacer la correccion
    n11 = c_t[lab_1[0]][lab_2[0]]
    n10 = c_t[lab_1[0]][lab_2[1]]
    n01 = c_t[lab_1[1]][lab_2[0]]
    n00 = c_t[lab_1[1]][lab_2[1]]
    odds = (n11*n00)/(n10*n01)
    return odds

w_d = 'C:/Users/ivand/Desktop/Universidad/Ago-Dic2021/MineriaDatos/Data/'
i_f = w_d + 'info_students.csv'

df = pd.read_csv(i_f)

# [sex, videogame_console]
sex = df['sex'].tolist()
con = df['videogame_console'].tolist()
c_t = contingency_table(sex, con)
print('[sex, videogame_console]:', c_t)
odds = odds_ratio(c_t, ['h', 'm'], ['y', 'n'])
print(f'Odds ratio [sex, videogame_console]: {odds:.3f}')
print()

# [sex, pet]
pet = df['pet'].tolist()
pet = ['y' if m != 'n' else m for m in pet]
c_t = contingency_table(sex, pet)
print('[sex, pet]:', c_t)
odds = odds_ratio(c_t, ['h', 'm'], ['y', 'n'])
print(f'Odds ratio [sex, pet]: {odds:.3f}')
print()

# [videogame_console, pet]
c_t = contingency_table(con, pet)
print('[sex, pet]:', c_t)
odds = odds_ratio(c_t, ['y', 'n'], ['y', 'n'])
print(f'Odds ratio [videogame_console, pet]: {odds:.3f}')