# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 00:13:33 2021

@author: ivand
"""

# Compute the five-number summary, the mean, and the standard deviation for the
# annual salary and draw the boxplots for the 4 most common ethnicities. You 
# first nned to find the 4 ethnicities with more answers and compute the statistics
# for each one.
# Perform the computations with the original data and with the trimmed data at
# 10% for the salary (you must cut the 10% lowest salaries and 10% highest salaries).
# Make comparisons between the results with the original data and the ones with
# the trimmed data.
# Besides, try to give and explanation for the following questions, using the
# trimmed data at 10% for the salary, only considering the 4 most common ethnicities,
# and by computing all the additional and necessary statistics and drawing the
# necessary graphs/plots.

import pandas as pd
import matplotlib.pyplot as plt

def trim_data(values, a):
    n = len(values)
    k = int(a/100*n)
    print(f'Valores a recortar: {k}')
    return values[k:n-k]

def freq(lst):
    freq = {}
    for i in lst:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq

#-------------------------- Salaries per ethnicity ----------------------------
def summary():
    eth = df['Ethnicity'].tolist()
    eth_clean = []
    eth_list = []
    for i in range(len(eth)):
        eth_clean.append(eth[i].split(';'))
    for i in eth_clean:
        for j in i:
            eth_list.append(j)
    eth_freq = freq(eth_list)
    eth_freq = sorted(eth_freq.items(), key=lambda x:x[1], reverse=True)
    eth_freq = eth_freq[:4]
    eth_freq = [i[0] for i in eth_freq]
    print('\n')
    print('The 4 most common ethnicities are: ', eth_freq)
    eth_f1 = (df['Ethnicity'].str.contains(eth_freq[0]))
    salary_1 = df[eth_f1]['ConvertedComp']
    eth_f2 = (df['Ethnicity'].str.contains(eth_freq[1]))
    salary_2 = df[eth_f2]['ConvertedComp']
    eth_f3 = (df['Ethnicity'].str.contains(eth_freq[2]))
    salary_3 = df[eth_f3]['ConvertedComp']
    eth_f4 = (df['Ethnicity'].str.contains(eth_freq[3]))
    salary_4 = df[eth_f4]['ConvertedComp']
    plt.boxplot(salary_1)
    plt.title(eth_freq[0])
    plt.figure()
    plt.boxplot(salary_2)
    plt.title(eth_freq[1])
    plt.figure()
    plt.boxplot(salary_3)
    plt.title(eth_freq[2])
    plt.figure()
    plt.boxplot(salary_4)
    plt.title(eth_freq[3])
    print('------------ Summary for White or of European descent ----------------')
    print(salary_1.describe())
    print('\n')
    print('-------------- Summary for Hispanic or Latino/Latina -----------------')
    print(salary_2.describe())
    print('\n')
    print('------------------- Summary for South Asian --------------------------')
    print(salary_3.describe())
    print('\n')
    print('-------------------- Summary for East Asian --------------------------')
    print(salary_4.describe())
    print('\n')
    
    #--------------------------- Data trimmed 10% ---------------------------------
    salary1_t = trim_data(salary_1, 10)
    salary2_t = trim_data(salary_2, 10)
    salary3_t = trim_data(salary_3, 10)
    salary4_t = trim_data(salary_4, 10)
    plt.figure()
    plt.boxplot(salary1_t)
    plt.title('White or of European descent (trimmed 10%)')
    plt.figure()
    plt.boxplot(salary2_t)
    plt.title('Hispanic or Latino/Latina (trimmed 10%)')
    plt.figure()
    plt.boxplot(salary3_t)
    plt.title('South Asian (trimmed 10%)')
    plt.figure()
    plt.boxplot(salary4_t)
    plt.title('East Asian (trimmed 10%)')
    print('------- Summary for White or of European descent (trimmed 10%) -------')
    print(salary1_t.describe())
    print('\n')
    print('-------- Summary for Hispanic or Latino/Latina (trimmed 10%) ---------')
    print(salary2_t.describe())
    print('\n')
    print('-------------- Summary for South Asian (trimmed 10%) -----------------')
    print(salary3_t.describe())
    print('\n')
    print('--------------- Summary for East Asian (trimmed 10%) -----------------')
    print(salary4_t.describe())
    print('\n')
    return (eth_f1, eth_f2, eth_f3, eth_f4, 
            salary1_t, salary2_t, salary3_t, salary4_t,
            eth_freq)

#-------------------------- Answers per ethnicity -----------------------------
# a. Which ethnicity has more answers?

def answers(eth_freq, salary_1, salary_2, salary_3, salary_4):
    plt.figure()
    pie_labels = eth_freq
    e_list = [len(salary_1), len(salary_2), len(salary_3), len(salary_4)]
    plt.pie(e_list, explode=(0.1, 0, 0, 0), labels=pie_labels)
    plt.title('Respuestas para Ethnicity')
    print('Answers for White or of European descent: ', len(salary_1))
    print('Answers for Hispanic or Latino/Latina: ', len(salary_2))
    print('Answers for South Asian: ', len(salary_3))
    print('Answers for East Asian: ', len(salary_4))
    print('\n')

#--------------------------- Higher/Lower salaries ----------------------------
# b. Which ethnicity tends to have higher salaries, and which one tends to have
# lower salaries?

def higher_lower(salary_1, salary_2, salary_3, salary_4):
    avg_d = {'White or of European descent':salary_1.mean(),
              'Hispanic or Latino/Latina':salary_2.mean(), 
              'South Asian':salary_3.mean(), 'East Asian': salary_4.mean()}
    plt.figure()
    plt.bar(avg_d.keys(), avg_d.values())
    plt.title('Average salary by etnicity')
    avg_max_v = max(avg_d.values())
    for k, v in avg_d.items():
        if v == avg_max_v:
            avg_max_l = k
    avg_min_v = min(avg_d.values())
    for k, v in avg_d.items():
        if v == avg_min_v:
            avg_min_l = k
    print(f'The ethnicity with higher salaries is {avg_max_l} with: {avg_max_v:.2f}')
    print(f'The ethnicity with lower salaries is {avg_min_l} with: {avg_min_v:.2f}')
    print('\n')

# -------------------- Programming langauge per ethnicity ---------------------
# c. What are the most popular and less popular programming language per ethnicity?

def language(eth_f1, eth_f2, eth_f3, eth_f4):
    lst_eth1 = df[eth_f1]['LanguageWorkedWith'].tolist()
    lst_eth2 = df[eth_f2]['LanguageWorkedWith'].tolist()
    lst_eth3 = df[eth_f3]['LanguageWorkedWith'].tolist()
    lst_eth4 = df[eth_f4]['LanguageWorkedWith'].tolist()
    temp_eth1 = []
    temp_eth2 = []
    temp_eth3 = []
    temp_eth4 = []
    lst_lan_eth1 = []
    lst_lan_eth2 = []
    lst_lan_eth3 = []
    lst_lan_eth4 = []
    for i in range(len(lst_eth1)):
        temp_eth1.append(lst_eth1[i].split(';'))
    for i in range(len(lst_eth2)):
        temp_eth2.append(lst_eth2[i].split(';'))
    for i in range(len(lst_eth3)):
        temp_eth3.append(lst_eth3[i].split(';'))
    for i in range(len(lst_eth4)):
        temp_eth4.append(lst_eth4[i].split(';'))
    for i in temp_eth1:
        for j in i:
            lst_lan_eth1.append(j)
    for i in temp_eth2:
        for j in i:
            lst_lan_eth2.append(j)
    for i in temp_eth3:
        for j in i:
            lst_lan_eth3.append(j)
    for i in temp_eth4:
        for j in i:
            lst_lan_eth4.append(j)
    freq_lan_eth1 = freq(lst_lan_eth1)
    freq_lan_eth2 = freq(lst_lan_eth2)
    freq_lan_eth3 = freq(lst_lan_eth3)
    freq_lan_eth4 = freq(lst_lan_eth4)
    lan_eth1_max = max(freq_lan_eth1, key=freq_lan_eth1.get)
    lan_eth2_max = max(freq_lan_eth2, key=freq_lan_eth2.get)
    lan_eth3_max = max(freq_lan_eth3, key=freq_lan_eth3.get)
    lan_eth4_max = max(freq_lan_eth4, key=freq_lan_eth4.get)
    lan_eth1_min = min(freq_lan_eth1, key=freq_lan_eth1.get)
    lan_eth2_min = min(freq_lan_eth2, key=freq_lan_eth2.get)
    lan_eth3_min = min(freq_lan_eth3, key=freq_lan_eth3.get)
    lan_eth4_min = min(freq_lan_eth4, key=freq_lan_eth4.get)
    plt.figure()
    plt.pie(freq_lan_eth1.values(), labels=freq_lan_eth1.keys())
    plt.title('Languages for White or of European descent')
    plt.figure()
    plt.pie(freq_lan_eth2.values(), labels=freq_lan_eth2.keys())
    plt.title('Lnguages for Hispanic or Latino/Latina')
    plt.figure()
    plt.pie(freq_lan_eth3.values(), labels=freq_lan_eth3.keys())
    plt.title('Languages for South Asian')
    plt.figure()
    plt.pie(freq_lan_eth4.values(), labels=freq_lan_eth4.keys())
    plt.title('Languages for East Asian')
    print('The most popular language for White or of European descent is: ', lan_eth1_max)
    print('The most popular language for Hispanic or Latino/Latina is: ', lan_eth2_max)
    print('The most popular language for South Asian is: ', lan_eth3_max)
    print('The most popular language for East Asian is: ', lan_eth4_max)
    print('\n')
    print('The least popular language for White or of European descent is: ', lan_eth1_min)
    print('The least popular language for Hispanic or Latino/Latina is: ', lan_eth2_min)
    print('The least popular language for South Asian is: ', lan_eth3_min)
    print('The least popular language for East Asian is: ', lan_eth4_min)
    print('\n')

# -------------------- Developer type per ethnicity ---------------------
# d. What are the most popular and less popular developer type per ethnicity?

def dev_type(eth_f1, eth_f2, eth_f3, eth_f4):
    lst_eth1 = df[eth_f1]['DevType'].tolist()
    lst_eth2 = df[eth_f2]['DevType'].tolist()
    lst_eth3 = df[eth_f3]['DevType'].tolist()
    lst_eth4 = df[eth_f4]['DevType'].tolist()
    temp_eth1 = []
    temp_eth2 = []
    temp_eth3 = []
    temp_eth4 = []
    lst_type_eth1 = []
    lst_type_eth2 = []
    lst_type_eth3 = []
    lst_type_eth4 = []
    for i in range(len(lst_eth1)):
        temp_eth1.append(lst_eth1[i].split(';'))
    for i in range(len(lst_eth2)):
        temp_eth2.append(lst_eth2[i].split(';'))
    for i in range(len(lst_eth3)):
        temp_eth3.append(lst_eth3[i].split(';'))
    for i in range(len(lst_eth4)):
        temp_eth4.append(lst_eth4[i].split(';'))
    for i in temp_eth1:
        for j in i:
            lst_type_eth1.append(j)
    for i in temp_eth2:
        for j in i:
            lst_type_eth2.append(j)
    for i in temp_eth3:
        for j in i:
            lst_type_eth3.append(j)
    for i in temp_eth4:
        for j in i:
            lst_type_eth4.append(j)
    freq_type_eth1 = freq(lst_type_eth1)
    freq_type_eth2 = freq(lst_type_eth2)
    freq_type_eth3 = freq(lst_type_eth3)
    freq_type_eth4 = freq(lst_type_eth4)
    type_eth1_max = max(freq_type_eth1, key=freq_type_eth1.get)
    type_eth2_max = max(freq_type_eth2, key=freq_type_eth2.get)
    type_eth3_max = max(freq_type_eth3, key=freq_type_eth3.get)
    type_eth4_max = max(freq_type_eth4, key=freq_type_eth4.get)
    type_eth1_min = min(freq_type_eth1, key=freq_type_eth1.get)
    type_eth2_min = min(freq_type_eth2, key=freq_type_eth2.get)
    type_eth3_min = min(freq_type_eth3, key=freq_type_eth3.get)
    type_eth4_min = min(freq_type_eth4, key=freq_type_eth4.get)
    plt.figure()
    plt.pie(freq_type_eth1.values(), labels=freq_type_eth1.keys())
    plt.title('Developer types for White or of European descent')
    plt.figure()
    plt.pie(freq_type_eth2.values(), labels=freq_type_eth2.keys())
    plt.title('Developer types for Hispanic or Latino/Latina')
    plt.figure()
    plt.pie(freq_type_eth3.values(), labels=freq_type_eth3.keys())
    plt.title('Developer types for South Asian')
    plt.figure()
    plt.pie(freq_type_eth4.values(), labels=freq_type_eth4.keys())
    plt.title('Developer types for East Asian')
    print('The most popular type for White or of European descent is: ', type_eth1_max)
    print('The most popular type for Hispanic or Latino/Latina is: ', type_eth2_max)
    print('The most popular type for South Asian is: ', type_eth3_max)
    print('The most popular type for East Asian is: ', type_eth4_max)
    print('\n')
    print('The least popular type for White or of European descent is: ', type_eth1_min)
    print('The least popular type for Hispanic or Latino/Latina is: ', type_eth2_min)
    print('The least popular type for South Asian is: ', type_eth3_min)
    print('The least popular type for East Asian is: ', type_eth4_min)
    print('\n')

w_d = 'C:/Users/ivand/Desktop/Universidad/Ago-Dic2021/MineriaDatos/Practica/'
i_f = w_d + 'survey_results.csv'

df = pd.read_csv(i_f)

f1, f2, f3, f4, s1, s2, s3, s4, e_freq = summary()
answers(e_freq, s1, s2, s3, s4)
higher_lower(s1, s2, s3 ,s4)
language(f1, f2, f3, f4)
dev_type(f1, f2, f3, f4)

