# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 23:30:15 2021

@author: ivand
"""

import pandas as pd
import math as mt

def cond_prob(values_1, values_2, l_1, l_2):
    n = len(values_1)
    num = den = 0
    for v_1, v_2 in zip(values_1, values_2):
        if v_1 == l_1 and v_2 == l_2:
            num += 1
        if v_2 == l_2:
            den += 1
    num /= n
    den /= n
    cp = num/den
    return cp

def cond_prob_iter(values_1, values_2, lab_1, lab_2):
    for l_1 in lab_1:
        for l_2 in lab_2:
            p_c = cond_prob(values_1, values_2, l_1, l_2)
            print(f'Conditionale probability of [{l_1}|{l_2}] = {p_c:.3f}')
    pass

w_d = 'C:/Users/ivand/Desktop/Universidad/Ago-Dic2021/MineriaDatos/Data/'
i_f = w_d + 'info_students.csv'

df = pd.read_csv(i_f)

#Lista de variables nominales
sex = df['sex'].tolist()
con = df['videogame_console'].tolist()
pet = df['pet'].tolist()
pet = ['y' if m != 'n' else m for m in pet]
sex_l = list(set(sex))
con_l = list(set(con))
pet_l = list(set(pet))

print('Conditional probability between sex and videogame console')
cond_prob_iter(sex, con, sex_l, con_l)
print('-----------------------------------------------------------')
print('Conditional probability between sex and pet')
cond_prob_iter(sex, pet, sex_l, pet_l)
print('-----------------------------------------------------------')
print('Conditional probability between videogame console and pet')
cond_prob_iter(con, pet, con_l, pet_l)
print('-----------------------------------------------------------')
