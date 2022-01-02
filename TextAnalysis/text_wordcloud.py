# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 15:04:31 2021

@author: ivand

@Description: Usando el código del ejercicio previo, generar una nube de
palabras con la libreria Wordcloud.

Para instalar el módulo WordCLoud, desde La terminal: pip install wordcloud
"""

from wordcloud import WordCloud
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
    pub = no_accents(pub)
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

wc = WordCloud(background_color='white', width=1200, height=1000, relative_scaling=1)

wc.generate_from_frequencies(d_freq)

plt.figure()
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
