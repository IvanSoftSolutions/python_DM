# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 12:04:49 2021

@author: ivand
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

def vocabulary(l_pub, s_w):
    l_words = []
    # l_pub_tok = [] 
    for pub in l_pub:
        tokens = clean_text(pub, s_w)
        # l_pub_tok.append(tokens)
        l_words.extend(tokens)
    voc = set(l_words)
    return voc

s_w = stopwords.words('spanish')
s_w.extend(['jajajaja', 'jaja', 'jajaja', 'mas'])
s_w = set(s_w)

w_d = 'C:/Users/ivand/Desktop/Universidad/Ago-Dic2021/MineriaDatos/FinalProject/'
i_f = w_d + 'fb_posts.csv'

df = pd.read_csv(i_f)

pubs = df['publicacion'].tolist()
sexs = df['sexo'].tolist()

# -------------------------- Vocabulary ------------------------------
voc = vocabulary(pubs, s_w)
n = len(pubs)

# ---------------------------- Training --------------------------------
prior = {}
c_prob = {'f':{}, 'm':{}}
for sex in sexs:
    f_s = (df['sexo'] == sex)
    l_pub = df[f_s]['publicacion'].tolist()
    n_sex = len(l_pub)
    prior[sex] = n_sex/n
    t_doc = []
    for pub in l_pub:
        tokens = clean_text(pub, s_w)
        t_doc.append(tokens)
    t_total = [item for sublist in t_doc for item in sublist]
    t_freq = {}
    for t in voc:
        if t_total.count(t) == 0:
            continue
        t_freq[t] = t_total.count(t)
    for t in voc:
        if t not in t_freq:
            c_prob[t] = 0.000001
            continue
        num = t_freq[t] + 1
        den = sum(t_freq.values()) + len(t_freq.values())
        c_prob[sex][t] = num/den

# --------------------------- Test ---------------------------
d = 'Amigos'
w = clean_text(d, s_w)
score = {}
for sex in sexs:
    score[sex] = mt.log(prior[sex])
    for t in w:
        if t not in c_prob[sex]:
            score[sex] += 0.00000001
            continue
        score[sex] += mt.log(c_prob[sex][t])
d_label = max(score, key=score.get)
print(f'This publication comes from a {d_label}')
        