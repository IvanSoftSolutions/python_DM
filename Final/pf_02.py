# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 13:04:25 2021

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
    l_pub_tok = [] 
    for pub in l_pub:
        tokens = clean_text(pub, s_w)
        l_pub_tok.append(tokens)
        l_words.extend(tokens)
    voc = set(l_words)
    return l_pub_tok, voc

def condprob_b(pubs, sexs, w, c):
    n = len(pubs)
    num = 0
    dem = 0
    num2 = 0
    dem2 = 0
    p_c = {}
    for p, s in zip(pubs, sexs):
        if (w in p) and (s == c):
            num += 1
        else:
            num += 0.000000000001
        if w in p:
            dem += 1
        else:
            dem += 0.000000000001
        if (w not in p) and (s == c):
            num2 += 1
        if w not in p:
            dem2 += 1
    p_c['in'] = (num/n)/(dem/n)
    p_c['not'] = (num2/n)/(dem2/n)
    return p_c

def sort_words(d):
    l_w = [(p, w) for w, p in d.items()]
    l_w.sort(reverse=True)
    return l_w 

s_w = stopwords.words('spanish')
s_w.extend(['jajajaja', 'jaja', 'jajaja', 'mas'])
s_w = set(s_w)

w_d = 'C:/Users/ivand/Desktop/Universidad/Ago-Dic2021/MineriaDatos/FinalProject/'
i_f = w_d + 'fb_posts.csv'

df = pd.read_csv(i_f)

pubs = df['publicacion'].tolist()
sexs = df['sexo'].tolist()

# -------------------------- Vocabulary ------------------------------
l_pub_tok, voc = vocabulary(pubs, s_w)
n = len(pubs)

# Probability of category
p_sex = {}
for sex in sexs:
    f_s = (df['sexo'] == sex)
    l_pub = df[f_s]['publicacion'].tolist()
    n_sex = len(l_pub)
    p_sex[sex] = n_sex/n
    
# Probability of t in posts and NOT in posts
w_prob = {}
n_w = 0
for w in voc:
    w_in = 0
    w_not = 0
    for p in l_pub_tok:
        if w in p:
            w_in += 1
        else:
            w_not += 1
        n_w += len(p)
    w_prob[w] = {'in': w_in/n_w, 'not': w_not/n_w}

# Probability of category given t appeared and given DOES NOT appeared
p_ct = {'f':{}, 'm':{}}
for w in voc:
    p_ct['f'][w] = condprob_b(pubs, sexs, w, 'f')
    p_ct['m'][w] = condprob_b(pubs, sexs, w, 'm')
    
# Information gain
i_g = {}
x_c = 0
x_ct = 0
x_ct_not = 0
sexs = set(sexs)
for sex in sexs:
    x_c +=  p_sex[sex]*mt.log(p_sex[sex])
for sex in sexs:
    for w in voc:
        x_ct += (p_ct[sex][w]['in'])*mt.log(p_ct[sex][w]['in'])
        x_ct_not += p_ct[sex][w]['not']*mt.log(p_ct[sex][w]['not'])
        i_g[w] = - x_c + w_prob[w]['in']*x_ct + w_prob[w]['not']*x_ct_not

# Sort by information gain and return highest 50
h_ig = sort_words(i_g)
t = '\n'.join(w+f': {p:.3f}' for p, w in h_ig[:50])
print(t)