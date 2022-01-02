# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 21:25:13 2021

@author: ivand

@Description: Utilizando el código del ejercicio previo para generar
La matriz términos-documentos con representación dispersa, aplicar el
pesado tf-idf para cada vector de documento.
        0   1   2   3   4
voc = [w0, w1, w2, w3, w4]

tdm= [[2, 4, 0, 0, 0],
      [0, 0, 0, 4, 2],
      [2, 0, 2, 0, 0]]

df   = [2, 1, 1, 1, 1]
1+df = [3, 2, 2, 2, 2]
n_d = 3 --> Número de documentos
(1+n_d)/(1+df(t)) = [4/3, 4/2, 4/2, 4/2, 4/2]
Log ((1+n_d)/(1+df(t))) = [0.125, 0.301, 0.301, 0.301, 0.301]
Log ((1+n_d)/(1+df(t)))+1 = [1.125, 1.301, 1.301, 1.301, 1.301]

idf(t, d) = log((1+n_d)/(1+df(t))) + 1

tdm_sparse = [{0:2*1.125, 1:4*1.301},
              {3:4*1.301, 4:2*1.301},
              {0:2*1.125, 2:2*1.301}]
"""

from nltk.corpus import stopwords
import pandas as pd
import math as mt
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

#Calcular la frecuencia de documentos
# En cuantos documentos aparece cada palabra
dof = [0]*len(voc)
for row in tdm:
    for c in row:
        dof[c] += 1

# Clacular el idf, la frecuencia de documentos invertida
# log((1+n_d)/(1+df(t)))+1
nd = len(tdm) + 1
idf = []
for v in dof:
    den = 1+v 
    res = mt.log(nd/den)+1
    idf.append(res)

# Calcular la matriz tf-idf final
tdm_tfidf = []
for row in tdm:
    v = {}
    for c, f in row.items():
        v[c] = f*idf[c]
    tdm_tfidf.append(v)
    


