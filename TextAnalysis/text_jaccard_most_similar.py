# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 18:51:01 2021

@author: ivand

@Description: Usando el código del ejercicio previo. Encontrar para cada
usuario cual es el usuario que más se le parece, de acuerdo con el indice
Jaccard.

u1 = {'hola', 'mundo', 'que', 'tal'}
u2 = {'perro', 'mundo', 'que', 'gato'}
u3 = {'perro', 'gato', 'que', 'sirena'}

JA(u1, u2) = 0.3333
JA(u1, u3) = 0.14
JA(u2, u3) = 0.25

u1: usuario mas similar es u2
u2: usuario mas similar es u1
u3: usuario mas similar es u2
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

#Palabras comunes por usuario
friends = df['amigo'].tolist()
friends = set(friends)
for i in friends:
    f_f = (df['amigo'] == i)
    l_pub = df[f_f]['publicacion'].tolist()
    voc_a = vocabulary(l_pub, s_w)
    l_f = []
    for j in friends:
        if i != j:
            f_f = (df['amigo'] == j)
            l_pub = df[f_f]['publicacion'].tolist()
            voc_b = vocabulary(l_pub, s_w)
            inter = voc_a.intersection(voc_b)
            jacc = jaccard(voc_a, voc_b)
            l_f.append((jacc, j))
    l_f.sort(reverse=True)
    ms_j = l_f[0][0]
    ms_f = l_f[0][1]
    print(f'{i}: usuario mas similar es {ms_f}, ij = {ms_j:.3f}')
    