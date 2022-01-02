# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 16:48:30 2021

@author: ivand

@Description: Usando el código del ejercicio previo, encontrar el
vocabulario por usuario y por género. Calcular entre cada usuario o género
el indice de Jaccard.

Métrica de similitud
J(A, B) = |A ^ B| / |A V B|

u1 = {'hola', 'mundo', 'que', 'tal'}
u2 = {'perro', 'mundo', 'que', 'gato'}
u3 = {'perro', 'gato', 'que', 'sirena'}

JA(u1, u2) = |['mundo', 'que ']|/
             |['hola', 'mundo', 'que', 'tal', 'perro', 'gato']|
JA(u1, u2) = 2/6 = 0.3333

JA(u1, u3) = |['que']|/
             |['hola', 'mundo', 'que', 'tal ', 'perro', 'gato', 'sirena']|
JA(u1, u3) = 1/7 = 0.14

J --> [0, 1] ==> 0 = Los conjuntos no se parecen
                 1 = Los conjuntos son idénticos
"""

from wordcloud import WordCloud
from nltk.corpus import stopwords
import pandas as pd
import matplotlib.pyplot as plt
import re

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

s_w = stopwords.words('spanish')
s_w.extend(['jajajaja', 'jaja', 'jajaja', 'mas'])
s_w = set(s_w)

w_d = 'C:/Users/ivand/Desktop/Universidad/Ago-Dic2021/MineriaDatos/FinalProject/'
i_f = w_d + 'fb_posts.csv'

df = pd.read_csv(i_f)

# #Palabras comunes por usuario
# friends = df['amigo'].tolist()
# friends = list(set(friends))
# for i in range(len(friends)-1):
#     f_f = (df['amigo'] == friends[i])
#     l_pub = df[f_f]['publicacion'].tolist()
#     voc_a = vocabulary(l_pub, s_w)
#     for j in range(i+1, len(friends)):
#         f_f = (df['amigo'] == friends[j])
#         l_pub = df[f_f]['publicacion'].tolist()
#         voc_b = vocabulary(l_pub, s_w)
#         inter = voc_a.intersection(voc_b)
#         jacc = jaccard(voc_a, voc_b)
#         print(f'Indice Jaccard entre {friends[i]} y {friends[j]} = {jacc}')
        
#Palabras comunes por genero
sexs = df['sexo'].tolist()
sexs = set(sexs)
for sex_a in sexs:
    f_s = (df['sexo'] == sex_a)
    l_pub = df[f_s]['publicacion'].tolist()
    voc_a = vocabulary(l_pub, s_w)
    for sex_b in sexs:
        f_s = (df['sexo'] == sex_b)
        l_pub = df[f_s]['publicacion'].tolist()
        voc_b = vocabulary(l_pub, s_w)
        inter = voc_a.intersection(voc_b)
        jacc = jaccard(voc_a, voc_b)
        print(f'Indice Jaccard entre {sex_a} y {sex_b} = {jacc}')