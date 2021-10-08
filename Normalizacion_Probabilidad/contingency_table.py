# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 00:07:29 2021

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

w_d = 'C:/Users/ivand/Desktop/Universidad/Ago-Dic2021/MineriaDatos/Data/'
i_f = w_d + 'info_students.csv'

df = pd.read_csv(i_f)

# [sex, videogame_console]
sex = df['sex'].tolist()
con = df['videogame_console'].tolist()
c_t = contingency_table(sex, con)
print('[sex, videogame_console]:', c_t)
# In percentages
p_h_y = c_t['h']['y']/(c_t['h']['y']+c_t['h']['n'])
p_m_y = c_t['m']['y']/(c_t['m']['y']+c_t['m']['n'])
print(f'Men with videogame console:{p_h_y:.3f}%')
print(f'Women with videogame console:{p_m_y:.3f}%')

# [sex, pet]
pet = df['pet'].tolist()
pet = ['y' if m != 'n' else m for m in pet]
c_t = contingency_table(sex, pet)
print('[sex, pet]:', c_t)
# In percentages
p_h_y = c_t['h']['y']/(c_t['h']['y']+c_t['h']['n'])
p_m_y = c_t['m']['y']/(c_t['m']['y']+c_t['m']['n'])
print(f'Men with pet:{p_h_y:.3f}%')
print(f'Women with pet:{p_m_y:.3f}%')

# [videogame_console, pet]
c_t = contingency_table(con, pet)
print('[videogame_console, pet]:', c_t)
# In percentages
p_y_y = c_t['y']['y']/(c_t['y']['y']+c_t['y']['n'])
p_n_y = c_t['n']['y']/(c_t['n']['y']+c_t['n']['y'])
print(f'Console with pet:{p_y_y:.3f}%')
print(f'No console with pet:{p_n_y:.3f}%')