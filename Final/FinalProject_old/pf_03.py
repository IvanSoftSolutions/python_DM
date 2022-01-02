# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from nltk.corpus import stopwords
import re
import math as mt
import numpy as np

def clean_text(s, s_w):
    s = s.lower()
    words = re.findall('[a-záéíóúüñ]+', s)
    l = [w for w in words if w not in s_w and w.isalpha() and
         len(w) > 2 and len(w) < 26]
    return l

def term_doc(voc):
    tdm = []
    for u in p_d:
        text = p_d[u]
        vector = []
        for word in voc:
            vector.append(text.count(word))
        tdm.append(vector)

    df = [0]*len(voc)
    for row in tdm:
        for i, column in enumerate(row):
            if column != 0:
                df[i] += 1

    nd = 1+len(tdm)
    idf = []
    for val in df:
        idf.append(mt.log(nd/(1+val))+1)
    
    tdm_tfidf = []
    for row in tdm:
        vector = []
        for i, column in enumerate(row):
            vector.append(column*idf[i])
        tdm_tfidf.append(vector)
    
    tdm_tfidf_norm = []
    for row in tdm_tfidf:
        norm = 0
        temp = []
        for column in row:
            norm += column**2
        norm = norm **(1/2)
        for column in row:
            temp.append(column/norm)
        tdm_tfidf_norm.append(temp)
    return tdm_tfidf_norm

#-------------------------NMF Algorithm---------------------------
def mu(x, r, s_iter, delta):
    w = np.random.rand(np.size(x, 0), r)
    h = np.random.rand(r, np.size(x, 1))
    for n in range(s_iter):
        
        w_tx = w.T @ x
        w_twh = w.T @ w @ h + delta
        for i in range(np.size(h, 0)):
            for j in range (np.size(h, 1)):
                h[i, j] = h[i, j] * w_tx[i, j] / w_twh[i, j]
        
        xh_t = x @ h.T
        whh_t = w @ h @ h.T + delta
        for i in range(np.size(w, 0)):
            for j in range(np.size(w, 1)):
                w[i, j] = w[i, j] * xh_t[i, j] / whh_t [i, j]
        
        frob_norm = np.linalg.norm(x - w @ h, 'fro')
        print("iteration" + str(n + 1) + ": " + str(frob_norm))
    return w, h

def print_clusters(w, voc, r):
    sorted_w = w[:, np.argsort(w.sum(axis=0))]
    for i in range(np.size(w, 1)):
        cluster = []
        idx = (-sorted_w[:, i]).argsort()[:r]
        for j in range(np.size(idx)):
            cluster.append(voc[idx[j]])
        print('Cluster' + str(i + 1) + ': ' + ', '.join(cluster))

#%%        
w_d = 'C:/users/ivand/Desktop/ProyectoFinal/'
p_f = w_d + 'posts.txt'
l_f = w_d + 'labels.txt'
u_f = w_d + 'users.txt'

s_w = stopwords.words('spanish')
s_w.extend(['jaja', 'jajaja', 'jajajaja', 'jajajajaja', 'jajajajajaja'
'this', 'and', 'the'])
s_w = set(s_w)

p_d = {}
l_d = {}
voc = []

with open(p_f, 'r', encoding='utf-8') as p_r, \
    open(l_f, 'r', encoding='utf-8') as l_r, \
    open(u_f, 'r', encoding='utf-8') as u_r:
        for p, l, u in zip(p_r, l_r, u_r):
            l = l.strip()
            p = p.strip()
            u = u.strip()
            words = clean_text(p, s_w)
            if u not in p_d:
                p_d[u] = []
            p_d[u].extend(words)
            l_d[u] = l
            voc.extend(words)
voc = set(voc)
voc = list(voc)

r = input("Introduzca el tamaño r para las matrices W y H: ")
s_iter = input("Establezca el numero de iteraciones: ")
r = int(r)
s_iter = int(s_iter)

x = term_doc(voc)
w, h = mu(x, r, s_iter, delta = 0.0000001)
print_clusters(w, voc, r)