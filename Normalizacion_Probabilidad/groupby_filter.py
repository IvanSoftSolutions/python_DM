# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 18:30:35 2021

@author: ivand
"""

import matplotlib.pyplot as plt
import pandas as pd

def split_column(df, l_v, val):
    l_v_t = [x for x in l_v]
    l_v_t.append(val)
    records = df[l_v_t].to_records(index=False)
    records = list(records)
    values = []
    for record in records:
        r = []
        if '/' in record[-1]:
            op = record[-1].split('/')
            for o in op:
                r = [e for e in record]
                r[-1] = o
                values.append(r)
        else:
            r = [e for e in record]
            values.append(r)
    df_out = pd.DataFrame(values)
    df_out.columns = l_v_t
    return df_out

def plots_pandas(df, var, val):
    groups = df.groupby(val)[var].apply(list)
    titles = list(groups.keys())
    n_g = len(groups)
    fig, axs = plt.subplots(1, n_g)
    for i, (group, title) in enumerate(zip(groups, titles)):
        group.sort()
        x = list(range(len(group)))
        axs[i].scatter(x, group)
        axs[i].set_title(title)
    plt.suptitle(f'{var} by {val}')
    plt.figure()
    df.boxplot(column=[var], by=val)
    plt.figure()
    df[var].hist(bins=8, by=df[val])
    plt.suptitle(f'{var} by {val}')
    
def summary_pandas(df, l_v, val):
    labels = df[val].unique().tolist()
    for v in l_v:
        for label in labels:
            label_filter = df[val] == label
            print(f'----------------Valores completos para {label} para la variable {v} ---------------')
            print(df[label_filter][v].describe())
            print('--------------------------------------------')
            # a = 10
            # print(f'++++++++ Valores recortados para {label} para la variable {v} al {a}% +++++++++')
            # n = df[v].count()
            # k = int(a/100*n)
            # df_trim = df.sort_values(by=v, ignore_index=True)
            # df_trim = df_trim[k:n-k]
            # print(df_trim[label_filter][v].describe())
            # print('+++++++++++++++++++++++++++++++++++++++++++++++')
            print('++++++++++++++++++++++')
        plots_pandas(df, v, val)
        # plots_pandas(df_trim, v, val)
        
w_d = 'C:/Users/ivand/Desktop/Universidad/Ago-Dic2021/MineriaDatos/Data/'
i_f = w_d + 'info_students.csv'

df = pd.read_csv(i_f)

l_v = ['age', 'height', 'weight', 'semester', 'courses_taken']
l_v = ['height']

summary_pandas(df, l_v, 'sex')

# df_out = split_column(df, l_v, 'pet')
# summary_pandas(df_out, l_v, 'pet')
