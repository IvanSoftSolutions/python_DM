# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 14:44:23 2021

@author: ivand

@Description: Transformar Las publicaciones del archivo CSVra una matriz
términos-documentos. Cada publicación (cada renglón) se considera un
documento.

1. Extraer el vocabulario como el conjunto de palabras únicas

2. Formar un vector para cada publicación al iterar sobre Las palabras del
vocabulario y contar cuántas veces aparece cada una en la publicación.

3. Agreagar el vector a la matrix términos documentos.

t_d_m = [] # Una Lista de Listas, cada Lista interna es el vector de una
            publicación
            
L_re = [['Banana', 'Apple', 'Banana', 'Banana', 'Banana', 'Apple'],
        ['Banana', 'Orange', 'Banana', 'Banana', 'Orange ', 'Banana'],
        ['Apple', 'Orange', 'Orange', 'Apple']]

voc = ['Apple', 'Banana', 'Orange']

t_d_m = [[2, 4, 0],
         [0, 4, 2].
         [2, 0, 2]]
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

def tokenizer(l_pub, s_w):
    l_words = []
    l_pub_tok = [] 
    for pub in l_pub:
        tokens = clean_text(pub, s_w)
        l_pub_tok.append(tokens)
        l_words.extend(tokens)
    voc = set(l_words)
    return l_pub_tok, voc

s_w = stopwords.words('spanish')
s_w.extend(['jajajaja', 'jaja', 'jajaja', 'mas'])
s_w = set(s_w)

w_d = 'C:/Users/ivand/Desktop/Universidad/Ago-Dic2021/MineriaDatos/FinalProject/'
i_f = w_d + 'fb_posts.csv'

df = pd.read_csv(i_f)

pubs = df['publicacion'].tolist()

#Paso 1: Formar vocabulario y tokenizar las publicaciones
pubs, voc = tokenizer(pubs, s_w)
voc = list(voc)

tdm = []
for pub in pubs:
    v = []
    for w in voc:
        c = pub.count(w)
        v.append(c)
    tdm.append(v)
    
#La matriz resultante va a tener muchos ceros 
# ya que hay muchas palabras en el vocabulario
# pero cada publicaion tiene muy pocas palabras
# del total (vocabulario)

# Matriz dispersa (tiene muchos ceros) 

