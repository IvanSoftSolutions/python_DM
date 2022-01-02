# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 11:06:02 2020

@author: d3ads
"""
from nltk.corpus import stopwords
import math as mt
import numpy as np
import re

def clean_text(s, s_w):
    s = s.lower()
    words = re.findall('[a-záéíóúüñ]+', s)
    l = [w for w in words if w not in s_w and w.isalpha() and len(w) >= 3 and len(w) <= 25]
    return l

def TrainMultinominalNB(C, D):
    V = [D[i] for i in D]
    N = len(D) #20
    prior = {}
    condprob = {}
    
    for c in C:
        Nc = CountDocsInClass(D, c)
        prior[c] = Nc / N
        Textc = ConcatenateTextOfAllDocsInClass(D, c)
        term = term_document(Textc)
        condprob[c] = CondProb(term)
        
    return V, prior, condprob
        
def CountDocsInClass(D, c):
    lst = [l_d[i] for i in D.keys()]
    return lst.count(c)

def ConcatenateTextOfAllDocsInClass(Dic, G):
    dic = {}
    lst =[]
    
    for i in l_d:
        if l_d[i] == G:
            dic[l_d[i]] = []
            
            for j in Dic[i]:
                lst.append(j)      
                
    for i in dic.keys():
        dic[i].extend(lst)
    return dic

def term_document(D):
    lst = []
    dic = {}
    k = 0
    
    for u in D:
        lst.append([])
        dic[u] = []
        
        for i in voc:
            if i in D[u]:
                count = D[u].count(i)
                lst[k].append(count)
            else:
                lst[k].append(0)
                
        dic[u].extend(lst[k])
        k += 0
        
    return dic

def CondProb(Tct):
    lst = []   
    for u in Tct:
        for j in Tct[u]:
            suma = (j+1) / (sum(Tct[u])+len(voc))
            lst.append(suma)
    return lst

def ApplyMultinominalNB(C, V, prior, condprob, d):
    dic = {}
    
    for c in condprob: #m, h
        W = ExtractTokensFromDoc(d, condprob, c)
        a = 1
        for i in W:
            if i in d:
                a = a * (W[i]**d.count(i))
                
        a = a * prior[c]
        dic[c] = a
        
    return dic

def ApplyMultinominalNB2(C, V, prior, condprob, d):
    score = {}
    suma = 0
    lst = []
    
    for c in condprob:
        W = ExtractTokensFromDoc(d, condprob, c)
        for i in W:
            if i in d:
                b = mt.log(W[i])
                
                if d.count(i) > 1:
                    for p in range(d.count(i)):
                        suma += b
                else:
                    suma += b
        score[c] = suma + mt.log(prior[c])
        lst.append(score[c])
        
    index = np.argmax(lst)
    value = lst[index]
    

    return value, score
        
def ExtractTokensFromDoc(d, condprob, c):
    lista = [u if u in d else '' for u in voc]
    dic = {}
    
    for i in range(len(lista)):
        if lista[i] != '':
            new = condprob[c]
            dic[lista[i]] = new[i]
    return dic
                
#%%
w_d = 'C:/Users/d3ads/Desktop/ESCUELA/10MO SEMESTRE/MINERIA DE DATOS/Proyecto/Nueva carpeta/'
p_f = w_d + 'posts.txt'
l_f = w_d + 'labels.txt'
u_f = w_d + 'users.txt'

s_w = stopwords.words('spanish')
s_w.extend(['jaja', 'jajaja', 'jiji', 'bno', 'plss', 'tsu', 'jajajajajajajajaja',
            'aaaaah', 'aaayyy', 'aahh', 'jajaahhh', 'jajaj', 'jajajaa', 'jajajaajajajjaa', 'jajajaja', 'jajajajaj', 'jajajajaja', 'jajakasjajs', 'jajjajaja', 'jajjajajaja', 'jajjajja', 'jajs'])
s_w = set(s_w)

p_d = {}
l_d = {}
voc = []

with open(p_f, 'r', encoding = 'utf-8') as p_r, open(l_f, 'r', encoding = 'utf-8') as l_r, open(u_f, 'r', encoding= 'utf-8') as u_r:
    for p, l, u in zip(p_r, l_r, u_r):
        u = u.strip()
        p = p.strip()
        l = l.strip()
        
        words = clean_text(p, s_w)
           
        if u not in p_d:
            p_d[u] = []
            
        p_d[u].extend(words)
        l_d[u] = l
        voc.extend(words)

voc = set(voc)
voc = sorted(voc)

clase = [l_d[str(i)] for i in range(len(l_d))]
V, prior, condprob = TrainMultinominalNB(set(clase), p_d)

x = ''
while(x == ''):
    x = input('Frase: ')

d = clean_text(x, s_w)
a = ApplyMultinominalNB(set(clase), V, prior, condprob, d)
print(a)

value, score = ApplyMultinominalNB2(set(clase), V, prior, condprob, d)
print('\n', score)
print(value)