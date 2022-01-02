# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 13:41:29 2021

@author: ivand
"""
# Compute the five-number summary, the mean, and the standard deviation for the
# annual salary and draw the boxplots for the 4 most common programming languages.
# You first nned to find the 4 programming languages with more answers and compute
# the statisticsfor each one.
# Perform the computations with the original data and with the trimmed data at
# 10% for the salary (you must cut the 10% lowest salaries and 10% highest salaries).
# Make comparisons between the results with the original data and the ones with
# the trimmed data.
# Besides, try to give and explanation for the following questions, using the
# trimmed data at 10% for the salary, only considering the 4 most common 
# programming languages, and by computing all the additional and necessary 
# statistics and drawing the necessary graphs/plots.

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

#-------------------------- Salaries per language ----------------------------
def summary():
    lan = df['LanguageWorkedWith'].tolist()
    lan_clean = []
    lan_list = []
    for i in range(len(lan)):
        lan_clean.append(lan[i].split(';'))
    for i in lan_clean:
        for j in i:
            lan_list.append(j)
    lan_freq = freq(lan_list)
    lan_freq = sorted(lan_freq.items(), key=lambda x:x[1], reverse=True)
    lan_freq = lan_freq[:4]
    lan_freq = [i[0] for i in lan_freq]
    print('\n')
    print('The 4 most common languages are: ', lan_freq)
    lan_f1 = (df['LanguageWorkedWith'].str.contains(lan_freq[0]))
    salary_1 = df[lan_f1]['ConvertedComp']
    lan_f2 = (df['LanguageWorkedWith'].str.contains(lan_freq[1]))
    salary_2 = df[lan_f2]['ConvertedComp']
    lan_f3 = (df['LanguageWorkedWith'].str.contains(lan_freq[2]))
    salary_3 = df[lan_f3]['ConvertedComp']
    lan_f4 = (df['LanguageWorkedWith'].str.contains(lan_freq[3]))
    salary_4 = df[lan_f4]['ConvertedComp']
    plt.boxplot(salary_1)
    plt.title(lan_freq[0])
    plt.figure()
    plt.boxplot(salary_2)
    plt.title(lan_freq[1])
    plt.figure()
    plt.boxplot(salary_3)
    plt.title(lan_freq[2])
    plt.figure()
    plt.boxplot(salary_4)
    plt.title(lan_freq[3])
    print('------------ Summary for JavaScript ----------------')
    print(salary_1.describe())
    print('\n')
    print('-------------- Summary for  HTML/CSS -----------------')
    print(salary_2.describe())
    print('\n')
    print('------------------- Summary for SQL --------------------------')
    print(salary_3.describe())
    print('\n')
    print('--------------- Summary for Bash/Shell/PowerShell --------------------')
    print(salary_4.describe())
    print('\n')
    
    #--------------------------- Data trimmed 10% ---------------------------------
    salary1_t = trim_data(salary_1, 10)
    salary2_t = trim_data(salary_2, 10)
    salary3_t = trim_data(salary_3, 10)
    salary4_t = trim_data(salary_4, 10)
    plt.figure()
    plt.boxplot(salary1_t)
    plt.title('JavaScript (trimmed 10%)')
    plt.figure()
    plt.boxplot(salary2_t)
    plt.title('HTML/CSS (trimmed 10%)')
    plt.figure()
    plt.boxplot(salary3_t)
    plt.title('SQL (trimmed 10%)')
    plt.figure()
    plt.boxplot(salary4_t)
    plt.title('Bash/Shell/PowerShell (trimmed 10%)')
    print('------- Summary for JavaScript (trimmed 10%) -------')
    print(salary1_t.describe())
    print('\n')
    print('-------- Summary for HTML/CSS (trimmed 10%) ---------')
    print(salary2_t.describe())
    print('\n')
    print('-------------- Summary for SQL (trimmed 10%) -----------------')
    print(salary3_t.describe())
    print('\n')
    print('---------- Summary for Bash/Shell/PowerShell (trimmed 10%) -----------')
    print(salary4_t.describe())
    print('\n')
    return (lan_f1, lan_f2, lan_f3, lan_f4, 
            salary1_t, salary2_t, salary3_t, salary4_t,
            lan_freq)

#-------------------------- Answers per language ------------------------------
# a. Which programming language has more answers?

def answers(lan_freq, salary_1, salary_2, salary_3, salary_4):
    plt.figure()
    pie_labels = lan_freq
    e_list = [len(salary_1), len(salary_2), len(salary_3), len(salary_4)]
    plt.pie(e_list, explode=(0.1, 0, 0, 0), labels=pie_labels)
    plt.title('Respuestas para LanguageWorkedWith')
    print('Answers for JavaScript: ', len(salary_1))
    print('Answers for HTML/CSS: ', len(salary_2))
    print('Answers for SQL: ', len(salary_3))
    print('Answers for Bash/Shell/PowerShell: ', len(salary_4))
    print('\n')

#--------------------------- Higher/Lower salaries ----------------------------
# b. Which programming language tends to have higher salaries, and which one
# tends to have lower salaries?

def higher_lower(salary_1, salary_2, salary_3, salary_4):
    avg_d = {'JavaScript':salary_1.mean(), 'HTML/CSS':salary_2.mean(), 
              'SQL':salary_3.mean(), 'Bash/Shell/PowerShell': salary_4.mean()}
    plt.figure()
    plt.bar(avg_d.keys(), avg_d.values())
    plt.title('Average salary by language')
    avg_max_v = max(avg_d.values())
    for k, v in avg_d.items():
        if v == avg_max_v:
            avg_max_l = k
    avg_min_v = min(avg_d.values())
    for k, v in avg_d.items():
        if v == avg_min_v:
            avg_min_l = k
    print(f'The language with higher salaries is {avg_max_l} with: {avg_max_v:.2f}')
    print(f'The language with lower salaries is {avg_min_l} with: {avg_min_v:.2f}')
    print('\n')

# -------------------- Developer type per language ---------------------
# c. What are the most popular and less popular developer type per programming
# language?

def dev_type(lan_f1, lan_f2, lan_f3, lan_f4):
    lst_lan1 = df[lan_f1]['DevType'].tolist()
    lst_lan2 = df[lan_f2]['DevType'].tolist()
    lst_lan3 = df[lan_f3]['DevType'].tolist()
    lst_lan4 = df[lan_f4]['DevType'].tolist()
    temp_lan1 = []
    temp_lan2 = []
    temp_lan3 = []
    temp_lan4 = []
    lst_type_lan1 = []
    lst_type_lan2 = []
    lst_type_lan3 = []
    lst_type_lan4 = []
    for i in range(len(lst_lan1)):
        temp_lan1.append(lst_lan1[i].split(';'))
    for i in range(len(lst_lan2)):
        temp_lan2.append(lst_lan2[i].split(';'))
    for i in range(len(lst_lan3)):
        temp_lan3.append(lst_lan3[i].split(';'))
    for i in range(len(lst_lan4)):
        temp_lan4.append(lst_lan4[i].split(';'))
    for i in temp_lan1:
        for j in i:
            lst_type_lan1.append(j)
    for i in temp_lan2:
        for j in i:
            lst_type_lan2.append(j)
    for i in temp_lan3:
        for j in i:
            lst_type_lan3.append(j)
    for i in temp_lan4:
        for j in i:
            lst_type_lan4.append(j)
    freq_type_lan1 = freq(lst_type_lan1)
    freq_type_lan2 = freq(lst_type_lan2)
    freq_type_lan3 = freq(lst_type_lan3)
    freq_type_lan4 = freq(lst_type_lan4)
    type_lan1_max = max(freq_type_lan1, key=freq_type_lan1.get)
    type_lan2_max = max(freq_type_lan2, key=freq_type_lan2.get)
    type_lan3_max = max(freq_type_lan3, key=freq_type_lan3.get)
    type_lan4_max = max(freq_type_lan4, key=freq_type_lan4.get)
    type_lan1_min = min(freq_type_lan1, key=freq_type_lan1.get)
    type_lan2_min = min(freq_type_lan2, key=freq_type_lan2.get)
    type_lan3_min = min(freq_type_lan3, key=freq_type_lan3.get)
    type_lan4_min = min(freq_type_lan4, key=freq_type_lan4.get)
    plt.figure()
    plt.pie(freq_type_lan1.values(), labels=freq_type_lan1.keys())
    plt.title('Developer types for JavaScript')
    plt.figure()
    plt.pie(freq_type_lan2.values(), labels=freq_type_lan2.keys())
    plt.title('Developer types for HTML/CSS')
    plt.figure()
    plt.pie(freq_type_lan3.values(), labels=freq_type_lan3.keys())
    plt.title('Developer types for SQL')
    plt.figure()
    plt.pie(freq_type_lan4.values(), labels=freq_type_lan4.keys())
    plt.title('Developer types for Bash/Shell/PowerShell')
    print('The most popular type for JavaScript is: ', type_lan1_max)
    print('The most popular type for HTML/CSS is: ', type_lan2_max)
    print('The most popular type for SQL is: ', type_lan3_max)
    print('The most popular type for Bash/Shell/PowerShell is: ', type_lan4_max)
    print('\n')
    print('The least popular type for JavaScript is: ', type_lan1_min)
    print('The least popular type for HTML/CSS is: ', type_lan2_min)
    print('The least popular type for SQL is: ', type_lan3_min)
    print('The least popular type for Bash/Shell/PowerShell is: ', type_lan4_min)
    print('\n')

w_d = 'C:/Users/ivand/Desktop/Universidad/Ago-Dic2021/MineriaDatos/Practica/'
i_f = w_d + 'survey_results.csv'

df = pd.read_csv(i_f)
f1, f2, f3, f4, s1, s2, s3, s4, c_freq = summary()
answers(c_freq, s1, s2, s3, s4)
higher_lower(s1, s2, s3, s4)
dev_type(f1, f2, f3, f4)



