# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 02:24:20 2021

@author: ivand

@Solicitar n números enteros y decir cuántos son pares, cuántos impares, cuántos
 negativos, cuantos positivos y cuántos ceros
"""

n = int(input('Introduzca la cantidad de numeros: '))
l = []
pares = 0
impares = 0
negativos = 0
positivos = 0
ceros = 0
if(n > 0):
    for i in range(n):
        x = int(input('Enter grade: '))
        l.append(x)
length = len(l)
for j in range(length):
    if(l[j] % 2 == 0):
        pares += 1
    elif(l[j] % 2 > 0):
        impares += 1
    if(l[j] > 0):
        positivos += 1
    elif(l[j] < 0):
        negativos += 1
    if(l[j] == 0):
        ceros += 1
print('Pares: ', pares, ' Impares: ', impares, ' Negativos: ', negativos,
      ' Positivos: ', positivos, ' Ceros: ', ceros)