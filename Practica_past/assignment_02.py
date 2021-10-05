# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 14:38:36 2021

@author: ivand
"""

# =============================================================================
# 2. Compute the five-number summary, the mean, and the standard deviation for the 
# annual salary and draw the boxplots for the 4 most common ethnicities (the ones
# with more answers, you must compute the statistics for each one). Besides, answer
# the following questions by computing all the additional and necessary statistics
# and drawing the necessary graphs/plots.
# =============================================================================

import math
import pandas as pd
import matplotlib.pyplot as plt
import operator

# =============================================================================
# --------------------------Five number summary--------------------------------
# =============================================================================
#------ Frequency -------
def freq(lst):
    freq = {}
    for i in lst:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq

#------ Percentiles -------
def percentile(lst, perc):
    n = len(lst)
    position = ( n - 1 ) * perc
    ql = math.floor(position)
    qu = math.ceil(position)
    return lst[ql] + (lst[qu] - lst[ql]) * perc

#------- Mean ---------
def mean(lst):
   return sum(lst) / len(lst)

#-------- Outliers ---------
def outliers(lst):
    fq = percentile( lst, 0.25)
    tq = percentile( lst, 0.75)
    IQR = tq - fq
    UIF = tq + (1.5 * IQR )
    LIF = fq - (1.5 * IQR )
    for i in lst:
        if i >= LIF:
            n_lw = i
            break
    for i in lst[::-1]:
        if i <= UIF:
            n_uw = i
            break
    outliers = []
    for i in lst:
        if i < n_lw or i > n_uw:
            outliers.append(i)
    return outliers, n_lw, n_uw

#------- Trimmed Data --------
def trim_data(lst, a):
    k = a / 100 * len(lst)
    k = math.floor(k)
    n_lst = lst[k:len(lst)-k]
    return n_lst

#------- Standard Variation -------
def std_var(lst):
    mn = mean(lst)
    n =len(lst)
    num = [( x - mn )**2 for x in lst]
    num = sum(num)
    var = num /( n - 1 ) 
    std = math.sqrt(var)
    return var, std

#------- 5 Number Summary -------
def summary(lst,title):
    lst.sort()
    mi = lst [0]
    mx = lst[-1]
    med = percentile(lst, 0.5)
    fq  = percentile(lst,0.25)
    tq  = percentile(lst,0.75)
    rango = mx - mi
    iqr = tq - fq
    outs, lw, uw = outliers(lst)
    mn = mean(lst)
    var, std = std_var(lst)
    
    #------- Console Data Print -------    
    print('Data quantity: ', len(lst))
    print('Minimum: ', mi)
    print('Maximum: ', mx)
    print('Median: ', med)
    print('1st quartile: ', fq)
    print('3rd quartile: ', tq)
    print('Mean: ', mn)
    print('Range: ', rango)
    print('IQR: ', iqr )
    print('Standard deviation: ', std)

    #------- Plot --------    
    plt.title(title)
    plt.boxplot(lst)
    plt.figure()
    print('\n')
    
# =============================================================================
# a. Which ethnicity has more answers?

def gender_answers():
    lst_man = df[f_genderMan]['Gender'].tolist()
    lst_woman = df[f_genderWoman]['Gender'].tolist()
    lst_nonb = df[f_genderNonB]['Gender'].tolist()
    print('Number of answers Man: ', len(lst_man))
    print('Number of answers Woman: ', len(lst_woman))
    print('Number of answers Non-Binary: ', len(lst_nonb))
    labels = 'Man', 'Woman', 'Non-Binary...'
    sizes = [len(lst_man), len(lst_woman), len(lst_nonb)]
    colors = ['blue', 'pink', 'gray']
    plt.pie(sizes, labels=labels, colors=colors)
    plt.figure()
    print('\n')
    
# =============================================================================
# b. Which gender tends to have higher salaries, and which one tends to have 
# lower salaries?

def lower_salaries():
    lst_man = df[f_genderMan]['ConvertedComp'].tolist()
    lst_woman = df[f_genderWoman]['ConvertedComp'].tolist()
    lst_nonb = df[f_genderNonB]['ConvertedComp'].tolist()
    mean_man = mean(lst_man)
    mean_woman = mean(lst_woman)
    mean_nonb = mean(lst_nonb)
    gender = {'Man': mean_man, 'Woman': mean_woman, 'NonB': mean_nonb}
    keys = gender.keys()
    values = gender.values()
    plt.bar(keys, values)
    plt.figure()
    print('The salary median for gender = Man is: ', mean_man)
    print('The salary median for gender = Woman is: ', mean_woman)
    print('The salary median for gender = Non-Binary... is: ', mean_nonb)
    print('\n')

# =============================================================================
# c. What are the most popular and less popular programming language per gender?

def lang_pop():
    lst_man = df[f_genderMan]['LanguageWorkedWith'].tolist()
    lst_woman = df[f_genderWoman]['LanguageWorkedWith'].tolist()
    lst_nonb = df[f_genderNonB]['LanguageWorkedWith'].tolist()
    temp_man = []
    temp_woman = []
    temp_nonb = []
    lst_lan_man = []
    lst_lan_woman = []
    lst_lan_nonb = []
    for i in range(len(lst_man)):
        temp_man.append(lst_man[i].split(';'))
    for i in range(len(lst_woman)):
        temp_woman.append(lst_woman[i].split(';'))
    for i in range(len(lst_nonb)):
        temp_nonb.append(lst_nonb[i].split(';'))
    for i in temp_man:
        for j in i:
            lst_lan_man.append(j)
    for i in temp_woman:
        for j in i:
            lst_lan_woman.append(j)
    for i in temp_nonb:
        for j in i:
            lst_lan_nonb.append(j)
    freq_lan_man = freq(lst_lan_man)
    freq_lan_woman = freq(lst_lan_woman)
    freq_lan_nonb = freq(lst_lan_nonb)
    lan_man_max = max(freq_lan_man, key=freq_lan_man.get)
    lan_woman_max = max(freq_lan_woman, key=freq_lan_woman.get)
    lan_nonb_max = max(freq_lan_nonb, key=freq_lan_nonb.get)
    lan_man_min = min(freq_lan_man, key=freq_lan_man.get)
    lan_woman_min = min(freq_lan_woman, key=freq_lan_woman.get)
    lan_nonb_min = min(freq_lan_nonb, key=freq_lan_nonb.get)
    print('The most popular language for gender = Man is: ', lan_man_max)
    print('The most popular language for gender = Woman is: ', lan_woman_max)
    print('The most popular language for gender = Non-Binary... is: ', lan_nonb_max)
    print('\n')
    print('The least popular language for gender = Man is: ', lan_man_min)
    print('The least popular language for gender = Woman is: ', lan_woman_min)
    print('The least popular language for gender = Non-Binary... is: ', lan_nonb_min)  
    print('\n')

# =============================================================================
# d. What are the most popular and less popular developer type per gender?

def devtype_pop():
    lst_man = df[f_genderMan]['DevType'].tolist()
    lst_woman = df[f_genderWoman]['DevType'].tolist()
    lst_nonb = df[f_genderNonB]['DevType'].tolist()
    temp_man = []
    temp_woman = []
    temp_nonb = []
    lst_type_man = []
    lst_type_woman = []
    lst_type_nonb = []
    for i in range(len(lst_man)):
        temp_man.append(lst_man[i].split(';'))
    for i in range(len(lst_woman)):
        temp_woman.append(lst_woman[i].split(';'))
    for i in range(len(lst_nonb)):
        temp_nonb.append(lst_nonb[i].split(';'))
    for i in temp_man:
        for j in i:
            lst_type_man.append(j)
    for i in temp_woman:
        for j in i:
            lst_type_woman.append(j)
    for i in temp_nonb:
        for j in i:
            lst_type_nonb.append(j)
    freq_type_man = freq(lst_type_man)
    freq_type_woman = freq(lst_type_woman)
    freq_type_nonb = freq(lst_type_nonb)
    type_man_max = max(freq_type_man, key=freq_type_man.get)
    type_woman_max = max(freq_type_woman, key=freq_type_woman.get)
    type_nonb_max = max(freq_type_nonb, key=freq_type_nonb.get)
    type_man_min = min(freq_type_man, key=freq_type_man.get)
    type_woman_min = min(freq_type_woman, key=freq_type_woman.get)
    type_nonb_min = min(freq_type_nonb, key=freq_type_nonb.get)
    print('The most popular type for gender = Man is: ', type_man_max)
    print('The most popular type for gender = Woman is: ', type_woman_max)
    print('The most popular type for gender = Non-Binary... is: ', type_nonb_max)
    print('\n')
    print('The least popular type for gender = Man is: ', type_man_min)
    print('The least popular type for gender = Woman is: ', type_woman_min)
    print('The least popular type for gender = Non-Binary... is: ', type_nonb_min)
    print('\n')
# =============================================================================
# e. Is there a relation between gender and salary? (consider only the genders 
# man/woman)


def contingency_table(values_1, values_2):
    d_s = {}
    for i, j in zip(values_1, values_2):
        if i not in d_s:
            d_s[i] = {}
            d_s[i][j] = d_s[i].get(j, 0) + 1
        return d_s

def gs_relation():
    lst_man = df[f_genderMan]['Gender'].tolist()
    ct_gendersalary = contingency_table(lst_man, )
    

# =============================================================================

W_D = 'C:/users/ivand/Desktop/Ene-Jun2021/Clases/MineriaDatos/Práctica/'
I_F = W_D + 'survey_results.csv'
df = pd.read_csv(I_F, encoding = 'utf-8')
f_genderMan = (df['Gender'].str.contains(r'^Man'))
f_genderWoman = (df['Gender'].str.contains(r'^Woman'))
f_genderNonB = (df['Gender'].str.contains(r'^Non-binary, genderqueer, or gender non-conforming')) 
lst_man = df[f_genderMan]['ConvertedComp'].tolist()
title_man = ['Salario por genero: Man']
lst_woman = df[f_genderWoman]['ConvertedComp'].tolist()
title_woman = ['Salario por genero: Woman']
lst_nonb = df[f_genderNonB]['ConvertedComp'].tolist()
title_nonb = ['Salario por genero: Non-Binary...']
summary(lst_man, title_man)
summary(lst_woman, title_woman)
summary(lst_nonb, title_nonb)
# =============================================================================

gender_answers()
lower_salaries()
lang_pop()
devtype_pop()
gs_relation()
# =============================================================================