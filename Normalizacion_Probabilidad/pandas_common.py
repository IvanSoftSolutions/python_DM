# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 13:16:12 2021

@author: ivand
"""

import matplotlib.pyplot as plt
import pandas as pd

w_d = 'C:/Users/ivand/Desktop/Universidad/Ago-Dic2021/MineriaDatos/Data/'
f_i = w_d + 'info_students.csv'
df = pd.read_csv(f_i)

print(df.describe())

print(df[['age', 'semester']].describe())
df.boxplot(column ='age')
df.boxplot()
df[['age', 'semester']].boxplot()

ageMean = df['age'].mean()
ageMedian = df['age'].median()
print(df[['age', 'semester']].mean())
print(df[['age', 'semester']].median())
print(df[['age', 'semester']].quantile(.25))

print(df['age'] > 21)

sex_filter = (df['sex'] == 'm')
age_filter = (df['age'] > 21)
null_filter = df['age'].notnull()

print(df[sex_filter])
print(df[age_filter])
print(df[null_filter])

print(df.sort_values(by='age'))

console_filter = (df['videogame_console'] == 'y')
sex_console_filter = (df['videogame_console'] == 'y') & (df['sex'] == 'm')
print(df[sex_console_filter])
sex_console_filter = (df['videogame_console'] == 'y') & (df['sex'] == 'h')
print(df[sex_console_filter])

print(df[sex_console_filter][['age', 'semester']])
print(df[sex_console_filter][['age', 'semester']].describe())
df[sex_console_filter].boxplot(column = 'age')
df[sex_console_filter][['age', 'semester']].boxplot()

df[sex_console_filter].plot(x='age', y='semester', kind='scatter')

df.hist()
df['age'].hist()
df[sex_console_filter].hist('age')
df[sex_console_filter].hist(['age', 'semester'])


