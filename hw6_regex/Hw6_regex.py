import re
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Задание 1

!wget https://raw.githubusercontent.com/Serfentum/bf_course/master/15.re/references

with open('references') as reference:
    with open('links_from_reference.txt', 'w') as links:
        for line in reference.readlines():
            match = re.findall(r'ftp\.[./\w#]*', line)
            for line in match:
                print(line, file = links, sep = '\n')


# Задание 2

!wget https://raw.githubusercontent.com/Serfentum/bf_course/master/15.re/2430AD

with open('2430AD') as tale:
    for line in tale.readlines():
        match = re.findall(r'\d.\d?\d?', line)
        for number in match:
            print(number)

# Задание 3

words = []
with open('2430AD') as tale:
    for line in tale.readlines():
        match = re.findall(r"[A-Za-z]*[aA][A-Za-z]*", line)
        for line in match:
            words.append(line)
print(words)
# len(words)


# Задание 4

exclamation = []
with open('2430AD') as tale:
    for line in tale.readlines():
        match = re.findall(r"[A-Za-z ]*!", line)
        for line in match:
            exclamation.append(line)
            
print(exclamation)


# Задание 5

unique_lengths = {}
unique_words_list = []
all_words = []
length_n_prop = {}

# Creating list will all words

with open('2430AD') as tale:
    for line in tale.readlines():
        match = re.findall(r"[\w'-]*", line)
        for line in match:
            all_words.append(line.lower())

# Creating list of unique words
unique_words_list = list(set(all_words)) 

# Creating new dictianory with unique words and their lengths 

for word in unique_words_list:
    unique_lengths[word] = len(word)

# Creating list of lengths    
    
only_lengths = list(unique_lengths.values())

# Creating dictionary whith lengths and proportions

for number in only_lengths:
    length_n_prop[number] = only_lengths.count(number)/len(only_lengths)

# Creating barplot    
    
keys = list(length_n_prop.keys())
vals = list(length_n_prop.values())

fig = sns.barplot(x = keys, y = vals)
fig.set(xlabel='Lengths of unique words', ylabel='Portion from all words');


# Задание 6

def brickify(string):
    vowels = ['а', 'у', 'о', 'и', 'э', 'ы', 'я', 'ю', 'е', 'ё']
    for letter in vowels:
        string = re.sub(f'{letter}', f'{letter}к{letter}', string)
    return string

string = input('Мяу мяу мяу')                            
brickify(string)  