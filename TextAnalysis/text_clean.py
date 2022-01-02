# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 13:52:20 2021

@author: ivand

@Descrition: Leer archivo de publicaciones de amigos csv y para cada
publicacion:
    1.- ConvertirLa a minusculas
    2.- Separarla en tokens usando espacios o una expresion regular \w+
    3. - Quitar Los tokens de cada publicacion que sean solo numeros
"""

import pandas as pd
import re

w_d = 'C:/Users/ivand/Desktop/Universidad/Ago-Dic2021/MineriaDatos/FinalProject/'
i_f = w_d + 'fb_posts.csv'

df = pd.read_csv(i_f)

l_pub = df[ 'publicacion'].tolist()

# Punto 1
l_pub = [pub.lower() for pub in l_pub]

#Punto 2
l_pub = [re.findall('\w+', pub) for pub in l_pub]

#Punto 3
l_pub = [[token for token in pub if not token.isdigit()] for pub in l_pub]