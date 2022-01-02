# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 22:25:56 2021

@author: ivand

@Description: Utilizando el código del ejercicio previo con la matriz dispersa
pesada con tf-idf, normalizar cada uno de Los vectores de documento utilizando
La norma euclidiana
                                      norma = sqrt(x_0^2+x_1^2+x_2^2+x_3^2)
tdm_sparse = [{0:2.25, 1:5.204},  --> sqrt(2.25^2+5.204^2) = sqrt(32.144) = 5.669
              {3:5.204, 4:2.602}, --> sqrt(5.204^2+2.602^2) = sqrt(33.852) = 5.818
              {e:2.25, 2:2.602}]  --> sqrt(2.25^2+2.604^2) = sqrt(11.832) = 3.439

Normalizando

tdm_sparse = [{0:2.25/5.669, 1:5.204/5.669},
              {3:5.204/5.818, 4:2.602/5.818},
              {0:2.25/3.439, 2:2.602/3.439}]

tdm_sparse = [{0:0.396, 1:0.917}, --> sqrt(0.396^2+0.917^2) = 0.998
              {3:0.894, 4:0.447}, --> sgrt(0.894^2+0.447^2) = 0.999
              {0:0.654, 2:0.756}] --> sqrt(0.654^2+0.756^2) = 0.999
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

def euc_norm(vec):
    norm = sum([v**2 for k, v in vec.items()])
    norm = mt.sqrt(norm)
    return norm

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
    
# Normalizar con la norma Euclideana
for i, row in enumerate(tdm_tfidf):
    norm = euc_norm(row)
    row = {k:v/norm for k, v in row.items()}
    tdm_tfidf[i] = row
    
    