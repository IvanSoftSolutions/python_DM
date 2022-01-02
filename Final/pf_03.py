# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 11:56:48 2021

@author: ivand
"""

from nltk.corpus import stopwords
import pandas as pd
import math as mt
import numpy as np
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
    # l_pub_tok = [] 
    for pub in l_pub:
        tokens = clean_text(pub, s_w)
        # l_pub_tok.append(tokens)
        l_words.extend(tokens)
    voc = set(l_words)
    return voc

def user_text(l_pub, s_w):
    l_words = [] 
    for pub in l_pub:
        tokens = clean_text(pub, s_w)
        l_words.extend(tokens)
    return l_words

def euc_norm(vec):
    norm = sum([v**2 for k, v in vec.items()])
    norm = mt.sqrt(norm)
    return norm

def euc_distance(i, j):
    x_l = tdm_tfidf[i].values()
    y_l = tdm_tfidf[j].values()
    dist = []
    for x, y in zip(x_l, y_l):
        dist.append((y - x)**2)
    return dist

s_w = stopwords.words('spanish')
s_w.extend(['jajajaja', 'jaja', 'jajaja', 'mas'])
s_w = set(s_w)

w_d = 'C:/Users/ivand/Desktop/Universidad/Ago-Dic2021/MineriaDatos/FinalProject/'
i_f = w_d + 'fb_posts.csv'

df = pd.read_csv(i_f)

pubs = df['publicacion'].tolist()
voc = vocabulary(pubs, s_w)
voc = list(voc)
# Concatenate text of each user
users = df['amigo'].tolist()
users = set(users)

up_l = [] 
for user in users:
    u_f = (df['amigo'] == user)
    pubs = df[u_f]['publicacion'].tolist()
    u_p = user_text(pubs, s_w)
    up_l.append(u_p)

# Generate tdm
tdm = []
for u in up_l:
    v = {}
    for w in u:
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
    
# Normalizar con la norma Euclideana
for i, row in enumerate(tdm_tfidf):
    norm = euc_norm(row)
    row = {k:v/norm for k, v in row.items()}
    tdm_tfidf[i] = row
    
# Create proximity matrix
p_m = []
for i in range(len(tdm_tfidf)):
    d_r = []
    for j in range(len(tdm_tfidf)):
        x_l = tdm_tfidf[i].values()
        y_l = tdm_tfidf[j].values()
        dist = []
        for x, y in zip(x_l, y_l):
            dist.append((y - x)**2)
        d = sum(dist)
        d = mt.sqrt(d)
        d_r.append(d)
    p_m.append(d_r)
    
# Get min value and indexes of value
r_l = []
min_l = []
for i in range(len(p_m)):
    min_v = min(v for v in p_m[i] if v > 0)
    min_l.append(min_v)
i_2 = min_l.index(min(min_l))
for idx, l in enumerate(p_m):
    if min_l[i_2] in l:
        i_1 = idx
for i in range(len(p_m)):
    p_m[i].pop(i_1)
    p_m[i].pop(i_2)
n_v = []
for a, b in zip(p_m[i_1], p_m[i_2]):
    if a < b:
        n_v.append(a)
    else:
        n_v.append(b)
p_m.pop(i_1)
p_m.pop(i_2)
p_m.append(n_v)
r_l.append([i_1, i_2])

        