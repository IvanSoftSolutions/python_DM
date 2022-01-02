# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 12:45:33 2021

@author: ivand
"""
# Compute the five-number summary, the mean, and the standard deviation for the
# annual salary and draw the boxplots for the 4 most common countries. You 
# first nned to find the 4 countries with more answers and compute the statistics
# for each one.
# Perform the computations with the original data and with the trimmed data at
# 10% for the salary (you must cut the 10% lowest salaries and 10% highest salaries).
# Make comparisons between the results with the original data and the ones with
# the trimmed data.
# Besides, try to give and explanation for the following questions, using the
# trimmed data at 10% for the salary, only considering the 4 most common countries,
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

#-------------------------- Salaries per country ----------------------------
def summary():
    ctry = df['Country'].tolist()
    ctry_clean = []
    ctry_list = []
    for i in range(len(ctry)):
        ctry_clean.append(ctry[i].split(';'))
    for i in ctry_clean:
        for j in i:
            ctry_list.append(j)
    ctry_freq = freq(ctry_list)
    ctry_freq = sorted(ctry_freq.items(), key=lambda x:x[1], reverse=True)
    ctry_freq = ctry_freq[:4]
    ctry_freq = [i[0] for i in ctry_freq]
    print('\n')
    print('The 4 most common countries are: ', ctry_freq)
    ctry_f1 = (df['Country'].str.contains(ctry_freq[0]))
    salary_1 = df[ctry_f1]['ConvertedComp']
    ctry_f2 = (df['Country'].str.contains(ctry_freq[1]))
    salary_2 = df[ctry_f2]['ConvertedComp']
    ctry_f3 = (df['Country'].str.contains(ctry_freq[2]))
    salary_3 = df[ctry_f3]['ConvertedComp']
    ctry_f4 = (df['Country'].str.contains(ctry_freq[3]))
    salary_4 = df[ctry_f4]['ConvertedComp']
    plt.boxplot(salary_1)
    plt.title(ctry_freq[0])
    plt.figure()
    plt.boxplot(salary_2)
    plt.title(ctry_freq[1])
    plt.figure()
    plt.boxplot(salary_3)
    plt.title(ctry_freq[2])
    plt.figure()
    plt.boxplot(salary_4)
    plt.title(ctry_freq[3])
    print('------------ Summary for United States ----------------')
    print(salary_1.describe())
    print('\n')
    print('-------------- Summary for United Kingdom -----------------')
    print(salary_2.describe())
    print('\n')
    print('------------------- Summary for Germany --------------------------')
    print(salary_3.describe())
    print('\n')
    print('-------------------- Summary for Canada --------------------------')
    print(salary_4.describe())
    print('\n')
    
    #--------------------------- Data trimmed 10% ---------------------------------
    salary1_t = trim_data(salary_1, 10)
    salary2_t = trim_data(salary_2, 10)
    salary3_t = trim_data(salary_3, 10)
    salary4_t = trim_data(salary_4, 10)
    plt.figure()
    plt.boxplot(salary1_t)
    plt.title('United States (trimmed 10%)')
    plt.figure()
    plt.boxplot(salary2_t)
    plt.title('United Kingdom (trimmed 10%)')
    plt.figure()
    plt.boxplot(salary3_t)
    plt.title('Germany (trimmed 10%)')
    plt.figure()
    plt.boxplot(salary4_t)
    plt.title('Canada (trimmed 10%)')
    print('------- Summary for United States (trimmed 10%) -------')
    print(salary1_t.describe())
    print('\n')
    print('-------- Summary for United Kingdom (trimmed 10%) ---------')
    print(salary2_t.describe())
    print('\n')
    print('-------------- Summary for Germany (trimmed 10%) -----------------')
    print(salary3_t.describe())
    print('\n')
    print('--------------- Summary for Canada (trimmed 10%) -----------------')
    print(salary4_t.describe())
    print('\n')
    return (ctry_f1, ctry_f2, ctry_f3, ctry_f4, 
            salary1_t, salary2_t, salary3_t, salary4_t,
            ctry_freq)
    
#-------------------------- Answers per country -------------------------------
# a. Which country has more answers?

def answers(ctry_freq, salary_1, salary_2, salary_3, salary_4):
    plt.figure()
    pie_labels = ctry_freq
    e_list = [len(salary_1), len(salary_2), len(salary_3), len(salary_4)]
    plt.pie(e_list, explode=(0.1, 0, 0, 0), labels=pie_labels)
    plt.title('Respuestas para Country')
    print('Answers for United States: ', len(salary_1))
    print('Answers for United Kingdom: ', len(salary_2))
    print('Answers for Germany: ', len(salary_3))
    print('Answers for Canada: ', len(salary_4))
    print('\n')
    
#--------------------------- Higher/Lower salaries ----------------------------
# b. Which country tends to have higher salaries, and which one tends to have 
# lower salaries?

def higher_lower(salary_1, salary_2, salary_3, salary_4):
    avg_d = {'United States':salary_1.mean(), 'United Kingdom':salary_2.mean(), 
              'Germany':salary_3.mean(), 'Canada': salary_4.mean()}
    plt.figure()
    plt.bar(avg_d.keys(), avg_d.values())
    plt.title('Average salary by country')
    avg_max_v = max(avg_d.values())
    for k, v in avg_d.items():
        if v == avg_max_v:
            avg_max_l = k
    avg_min_v = min(avg_d.values())
    for k, v in avg_d.items():
        if v == avg_min_v:
            avg_min_l = k
    print(f'The country with higher salaries is {avg_max_l} with: {avg_max_v:.2f}')
    print(f'The country with lower salaries is {avg_min_l} with: {avg_min_v:.2f}')
    print('\n')

# ---------------------- Programming langauge per country ---------------------
# c. What are the most popular and less popular programming language per country?

def language(ctry_f1, ctry_f2, ctry_f3, ctry_f4):
    lst_ctry1 = df[ctry_f1]['LanguageWorkedWith'].tolist()
    lst_ctry2 = df[ctry_f2]['LanguageWorkedWith'].tolist()
    lst_ctry3 = df[ctry_f3]['LanguageWorkedWith'].tolist()
    lst_ctry4 = df[ctry_f4]['LanguageWorkedWith'].tolist()
    temp_ctry1 = []
    temp_ctry2 = []
    temp_ctry3 = []
    temp_ctry4 = []
    lst_lan_ctry1 = []
    lst_lan_ctry2 = []
    lst_lan_ctry3 = []
    lst_lan_ctry4 = []
    for i in range(len(lst_ctry1)):
        temp_ctry1.append(lst_ctry1[i].split(';'))
    for i in range(len(lst_ctry2)):
        temp_ctry2.append(lst_ctry2[i].split(';'))
    for i in range(len(lst_ctry3)):
        temp_ctry3.append(lst_ctry3[i].split(';'))
    for i in range(len(lst_ctry4)):
        temp_ctry4.append(lst_ctry4[i].split(';'))
    for i in temp_ctry1:
        for j in i:
            lst_lan_ctry1.append(j)
    for i in temp_ctry2:
        for j in i:
            lst_lan_ctry2.append(j)
    for i in temp_ctry3:
        for j in i:
            lst_lan_ctry3.append(j)
    for i in temp_ctry4:
        for j in i:
            lst_lan_ctry4.append(j)
    freq_lan_ctry1 = freq(lst_lan_ctry1)
    freq_lan_ctry2 = freq(lst_lan_ctry2)
    freq_lan_ctry3 = freq(lst_lan_ctry3)
    freq_lan_ctry4 = freq(lst_lan_ctry4)
    lan_ctry1_max = max(freq_lan_ctry1, key=freq_lan_ctry1.get)
    lan_ctry2_max = max(freq_lan_ctry2, key=freq_lan_ctry2.get)
    lan_ctry3_max = max(freq_lan_ctry3, key=freq_lan_ctry3.get)
    lan_ctry4_max = max(freq_lan_ctry4, key=freq_lan_ctry4.get)
    lan_ctry1_min = min(freq_lan_ctry1, key=freq_lan_ctry1.get)
    lan_ctry2_min = min(freq_lan_ctry2, key=freq_lan_ctry2.get)
    lan_ctry3_min = min(freq_lan_ctry3, key=freq_lan_ctry3.get)
    lan_ctry4_min = min(freq_lan_ctry4, key=freq_lan_ctry4.get)
    plt.figure()
    plt.pie(freq_lan_ctry1.values(), labels=freq_lan_ctry1.keys())
    plt.title('Languages for United States')
    plt.figure()
    plt.pie(freq_lan_ctry2.values(), labels=freq_lan_ctry2.keys())
    plt.title('Lnguages for United Kingdom')
    plt.figure()
    plt.pie(freq_lan_ctry3.values(), labels=freq_lan_ctry3.keys())
    plt.title('Languages for Germany')
    plt.figure()
    plt.pie(freq_lan_ctry4.values(), labels=freq_lan_ctry4.keys())
    plt.title('Languages for Canada')
    print('The most popular language for United States is: ', lan_ctry1_max)
    print('The most popular language for United Kingdom is: ', lan_ctry2_max)
    print('The most popular language for Germany is: ', lan_ctry3_max)
    print('The most popular language for Canada is: ', lan_ctry4_max)
    print('\n')
    print('The least popular language for United States is: ', lan_ctry1_min)
    print('The least popular language for United Kingdom is: ', lan_ctry2_min)
    print('The least popular language for Germany is: ', lan_ctry3_min)
    print('The least popular language for Canada is: ', lan_ctry4_min)
    print('\n')

# -------------------- Developer type per country ---------------------
# d. What are the most popular and less popular developer type per country?

def dev_type(ctry_f1, ctry_f2, ctry_f3, ctry_f4):
    lst_ctry1 = df[ctry_f1]['DevType'].tolist()
    lst_ctry2 = df[ctry_f2]['DevType'].tolist()
    lst_ctry3 = df[ctry_f3]['DevType'].tolist()
    lst_ctry4 = df[ctry_f4]['DevType'].tolist()
    temp_ctry1 = []
    temp_ctry2 = []
    temp_ctry3 = []
    temp_ctry4 = []
    lst_type_ctry1 = []
    lst_type_ctry2 = []
    lst_type_ctry3 = []
    lst_type_ctry4 = []
    for i in range(len(lst_ctry1)):
        temp_ctry1.append(lst_ctry1[i].split(';'))
    for i in range(len(lst_ctry2)):
        temp_ctry2.append(lst_ctry2[i].split(';'))
    for i in range(len(lst_ctry3)):
        temp_ctry3.append(lst_ctry3[i].split(';'))
    for i in range(len(lst_ctry4)):
        temp_ctry4.append(lst_ctry4[i].split(';'))
    for i in temp_ctry1:
        for j in i:
            lst_type_ctry1.append(j)
    for i in temp_ctry2:
        for j in i:
            lst_type_ctry2.append(j)
    for i in temp_ctry3:
        for j in i:
            lst_type_ctry3.append(j)
    for i in temp_ctry4:
        for j in i:
            lst_type_ctry4.append(j)
    freq_type_ctry1 = freq(lst_type_ctry1)
    freq_type_ctry2 = freq(lst_type_ctry2)
    freq_type_ctry3 = freq(lst_type_ctry3)
    freq_type_ctry4 = freq(lst_type_ctry4)
    type_ctry1_max = max(freq_type_ctry1, key=freq_type_ctry1.get)
    type_ctry2_max = max(freq_type_ctry2, key=freq_type_ctry2.get)
    type_ctry3_max = max(freq_type_ctry3, key=freq_type_ctry3.get)
    type_ctry4_max = max(freq_type_ctry4, key=freq_type_ctry4.get)
    type_ctry1_min = min(freq_type_ctry1, key=freq_type_ctry1.get)
    type_ctry2_min = min(freq_type_ctry2, key=freq_type_ctry2.get)
    type_ctry3_min = min(freq_type_ctry3, key=freq_type_ctry3.get)
    type_ctry4_min = min(freq_type_ctry4, key=freq_type_ctry4.get)
    plt.figure()
    plt.pie(freq_type_ctry1.values(), labels=freq_type_ctry1.keys())
    plt.title('Developer types for United Sates')
    plt.figure()
    plt.pie(freq_type_ctry2.values(), labels=freq_type_ctry2.keys())
    plt.title('Developer types for United Kingdom')
    plt.figure()
    plt.pie(freq_type_ctry3.values(), labels=freq_type_ctry3.keys())
    plt.title('Developer types for Germany')
    plt.figure()
    plt.pie(freq_type_ctry4.values(), labels=freq_type_ctry4.keys())
    plt.title('Developer types for Canada')
    print('The most popular type for United Sates is: ', type_ctry1_max)
    print('The most popular type for United Kingdom is: ', type_ctry2_max)
    print('The most popular type for Germany is: ', type_ctry3_max)
    print('The most popular type for Canada is: ', type_ctry4_max)
    print('\n')
    print('The least popular type for United Sates is: ', type_ctry1_min)
    print('The least popular type for United Kingdom is: ', type_ctry2_min)
    print('The least popular type for Germany is: ', type_ctry3_min)
    print('The least popular type for Canada is: ', type_ctry4_min)
    print('\n')

w_d = 'C:/Users/ivand/Desktop/Universidad/Ago-Dic2021/MineriaDatos/Practica/'
i_f = w_d + 'survey_results.csv'

df = pd.read_csv(i_f)

f1, f2, f3, f4, s1, s2, s3, s4, c_freq = summary()
answers(c_freq, s1, s2, s3, s4)
higher_lower(s1, s2, s3, s4)
language(f1, f2, f3, f4)
dev_type(f1, f2, f3, f4)
