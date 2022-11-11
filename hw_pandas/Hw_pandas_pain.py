#!/usr/bin/env python
# coding: utf-8

# **Задание 1. Работа с реальными данными (20 баллов)**
# 
# В биоинформатике часто приходится работать с табличными данными (gff, bed, vcf и т.д.), однако в терминале делать различные продвинутые операции довольно трудно, тут нам и приходит на помощь пандас.
# 
# В прикреплённых файлах лежит аннотация рибосомальной РНК некоторого метагеномного датасета в формате GFF (**rrna_annotation.gff**), а также файл с выравниванием метагеномной сборки на этот же датасет в формате BED 6 (**alignment.bed**).
# 
# - Напишите функции **read_gff** и **read_bed6** для чтения соответствующих форматов. Они должны возвращать датафреймы как в примере (картинка **Example1**), но имена колонок можно сделать любыми.
# - Колонка с атрибутами несёт слишком много избыточной информации и ей не удобно пользоваться, оставьте в ней только данные о типе рРНК одной короткой строкой (16S, 23S, 5S).
# - Сделайте таблицу, где для каждой хромосомы (на самом деле это не хромосомы, а референсные геномы) показано количество рРНК каждого типа. Постройте barplot, отображающий эти данные (картинка **rRNA_barplot**)
# - Далее самое интересное. Мы хотим узнать сколько рРНК в процессе сборки успешно собралось. Для этого можно воспользоваться программой **bedtools intersect** и пересечь эти два файла. В результате сохранятся только записи об рРНК, интервал которой перекрывался с интервалом контига в выравнивании, это означает, что это ген есть в сборке. Но забудьте про bedtools! У нас тут вообще-то пандас! Поэтому давайте получим такой же результат в нём. Выведите таблицу, содержащую исходные записи об рРНК **полностью** вошедших в сборку (не фрагментом), а также запись о контиге в который эта РНК попала. Итоговая таблица должна выглядеть примерно так (картинка **Example2**). Обратите внимание, что в один контиг может попасть несколько рРНК.

# In[1]:


import numpy as np
import pandas as pd
import re
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import matplotlib.ticker as tck
from matplotlib import rc,rcParams


# In[6]:


def read_gff(file):
    gff_table = pd.read_csv(file, sep='\t', header = 0, names= ['chromosome', 
                                                           'source', 'type',
                                                           'start', 'end',
                                                           'score', 'strand',
                                                           'phase', 'RNA type'])
    return gff_table

def read_bed6(file):
    bed_table = pd.read_csv(file, sep='\t', names = ['chromosome','start',
                                                     'end','name','score',
                                                     'strand'])
    return bed_table


# In[8]:


read_bed6('alignment.bed')


# In[9]:


read_gff('rrna_annotation.gff')


# In[7]:


gff_table = read_gff('rrna_annotation.gff')
gff_table['RNA type'] = gff_table['RNA type'].str.extract(r'([0-9]+S )')
gff_table


# Сделайте таблицу, где для каждой хромосомы (на самом деле это не хромосомы, а референсные геномы) показано количество рРНК каждого типа.

# In[11]:


gff_table = read_gff('rrna_annotation.gff')
counted_RNA = gff_table.groupby(['chromosome','RNA type']).agg({'RNA type': 'count'})
counted_RNA


# Постройте barplot, отображающий эти данные (картинка rRNA_barplot)

# In[10]:


counted_RNAs = gff_table.groupby(['RNA type','chromosome']).agg({'chromosome': 'count'})

counted_RNAs.unstack(0).plot.bar(figsize=(20,10))


# Выведите таблицу, содержащую исходные записи об рРНК полностью вошедших в сборку (не фрагментом), а также запись о контиге в который эта РНК попала. Итоговая таблица должна выглядеть примерно так (картинка Example2). Обратите внимание, что в один контиг может попасть несколько рРНК.

# In[55]:


gff_table = read_gff('rrna_annotation.gff')
bed_table = read_bed6('alignment.bed')

merged = pd.merge(gff_table, bed_table , how='outer', on=['chromosome'])

merged_new = merged[(merged['end_x'] <= merged['end_y']) & (merged['start_x'] >= merged['start_y'])]
merged_new


# **Задание 2. Кастомизация графиков (20 баллов)**
# 
# Для визуализации данных дифференциальной экспрессии генов, можно использовать специальный тип графика - **volcano plot.** По оси X на нём отложен **logFC (Logarithmic Fold Change) -** во сколько раз изменилась экспрессия гена в степенях двойки (logFC=-8 - экспрессия гена изменилась в 2^-8 раз). По оси Y откладывается уровень значимости данных изменений в виде **отрицательного десятичного логарифма p-value (с поправкой на множественное сравнение).** В данном задании вам нужно максимально точно воспроизвести график **volcano_plot.png** (прикреплён к заданию). Для этого используйте файл с данными **diffexpr_data.tsv.gz** (пандас умеет открывать **.gz** файлы, поэтому разжимать их не обязательно)**. Данные уже предобработаны, считать p-value и брать логарифмы уже не надо**, просто используйте колонки **logFC** и **log_pval**. Если необходимо, можете делать группировку данных или брать subsets, но в итоге на графике должны быть именно значения из этих колонок. Ниже приведён чеклист кастомизаций для удобства, чем больше вы сделаете, тем лучше.

# - Четыре сегмента на графике:
#     - [ ]  Цвета сегментов
#     - [ ]  Разделение сегментов пунктирными линиями
#         - [ ]  Серый цвет линий
#         - [ ]  Пунктирность линий
#         - [ ]  Толщина линий
#     - [ ]  Подпись "p_value = 0.05" над соответствующей линией
#     - [ ]  Размер точек
# - Оси и лейблы
#     - [ ]  xlabel, ylabel и title - жирным курсивом, размером +- как на картинке
#     - [ ]  Основание логарифма в нижнем регистре
#     - [ ]  Размер и толщина ticks на осях X и Y (minor ticks должны отображаться)
#     - [ ]  Симметричные лимиты для оси X, но чтобы все данные помещались. Условно, если минимальный **logFC = -1,** а максимальный **logFC = 10,** то значения по оси X должны отображаться от -11 до 11 (+-1 нужно для того, чтобы на график поместилась крайняя точка). Вычислите эти лимиты из данных, а не вбивайте готовые числа
#     - [ ]  Толщина осей
#     
# - Легенда
#     - [ ]  Размер и шрифт букв в легенде
#     - [ ]  Размер маркеров в легенде
#     - [ ]  Небольшая тень от легенды вправо вниз
# - Проаннотировать топ-2 генов, **значимо снизивших** экспрессию, и топ-2 генов, **значимо увеличивших** экспрессию
#     - [ ]  Стрелочки
#         - [ ]  Красные с чёрной гранью
#         - [ ]  Направление стрелок - произвольное
#     - [ ]  Текст у стрелочек
#         - [ ]  Жирный

# In[23]:


diff_data = pd.read_csv('diffexpr_data.tsv.gz', sep='\t')

def map_color(logFC, pval_corr):
    if logFC < 0:
        if pval_corr < 0.05:
            return 'Significantly downregulated'
        else:
            return 'Non-significantly downregulated'
    else:
        if pval_corr < 0.05:
            return 'Significantly upregulated'
        else:
            return 'Non-significantly upregulated'
    
diff_data['color'] = diff_data.apply(lambda x: map_color(x.logFC, x.pval_corr), axis = 1)
diff_data


# In[41]:


# creating sorted datasets

up_reg = diff_data[diff_data['color'] == 'Significantly upregulated'].sort_values(by='logFC', ascending = False)
up_reg


# In[42]:


down_reg = diff_data[diff_data['color'] == 'Significantly downregulated'].sort_values(by='logFC')
down_reg


# In[59]:


plt.figure(figsize = (20,10))

volc = sns.scatterplot(data = diff_data, x = 'logFC', y = 'log_pval', s = 28,
                       linewidth = 0,
                       hue = 'color',
                       hue_order = ['Significantly downregulated', 'Significantly upregulated', 'Non-significantly upregulated', 'Non-significantly downregulated'],
                       palette = ['#1B39B0', '#FF8C00', '#006400', '#FF4500'])

# Creating vertical and horizontal lines in the middle of a plot

volc.axhline(-np.log10(0.05), ls = '--', lw = 2, c = '#7A7A7A')
volc.axvline(0, ls = '--', lw = 2, c = '#7A7A7A')
volc.annotate('p value = 0.05', xy=(1000, 30), xycoords='figure points', color = '#7A7A7A', weight = 'semibold', size = 20)

# Setting font for labels of axis

font1 = {'family':'arial','color':'black','size':22, 'weight':'bold', 'style':'italic'}

plt.rcParams['mathtext.fontset'] = 'custom'
plt.rcParams['mathtext.bf'] = 'Arial:italic:bold'

# Names of plot and axis

plt.title('Volcano plot', fontdict = font1, size = 40)
plt.xlabel(r'$\mathbf{\bf{log_2(fold\ change)}}$', fontdict = font1)
plt.ylabel(r"$\mathbf{-log_{10}(p \ value \ corrected)}$", fontdict = font1,)

# Ticks stuff

plt.minorticks_on()

plt.xticks(size = 20, weight = 'bold')
plt.yticks(size = 20, weight = 'bold')
volc.tick_params(axis = 'both', which = 'minor', labelsize = 20, width = 2, size = 5)

# Making axis lines nice and fat

for axis in ['top','bottom','left','right']:
    volc.spines[axis].set_linewidth(3)
    
# Спасибо за все, легенда...

plt.legend(shadow = True, markerscale = 2, fontsize = 15)

# annotations

volc.annotate(up_reg.iloc[0][0],
            xy=(up_reg.iloc[0][1], up_reg.iloc[0][4]),
            xytext=(up_reg.iloc[0][1], up_reg.iloc[0][4] + 10),
            arrowprops=dict(arrowstyle='simple', facecolor='red'), size=20
             )
volc.annotate(up_reg.iloc[1][0],
            xy=(up_reg.iloc[1][1], up_reg.iloc[1][4]),
            xytext=(up_reg.iloc[1][1], up_reg.iloc[1][4] + 10),
            arrowprops=dict(arrowstyle='simple', facecolor='red'), size=20
            )

volc.annotate(down_reg.iloc[0][0],
            xy=(down_reg.iloc[0][1], down_reg.iloc[0][4]),
            xytext=(down_reg.iloc[0][1]-1, down_reg.iloc[0][4] + 10),
            arrowprops=dict(arrowstyle='simple', facecolor='red'), size=20
            )
volc.annotate(down_reg.iloc[1][0],
            xy=(down_reg.iloc[1][1], down_reg.iloc[1][4]),
            xytext=(down_reg.iloc[1][1]-1, down_reg.iloc[1][4] + 10),
            arrowprops=dict(arrowstyle='simple', facecolor='red'), size=20
            );

