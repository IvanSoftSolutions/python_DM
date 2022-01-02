# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 15:39:39 2021

@author: ivand

@Description: Usando el código del ejercicio previo, encontrar el
vocabulario por usuario y por género. Devolver el conjunto de palabras
comunes entre cada par de usuarios y cada entre géneros.

u1 = {'hola', 'mundo', 'que', 'tal '}
u2 = {'perro', 'mundo', 'que', 'gato'}
u3 = {'perro', 'gato', 'que', 'sirena'}

u1 int u2 = ['mundo', 'que']
u1 int u3 = ['que']
u2 int u3 = ['perro', 'gato', 'que']
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

s_w = stopwords.words('spanish')
s_w.extend(['jajajaja', 'jaja', 'jajaja', 'mas'])
s_w = set(s_w)

w_d = 'C:/Users/ivand/Desktop/Universidad/Ago-Dic2021/MineriaDatos/FinalProject/'
i_f = w_d + 'fb_posts.csv'

df = pd.read_csv(i_f)

# #Palabras comunes por usuario
# friends = df['amigo'].tolist()
# friends = set(friends)
# for friend_a in friends:
#     f_f = (df['amigo'] == friend_a)
#     l_pub = df[f_f]['publicacion'].tolist()
#     voc_a = vocabulary(l_pub, s_w)
#     for friend_b in friends:
#         f_f = (df['amigo'] == friend_b)
#         l_pub = df[f_f]['publicacion'].tolist()
#         voc_b = vocabulary(l_pub, s_w)
#         inter = voc_a.intersection(voc_b)
#         print(f'Palabras en comun entre {friend_a} y {friend_b} = {inter}')
        
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
        print(f'Palabras en comun entre {sex_a} y {sex_b} = {inter}')