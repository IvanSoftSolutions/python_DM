# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 14:06:39 2021

@author: ivand

@Descrition: Usando el código previo
1. Encontrar La frecuencia de cada token en todas Las publicaciones.
Ordenar Los tokens de mayor a menor frecuencia.

p1 = ['hola', 'mundo', 'que', 'tal']
p2 = ['si', 'me', 'gusta', 'el', "mundo']
p3 = ['si', 'vamos', 'quel', 'tal', 'y', 'gano'] 

d = {'hola':1, 'mundo':2, 'que':2, 'tal':2, 'si':2, ...}

l = [(2, 'mundo'), (2, 'que'), (2, 'tal'), (2, 'si'), (1, 'hota')...]

2. Formar el vocabulario, es decir, La lista de palabras únicas que encuentro
en todas Las publicaciones.

voc = ['hola', 'mundo', 'que', 'tal', 'si', 'me', 'gusta', 'el',
       'vamos', 'y', 'gano']

3. Generar una gráfica de barras para la frecuencia de palabras.

"""

import pandas as pd
import matplotlib.pyplot as plt
import re

w_d = 'C:/Users/ivand/Desktop/Universidad/Ago-Dic2021/MineriaDatos/FinalProject/'
i_f = w_d + 'fb_posts.csv'

df = pd.read_csv(i_f)

l_pub = df[ 'publicacion'].tolist()

# Minusculas
l_pub = [pub.lower() for pub in l_pub]

#Separar 
l_pub = [re.findall('\w+', pub) for pub in l_pub]

#Tokens
l_pub = [[token for token in pub if not token.isdigit()] for pub in l_pub]

#Punto 1 (Frecuencias)
d_freq = {}
for pub in l_pub:
    for token in pub:
        d_freq[token] = d_freq.get(token, 0) + 1

l_freq = [(freq, token) for token, freq in d_freq.items()]
l_freq.sort(reverse=True)

#Punto 2 (Vocabulario/Palabras unicas)
voc = [token for token in d_freq]
voc.sort()

#Punto 3 (Grafica de barras)
labels = []
values = []
for freq, token in l_freq:
    labels.append(token)
    values.append(freq)

plt.bar(labels, values)
