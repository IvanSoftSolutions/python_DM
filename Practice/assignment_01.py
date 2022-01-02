# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 13:47:45 2021

@author: ivand
"""

# Compute the five-number summary, the mean, and the standard deviation for the
# annual salary per gender (the data considers three genders, you must compute 
# the statistics for each one) and draw the boxplot. Perform the computations with
# the original data and with the trimmed data at 10% for the salary (you must cut
# the 10% lowest salaries and 10% highest salaries). Make comparisons between the
# results with the original data and the ones with the trimmed data.

# Besides, try to give and explanation for the following questions by using the
# trimmed data at 10% for the salary and by computing all the additional and
# necessary statistics and drawing the necessary graphs/plots.

import pandas as pd
import matplotlib.pyplot as plt
import math as mt

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

def var_std(values):
    n = len(values)
    md = sum(values)/n
    num = [(x - md)**2 for x in values]
    num = sum(num)
    var = num/(n-1)
    std = mt.sqrt(var)
    return std 
   
def point_biseral(values_1, values_2, lab):
    n = len(values_1)
    n0 = n1 = m0 = m1 = 0        
    for l, v in zip(values_1, values_2):
        if l == lab[0]:
            n0 += 1
            m0 += v
        else:
            n1 += 1
            m1 += v
    sy = var_std(values_2)
    m0 /= n0
    m1 /= n1
    t1 = (m0 - m1)/sy
    t2 = mt.sqrt((n0/n)*(n1/n))
    rpd = t1*t2
    return rpd

def relations(column):
    f_man = df['Gender'] == 'Man'
    f_woman = df['Gender'] == 'Woman'
    man = df[f_man]['Gender'].tolist()
    woman = df[f_woman]['Gender'].tolist()
    g_list = man + woman
    values = df[column].tolist()
    rpd = point_biseral(g_list, values, ['Man', 'Woman'])
    return rpd

#-------------------------- Salaries per gender ------------------------------
def summary(man_salary, woman_salary, nonb_salary):
    plt.boxplot(man_salary)
    plt.title('Man')
    plt.figure()
    plt.boxplot(woman_salary)
    plt.title('Woman')
    plt.figure()
    plt.boxplot(nonb_salary)
    plt.title('Non-binary...')
    print('----------------------- Summary for Man ------------------------------')
    print(man_salary.describe())
    print('\n')
    print('---------------------- Summary for Woman -----------------------------')
    print(woman_salary.describe())
    print('\n')
    print('------------------ Summary for Non-binary... -------------------------')
    print(nonb_salary.describe())
    print('\n')

    #--------------------------- Data trimmed 10% ---------------------------------
    man_salary_t = trim_data(man_salary, 10)
    woman_salary_t = trim_data(woman_salary, 10)
    nonb_salary_t = trim_data(nonb_salary, 10)
    plt.figure()
    plt.boxplot(man_salary_t)
    plt.title('Man (trimmed 10%)')
    plt.figure()
    plt.boxplot(woman_salary_t)
    plt.title('Woman (trimmed 10%)')
    plt.figure()
    plt.boxplot(nonb_salary_t)
    plt.title('Non-binary... (trimmed 10%)')
    print('----------------- Summary for Man (trimmed 10%) ----------------------')
    print(man_salary_t.describe())
    print('\n')
    print('---------------- Summary for Woman (trimmed 10%) ---------------------')
    print(woman_salary_t.describe())
    print('\n')
    print('------------- Summary for Non-binary... (trimmed 10%) ----------------')
    print(nonb_salary_t.describe())
    print('\n')
    return man_salary_t, woman_salary_t, nonb_salary_t
    
#-------------------------- Answers per gender -------------------------------
# a. Which gender has more answers?

def answers(man_salary, woman_salary, nonb_salary):
    pie_labels = 'Man', 'Woman', 'Non-binary, genderqueer, or gender non-conforming'
    g_list = [len(man_salary), len(woman_salary), len(nonb_salary)]
    plt.figure()
    plt.pie(g_list, explode=(0.1, 0, 0), labels=pie_labels)
    plt.title('Respuestas para Gender')
    print('Answers for Man: ', len(man_salary))
    print('Answers for Woman: ', len(woman_salary))
    print('Answers for Non-binary... : ', len(nonb_salary))
    print('\n')

#--------------------------- Higher/Lower salaries ----------------------------
# b. Which gender tends to have higher salaries, and which one tends to have lower
# salaries?

def higher_lower(man_salary_t, woman_salary_t, nonb_salary_t):   
    m_man = man_salary_t.mean()
    m_woman = woman_salary_t.mean()
    m_nonb = nonb_salary_t.mean()
    avg_d = {'Man':m_man, 'Woman':m_woman, 'Non-binary...':m_nonb}
    plt.figure()
    plt.bar(avg_d.keys(), avg_d.values())
    plt.title('Average salary by gender')
    avg_max_v = max(avg_d.values())
    for k, v in avg_d.items():
        if v == avg_max_v:
            avg_max_l = k
    avg_min_v = min(avg_d.values())
    for k, v in avg_d.items():
        if v == avg_min_v:
            avg_min_l = k
    print(f'The gender with higher salaries is {avg_max_l} with: {avg_max_v:.2f}')
    print(f'The gender with lower salaries is {avg_min_l} with: {avg_min_v:.2f}')
    print('\n')

# ---------------------- Programming langauge per gender ----------------------
# c. What are the most popular and less popular programming language per gender?

def language():
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
    plt.figure()
    plt.pie(freq_lan_man.values(), labels=freq_lan_man.keys())
    plt.title('Languages for Man')
    plt.figure()
    plt.pie(freq_lan_woman.values(), labels=freq_lan_woman.keys())
    plt.title('Lnguages for Woman')
    plt.figure()
    plt.pie(freq_lan_nonb.values(), labels=freq_lan_nonb.keys())
    plt.title('Languages for Non-Binary...')
    print('The most popular language for Man is: ', lan_man_max)
    print('The most popular language for Woman is: ', lan_woman_max)
    print('The most popular language for Non-Binary... is: ', lan_nonb_max)
    print('\n')
    print('The least popular language for Man is: ', lan_man_min)
    print('The least popular language for Woman is: ', lan_woman_min)
    print('The least popular language for Non-Binary... is: ', lan_nonb_min)  
    print('\n')

#------------------------- Developer type per gender --------------------------
# d. What are the most popular and less popular developer type per gender?

def dev_type():
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
    plt.figure()
    plt.pie(freq_type_man.values(), labels=freq_type_man.keys())
    plt.title('Developer type for Man')
    plt.figure()
    plt.pie(freq_type_woman.values(), labels=freq_type_woman.keys())
    plt.title('Developer type for Woman')
    plt.figure()
    plt.pie(freq_type_nonb.values(), labels=freq_type_nonb.keys())
    plt.title('Developer type for Non-Binary...')
    print('The most popular type for Man is: ', type_man_max)
    print('The most popular type for Woman is: ', type_woman_max)
    print('The most popular type for Non-Binary... is: ', type_nonb_max)
    print('\n')
    print('The least popular type for Man is: ', type_man_min)
    print('The least popular type for Woman is: ', type_woman_min)
    print('The least popular type for Non-Binary... is: ', type_nonb_min)
    print('\n')

#------------------------- Relation Gender/[Variable] ------------------------
# e. Is there a relation between gender and salary? (Consider only the genders
# man/woman)
# f. Is there a relation between gender and age? (Consider only the genders 
# man/woman)
# g. Is there a relation between gender and years of experience? (Consider only
# the genders man/woman)

def r_gen(column1):
    r = relations(column1)
    print(f'The relation between gender and {column1} is: {r}')

w_d = 'C:/Users/ivand/Desktop/Universidad/Ago-Dic2021/MineriaDatos/Practica/'
i_f = w_d + 'survey_results.csv'

df = pd.read_csv(i_f)

f_genderMan = (df['Gender'].str.contains(r'Man'))
man_salary = df[f_genderMan]['ConvertedComp']
f_genderWoman = (df['Gender'].str.contains(r'Woman'))
woman_salary = df[f_genderWoman]['ConvertedComp']
f_genderNonB = (df['Gender'].str.contains(r'Non-binary, genderqueer, or gender non-conforming'))
nonb_salary = df[f_genderNonB]['ConvertedComp']

m_t, w_t, n_t = summary(man_salary, woman_salary, nonb_salary)
answers(m_t, w_t, n_t)
higher_lower(m_t, w_t, n_t)
language()
dev_type()
r_gen('ConvertedComp')
r_gen('Age')
r_gen('YearsCode')