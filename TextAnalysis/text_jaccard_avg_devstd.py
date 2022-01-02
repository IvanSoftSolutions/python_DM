# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 19:09:09 2021

@author: ivand

@Description: Usando el código del ejercicio previo. Calcular el promedio
y la desviación estándar de la similitud (del indice Jaccard)
entre los usuarios de cada género.

u1 = {'hola', 'mundo', 'que', 'tal'}
u2 = {'perro', 'mundo', 'que', 'gato'}
u3 = {'perro', 'gato', 'que', 'sirena'}

j_l =  [[1, .6, e.8], --> u1
       [e.6, 1, е.5], --> и2
       [e.8, e.5, 1]] --> u3
 
       u1 u2 u3
l_s = [m, f, m] 

La salida es el promedio de similitud entre géneros:
Similitud promedio hombre/hombre = e.23
Similitud promedio mujer/mujer = 1
"""

from nltk.corpus import stopwords
import pandas as pd
import re
import math as mt

def no_accents(pub):
    pub = pub.replace('á', 'a')
    pub = pub.replace('é', 'e')
    pub = pub.replace('í', 'i')
    pub = pub.replace('ó', 'o')
    pub = pub.replace('ú', 'u')
    return pub

def clean_text(pub, s_w):
    pub = pub.lower()
    pub = no_accents(pub)
    tokens = re.findall('\w+', pub)
    tokens = [token for token in tokens
              if not token.isdigit()
              and token not in s_w
              and token.isalpha()
              and len(token) > 2 and len(token) < 20]
    return tokens

def vocabulary(l_pub, s_w):
    l_words = []
    for pub in l_pub:
        tokens = clean_text(pub, s_w)
        l_words.extend(tokens)
    voc = set(l_words)
    return voc

def jaccard(a, b):
    num = a.intersection(b)
    den = a.union(b)
    return len(num)/len(den)

def var_std(values):
    n = len(values)
    md = sum(values)/n
    num = [(x - md) **2 for x in values]
    num = sum(num)
    var = num/(n-1)
    std = mt.sqrt(var)
    return std

def percentil(values, p):
    pos = (len(values) - 1) * p
    pl = mt.floor(pos)
    pu = mt.ceil(pos)
    return values[pl]+(values[pu]-values[pl])*p

s_w = stopwords.words('spanish')
s_w.extend(['jajajaja', 'jaja', 'jajaja', 'mas'])
s_w = set(s_w)

w_d = 'C:/Users/ivand/Desktop/Universidad/Ago-Dic2021/MineriaDatos/FinalProject/'
i_f = w_d + 'fb_posts.csv'

df = pd.read_csv(i_f)

#Similitud promedio en grupos de genero
friends = df['amigo'].tolist()
friends = set(friends)
d_s = {'f':[], 'm':[]}
for i in friends:
    f_f = (df['amigo'] == i)
    l_pub = df[f_f]['publicacion'].tolist()
    l_sex = df[f_f]['sexo'].tolist()
    sex_a = l_sex[0]
    voc_a = vocabulary(l_pub, s_w)
    for j in friends:
        if i != j:
            f_f = (df['amigo'] == j)
            l_pub = df[f_f]['publicacion'].tolist()
            l_sex = df[f_f]['sexo'].tolist()
            sex_b = l_sex[0]
            voc_b = vocabulary(l_pub, s_w)
            inter = voc_a.intersection(voc_b)
            jacc = jaccard(voc_a, voc_b)
            if sex_a == sex_b:
                d_s[sex_a].append(jacc)

mean_f = sum(d_s['f'])/len(d_s['f'])
mean_m = sum(d_s['m'])/len(d_s['m'])
std_f = var_std(d_s['f'])
std_m = var_std(d_s['m'])
med_f = percentil(d_s['f'], 0.5)
med_m = percentil(d_s['m'], 0.5)
print(f'Similitud promedio mujer/mujer = {mean_f:.3f} +- {std_f:.3f}')
print(f'Similitud mediana mujer/mujer = {med_f:.3f}')
print(f'Similitud promedio hombre/hombre = {mean_m:.3f} +- {std_m:.3f}')
print(f'Similitud mediana hombre/hombre = {med_m:.3f}')
