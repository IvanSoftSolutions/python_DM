# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 19:36:35 2021

@author: ivand

@Description: Leer Las publicaciones del archivo csv. Procesar Las publicaciones
para extraer Las palabras con Los códigos previos. Calcular la probabilidad
condicional de cada palabra dado el género.

p. ej. p('aqui'|'m'), P('aqui'|'f'), P('hola'|'m' ), p('hola'|'f')

P(A|B) = P(AnB)/P(B)

Imprimir las 10 palabras más probables por género

Imprimir la intersección entre Las 20 palabras más probables de cada
género
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
    for p, s in zip(pubs, sexs):
        if (w in p) and (s == c):
            num += 1
        if s == c:
            dem += 1
    p_c = (num/n)/(dem/n)
    return p_c

def condprob_m(pubs, sexs, w, c):
    w_c = []
    n = 0
    for p, s in zip(pubs, sexs):
        if s == c:
            w_c.extend(p)
        n += len(p)
    num = w_c.count(w)
    dem = len(w_c)
    p_c = (num/n)/(dem/n)
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

pubs, voc = vocabulary(pubs, s_w)

# #--------------- Con el modelo Bernoulli --------------------
# #Probabilidad condicional de cada palabra dado que es mujer
# d_f = {}
# for w in voc:
#     p_c = condprob_b(pubs, sexs, w, 'f')
#     d_f[w] = p_c

# #Probabilidad condicional de cada palabra dado que es hombre
# d_m = {}
# for w in voc:
#     p_c = condprob_b(pubs, sexs, w, 'm')
#     d_m[w] = p_c
    
# #Ordenar las palabras por probabilidad para cad genero
# #Imprimir las 10 palabras mas probables por cada genero    
# l_w_f = sort_words(d_f)
# print('Palabras mas probables para las mujeres:')
# t = '\n'.join(w+f': {p:.3f}' for p, w in l_w_f[:10])
# print(t)
# print('-----------------------------------')
# l_w_m = sort_words(d_m)
# print('Palabras mas probables para los hombres:')
# t = '\n'.join(w+f': {p:.3f}' for p, w in l_w_m[:10])
# print(t)

# #Interseccion de las 20 palabras mas probables por genero
# print('---------------------------------------')
# mf_f = [w for p, w in l_w_f[:20]]
# mf_m = [w for p, w in l_w_m[:20]]
# mf_int = set(mf_f).intersection(set(mf_m))
# print(f'Interseccion de palabras: {mf_int}')

#--------------- Con el modelo Multinomial --------------------
#Probabilidad condicional de cada palabra dado que es mujer
d_f = {}
for w in voc:
    p_c = condprob_m(pubs, sexs, w, 'f')
    d_f[w] = p_c

#Probabilidad condicional de cada palabra dado que es hombre
d_m = {}
for w in voc:
    p_c = condprob_m(pubs, sexs, w, 'm')
    d_m[w] = p_c
    
#Ordenar las palabras por probabilidad para cad genero
#Imprimir las 10 palabras mas probables por cada genero    
l_w_f = sort_words(d_f)
print('Palabras mas probables para las mujeres:')
t = '\n'.join(w+f': {p:.3f}' for p, w in l_w_f[:10])
print(t)
print('-----------------------------------')
l_w_m = sort_words(d_m)
print('Palabras mas probables para los hombres:')
t = '\n'.join(w+f': {p:.3f}' for p, w in l_w_m[:10])
print(t)

#Interseccion de las 20 palabras mas probables por genero
print('---------------------------------------')
mf_f = [w for p, w in l_w_f[:20]]
mf_m = [w for p, w in l_w_m[:20]]
mf_int = set(mf_f).intersection(set(mf_m))
print(f'Interseccion de palabras: {mf_int}')