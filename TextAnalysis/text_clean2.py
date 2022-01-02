# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 14:30:08 2021

@author: ivand

@Description: Usando el código del ejercicio previo, ahora

1. Eliminar las palabras vacias (stopwords) de cada publicación utilizando
la lista precompilada que encontramos en elmódulo NLTK (Natural Language Tool Kit)

2. Remover tokens que sean una combinación de letras y números, y remover
tokens que sean muy cortos o muy Largos.

3. En Los tokens cambiar caracteres acentuados por no acentuados

4. Volver a calcular la frecuencia de palabras

5. Volver a formar el vocabulario, es decir, la lista de palabras únicas
que encuentro en todos Los textos

6. Generar una gráfica de barras para la frecuencia de palabras.
"""

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
    #Punto 3
    pub = no_accents(pub)
    #Punto 1 y 2
    tokens = re.findall('\w+', pub)
    tokens = [token for token in tokens
              if not token.isdigit()
              and token not in s_w
              and token.isalpha()
              and len(token) > 2 and len(token) < 20]
    return tokens

s_w = stopwords.words('spanish')
s_w = set(s_w)

w_d = 'C:/Users/ivand/Desktop/Universidad/Ago-Dic2021/MineriaDatos/FinalProject/'
i_f = w_d + 'fb_posts.csv'

df = pd.read_csv(i_f)

l_pub = df[ 'publicacion'].tolist()

l_clean = []
for pub in l_pub:
    tokens = clean_text(pub, s_w)
    l_clean.append(tokens)

#Frecuencias
d_freq = {}
for pub in l_clean:
    for token in pub:
        d_freq[token] = d_freq.get(token, 0) + 1

l_freq = [(freq, token) for token, freq in d_freq.items()]
l_freq.sort(reverse=True)

#Vocabulario
voc = [token for token in d_freq]
voc.sort()

labels = []
values = []
for freq, token in l_freq:
    labels.append(token)
    values.append(freq)

plt.bar(labels, values)