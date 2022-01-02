# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 15:06:39 2021

@author: ivand

@Description: Utilizando el código del ejercicio previo para generar
La matriz términos-documentos. Construir una estructura para almacenar
solo Los elementos que no sean ceros utilizando el indice de las palabras.

La salida es una lista de diccionarios.

t_d_m = [[2, 4, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 4, 2],
         [2, 0, 0, 0, 0, 0, 0, 2]]

        0   1   2   3   4   5  6   7
voc = [we, w1, w2, w3, w4, w5, w6, w7]

tdm_sparse = [{e:2, 1:4},
              {6:4, 7:2),
              {0:2, 3:2}]

"""

from nltk.corpus import stopwords
import pandas as pd
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

def tokenizer(l_pub, s_w):
    l_words = []
    l_pub_tok = [] 
    for pub in l_pub:
        tokens = clean_text(pub, s_w)
        l_pub_tok.append(tokens)
        l_words.extend(tokens)
    voc = set(l_words)
    return l_pub_tok, voc

s_w = stopwords.words('spanish')
s_w.extend(['jajajaja', 'jaja', 'jajaja', 'mas'])
s_w = set(s_w)

w_d = 'C:/Users/ivand/Desktop/Universidad/Ago-Dic2021/MineriaDatos/FinalProject/'
i_f = w_d + 'fb_posts.csv'

df = pd.read_csv(i_f)

pubs = df['publicacion'].tolist()

#Formar vocabulario y tokenizar las publicaciones
pubs, voc = tokenizer(pubs, s_w)
voc = list(voc)

tdm = []
for pub in pubs:
    v = {}
    for w in pub:
        idx = voc.index(w)
        v[idx] = v.get(idx, 0) + 1
    tdm.append(v)