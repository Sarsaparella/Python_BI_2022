import numpy as np
import pandas as pd
import re
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import matplotlib.ticker as tck
from matplotlib import rc,rcParams


# Задание 1

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

read_bed6('alignment.bed')

read_gff('rrna_annotation.gff')


gff_table = read_gff('rrna_annotation.gff')
gff_table['RNA type'] = gff_table['RNA type'].str.extract(r'([0-9]+S )')
gff_table


# Сделайте таблицу, где для каждой хромосомы (на самом деле это не хромосомы, а 
# референсные геномы) показано количество рРНК каждого типа

gff_table = read_gff('rrna_annotation.gff')
counted_RNA = gff_table.groupby(['chromosome','RNA type']).agg({'RNA type': 'count'})
counted_RNA


# Постройте barplot, отображающий эти данные (картинка rRNA_barplot)

counted_RNAs = gff_table.groupby(['RNA type','chromosome']).agg({'chromosome': 'count'})

counted_RNAs.unstack(0).plot.bar(figsize=(20,10))

# Выведите таблицу, содержащую исходные записи об рРНК полностью вошедших в сборку 

gff_table = read_gff('rrna_annotation.gff')
bed_table = read_bed6('alignment.bed')

merged = pd.merge(gff_table, bed_table , how='outer', on=['chromosome'])

merged_new = merged[(merged['end_x'] <= merged['end_y']) & (merged['start_x'] >= merged['start_y'])]
merged_new





# Задание 2 Кастомизация графиков

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


# creating sorted datasets

up_reg = diff_data[diff_data['color'] == 'Significantly upregulated'].sort_values(by='logFC', ascending = False)
up_reg


down_reg = diff_data[diff_data['color'] == 'Significantly downregulated'].sort_values(by='logFC')
down_reg


# Задание 1

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

# Plot itlef

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