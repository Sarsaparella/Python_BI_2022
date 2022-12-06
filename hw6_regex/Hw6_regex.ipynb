{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4189541e-abf5-4c3b-b681-5fb3e6340cc4",
   "metadata": {},
   "outputs": [],
   "source": [
    "OS: Ubuntu 20.04.2 LTS"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "a5646adc-d018-4b7b-b759-fc2f40f0e567",
   "metadata": {},
   "outputs": [],
   "source": [
    "import re\n",
    "import pandas as pd\n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "daf0a4d0-fa51-4043-ac9f-a66e8e57ef22",
   "metadata": {},
   "source": [
    "**1. Распарсите файл references при помощи регулярных выражений и запишите оттуда все ftp ссылки в файл ftps (5 баллов)**\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "id": "7e98d009-2ed7-4316-9166-6a8326ae4c27",
   "metadata": {
    "collapsed": true,
    "jupyter": {
     "outputs_hidden": true
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "--2022-11-15 23:15:44--  https://raw.githubusercontent.com/Serfentum/bf_course/master/15.re/references\n",
      "Распознаётся raw.githubusercontent.com (raw.githubusercontent.com)... 2606:50c0:8003::154, 2606:50c0:8000::154, 2606:50c0:8001::154, ...\n",
      "Подключение к raw.githubusercontent.com (raw.githubusercontent.com)|2606:50c0:8003::154|:443... соединение установлено.\n",
      "HTTP-запрос отправлен. Ожидание ответа... 200 OK\n",
      "Длина: 1206044 (1,1M) [text/plain]\n",
      "Сохранение в каталог: ««references»».\n",
      "\n",
      "references          100%[===================>]   1,15M  1,15MB/s    за 1,0s    \n",
      "\n",
      "2022-11-15 23:15:46 (1,15 MB/s) - «references» сохранён [1206044/1206044]\n",
      "\n"
     ]
    }
   ],
   "source": [
    "!wget https://raw.githubusercontent.com/Serfentum/bf_course/master/15.re/references"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "63969e91-62bf-449a-8ae4-75be6dd20c78",
   "metadata": {},
   "outputs": [],
   "source": [
    "with open('references') as reference:\n",
    "    with open('links_from_reference.txt', 'w') as links:\n",
    "        for line in reference.readlines():\n",
    "            match = re.findall(r'ftp\\.[./\\w#]*', line)\n",
    "            for line in match:\n",
    "                print(line, file = links, sep = '\\n')\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "39ad036b-f060-46b6-863c-3e3bc087f82a",
   "metadata": {},
   "source": [
    "**2. Извлеките из рассказа  2430 A.D. все числа  (5 баллов)**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "1028fd74-2e34-4549-8cd6-63bbf708fa29",
   "metadata": {
    "collapsed": true,
    "jupyter": {
     "outputs_hidden": true
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "--2022-11-17 19:42:55--  https://raw.githubusercontent.com/Serfentum/bf_course/master/15.re/2430AD\n",
      "Распознаётся raw.githubusercontent.com (raw.githubusercontent.com)... 2606:50c0:8001::154, 2606:50c0:8000::154, 2606:50c0:8002::154, ...\n",
      "Подключение к raw.githubusercontent.com (raw.githubusercontent.com)|2606:50c0:8001::154|:443... соединение установлено.\n",
      "HTTP-запрос отправлен. Ожидание ответа... 200 OK\n",
      "Длина: 16759 (16K) [text/plain]\n",
      "Сохранение в каталог: ««2430AD»».\n",
      "\n",
      "2430AD              100%[===================>]  16,37K  --.-KB/s    за 0,005s  \n",
      "\n",
      "2022-11-17 19:42:55 (3,13 MB/s) - «2430AD» сохранён [16759/16759]\n",
      "\n"
     ]
    }
   ],
   "source": [
    "!wget https://raw.githubusercontent.com/Serfentum/bf_course/master/15.re/2430AD"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "52691163-c06b-497e-a221-6bbe5c317785",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2430\n",
      "1969\n",
      "2430\n",
      "2430\n",
      "57\n",
      "57\n",
      "1970\n",
      "3.68\n",
      "35\n",
      "460\n",
      "2430\n"
     ]
    }
   ],
   "source": [
    "with open('2430AD') as tale:\n",
    "    for line in tale.readlines():\n",
    "        match = re.findall(r'\\d.\\d?\\d?', line)\n",
    "        for number in match:\n",
    "            print(number)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "04f24076-2b96-4737-b4ae-da4ea5cfc2d8",
   "metadata": {},
   "source": [
    "**3. Из того же рассказа извлеките все слова, в которых есть буква a, регистр при этом не важен  (5 баллов)**\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "dc9597af-9c6f-4bca-aa4a-5d5e44acf1ec",
   "metadata": {
    "collapsed": true,
    "jupyter": {
     "outputs_hidden": true
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['A', 'and', 'dawn', 'and', 'all', 'ache', 'have', 'a', 'nightmare', 'a', 'are', 'all', 'and', 'a', 'gleam', 'anywhere', 'an', 'original', 'a', 'personality', 'packed', 'talk', 'said', 'Alvarez', 'said', 'Social', 'eventually', 'An', 'character', 'escaped', 'adjustment', 'talking', 'irritates', 'past', 'tact', 'along', 'Trail', 'was', 'as', 'always', 'sparsely', 'have', 'taken', 'and', 'Alvarez', 'walking', 'Alvarez', 'was', 'tall', 'and', 'rather', 'athletic', 'a', 'muscular', 'activities', 'stairs', 'and', 'rampways', 'instance', 'almost', 'an', 'character', 'and', 'avoided', 'sunlamps', 'and', 'was', 'pale', 'said', 'want', 'can', 'have', 'square', 'space', 'and', 'has', 'apartment', 'Rather', 'a', 'a', 'way', 'said', 'Alvarez', 'And', 'a', 'Alvarez', 'added', 'matter', 'reach', 'peak', 'reach', 'reach', 'goal', 'All', 'mankind', 'And', 'said', 'at', 'that', 'way', 'that', 'against', 'plastic', 'passed', 'and', 'saw', 'distance', 'was', 'a', 'plankton', 'varieties', 'almost', 'that', 'above', 'far', 'above', 'was', 'giant', 'leading', 'sea', 'And', 'another', 'as', 'large', 'far', 'leading', 'sea', 'destination', 'was', 'a', 'back', 'that', 'thousands', 'had', 'passed', 'was', 'about', 'an', 'intangible', 'and', 'space', 'wall', 'was', 'blank', 'And', 'was', 'air', 'said', 'Alvarez', 'Inhuman', 'Literally', 'said', 'at', 'easy', 'signaled', 'waited', 'all', 'around', 'disregarded', 'manner', 'was', 'always', 'Cranwitz', 'was', 'waiting', 'same', 'all', 'gray', 'hair', 'and', 'uneasily', 'May', 'asked', 'Alvarez', 'Cranwitz', 'was', 'Cranwitz', 'and', 'sat', 'Cranwitz', 'remained', 'standing', 'and', 'said', 'Alvarez', 'said', 'ask', 'capacity', 'as', 'Representative', 'as', 'Representative', 'are', 'ready', 'social', 'Cranwitz', 'finally', 'was', 'and', 'had', 'clear', 'throat', 'want', 'said', 'have', 'a', 'contract', 'standing', 'family', 'has', 'always', 'had', 'all', 'and', 'said', 'irritably', 'asking', 'accede', 'voluntarily', 'Alvarez', 'understand', 'situation', 'what', 'was', 'father', 'really', 'what', 'was', 'last', 'year', 'Cranwitz', 'jaw', 'that', 'rate', 'has', 'year', 'amount', 'and', 'has', 'changed', 'That', 'year', 'year', 'year', 'carry', 'Alvarez', 'was', 'year', 'was', 'and', 'said', 'year', 'reached', 'goal', 'rate', 'exactly', 'matches', 'death', 'rate', 'population', 'exactly', 'steady', 'replacement', 'and', 'sea', 'farms', 'are', 'a', 'steady', 'state', 'stand', 'all', 'mankind', 'and', 'Because', 'a', 'Because', 'a', 'And', 'creatures', 'Guinea', 'Rabbits', 'and', 'lizards', 'haven', 'taken', 'a', 'all', 'What', 'harm', 'What', 'demanded', 'Cranwitz', 'said', 'at', 'was', 'a', 'Alvarez', 'had', 'heard', 'that', 'said', 'as', 'sympathy', 'as', 'and', 'a', 'certain', 'amount', 'real', 'sympathy', 'was', 'a', 'ago', 'vast', 'care', 'And', 'years', 'that', 'dinosaurs', 'have', 'man', 'ignorant', 'can', 'compare', 'real', 'asked', 'Cranwitz', 'was', 'larger', 'said', 'Cranwitz', 'Year', 'year', 'had', 'many', 'All', 'large', 'animals', 'All', 'carnivores', 'small', 'plants', 'creatures', 'Alvarez', 'said', 'What', 'wants', 'Mankind', 'against', 'Social', 'persuade', 'against', 'real', 'resistance', 'want', 'really', 'are', 'What', 'Alvarez', 'was', 'insinuating', 'Cranwitz', 'sat', 'A', 'certain', 'Someday', 'reach', 'Mankind', 'want', 'animals', 'want', 'start', 'a', 'variety', 'faded', 'stare', 'said', 'What', 'are', 'reached', 'said', 'Cranwitz', 'and', 'established', 'a', 'and', 'abandoned', 'all', 'solar', 'capable', 'human', 'Cranwitz', 'said', 'are', 'stars', 'Earthlike', 'Alvarez', 'head', 'reach', 'have', 'finally', 'Earth', 'and', 'human', 'have', 'made', 'and', 'Earth', 'margin', 'a', 'starship', 'capable', 'years', 'space', 'Have', 'wasn', 'last', 'said', 'Cranwitz', 'was', 'said', 'Alvarez', 'haven', 'romanticized', 'madness', 'was', 'a', 'and', 'was', 'and', 'reason', 'than', 'half', 'substance', 'war', 'and', 'preparations', 'war', 'ran', 'wasted', 'and', 'at', 'chance', 'and', 'tolerated', 'deviants', 'all', 'dreaded', 'what', 'called', 'population', 'and', 'dreamed', 'reaching', 'as', 'a', 'escape', 'combination', 'and', 'advances', 'that', 'changed', 'case', 'are', 'was', 'establishment', 'a', 'and', 'art', 'planetary', 'peace', 'and', 'a', 'placid', 'humanity', 'peacefully', 'and', 'multiplication', 'was', 'advance', 'exactly', 'many', 'Earth', 'many', 'calories', 'reached', 'Earth', 'and', 'that', 'many', 'carbon', 'plants', 'each', 'year', 'and', 'many', 'animal', 'plants', 'Earth', 'animal', 'Cranwitz', 'finally', 'And', 'all', 'human', 'Exactly', 'meant', 'all', 'animal', 'That', 'way', 'said', 'angrily', 'Alvarez', 'again', 'Cranwitz', 'said', 'replaced', 'placoderms', 'had', 'replaced', 'replaced', 'amphibians', 'and', 'replaced', 'mammals', 'at', 'last', 'has', 'reached', 'peak', 'Earth', 'bears', 'population', 'human', 'demanded', 'Cranwitz', 'vast', 'all', 'face', 'land', 'plants', 'and', 'animals', 'what', 'have', 'And', 'all', 'uninhabited', 'ocean', 'has', 'a', 'plankton', 'plankton', 'harvest', 'and', 'as', 'organic', 'matter', 'plankton', 'said', 'Alvarez', 'war', 'are', 'regulated', 'deaths', 'are', 'peaceful', 'infants', 'are', 'genetically', 'adjusted', 'and', 'Earth', 'are', 'normal', 'brain', 'largest', 'conceivable', 'quantity', 'conceivable', 'matter', 'And', 'all', 'that', 'brain', 'what', 'heaved', 'an', 'audible', 'exasperation', 'Alvarez', 'calm', 'said', 'destination', 'Perhaps', 'animals', 'Earth', 'was', 'was', 'necessary', 'and', 'take', 'chances', 'was', 'wasteful', 'Earth', 'was', 'had', 'and', 'had', 'after', 'mankind', 'came', 'had', 'learn', 'way', 'was', 'learning', 'had', 'take', 'chances', 'attempt', 'mad', 'mankind', 'has', 'have', 'planet', 'and', 'Alvarez', 'paused', 'that', 'said', 'want', 'Cranwitz', 'wants', 'generation', 'that', 'has', 'reached', 'and', 'want', 'having', 'reached', 'animals', 'are', 'way', 'Cranwitz', 'head', 'take', 'all', 'have', 'what', 'human', 'said', 'human', 'another', 'human', 'brain', 'what', 'measure', 'can', 'evaluate', 'human', 'brain', 'already', 'have', 'said', 'Alvarez', 'and', 'that', 'and', 'are', 'All', 'Earth', 'prepared', 'celebrate', 'year', 'AD', 'year', 'that', 'planet', 'at', 'last', 'goal', 'achieved', 'all', 'Shall', 'fan', 'a', 'flaw', 'a', 'flaw', 'Cranwitz', 'Earth', 'has', 'waiting', 'years', 'wait', 'cannot', 'and', 'voluntarily', 'a', 'said', 'all', 'say', 'that', 'Cranwitz', 'acted', 'and', 'that', 'act', 'was', 'reached', 'And', 'Cranwitz', 'said', 'imitating', 'And', 'say', 'that', 'Alvarez', 'and', 'persuaded', 'said', 'Alvarez', 'audible', 'annoyance', 'Cranwitz', 'can', 'against', 'Whatever', 'and', 'that', 'way', 'are', 'an', 'idealist', 'can', 'that', 'last', 'many', 'Cranwitz', 'and', 'Alvarez', 'hand', 'waved', 'and', 'said', 'a', 'remained', 'Cranwitz', 'Can', 'have', 'day', 'animals', 'And', 'And', 'stand', 'mankind', 'and', 'And', 'Alvarez', 'said', 'And', 'and', 'vast', 'continental', 'human', 'placidly', 'human', 'placidly', 'ate', 'half', 'a', 'carefully', 'made', 'talked', 'heat', 'ran', 'machinery', 'organized', 'libraries', 'amused', 'and', 'varied', 'machinery', 'repaired', 'plankton', 'planetary', 'ocean', 'basked', 'and', 'and', 'and', 'and', 'and', 'transferred', 'and', 'that', 'And', 'human', 'wastes', 'gathered', 'and', 'irradiated', 'and', 'and', 'human', 'and', 'treated', 'and', 'and', 'was', 'back', 'ocean', 'And', 'all', 'was', 'as', 'had', 'decades', 'and', 'millennia', 'Cranwitz', 'creatures', 'a', 'last', 'guinea', 'a', 'gaze', 'a', 'blade', 'grass', 'all', 'last', 'Earth', 'that', 'humans', 'humans', 'and', 'seared', 'plants', 'and', 'cages', 'and', 'animals', 'appropriate', 'vapors', 'and', 'and', 'last', 'was', 'and', 'mankind', 'and', 'was', 'Cranwitz', 'departed', 'Cranwitz', 'also', 'vapors', 'and', 'want', 'And', 'after', 'that', 'was', 'really', 'all', 'Earth', 'all', 'inhabitants', 'and', 'all', 'human', 'brain', 'was', 'Cranwitz', 'unusual', 'idea', 'universal', 'placidity', 'that', 'meant', 'that', 'had', 'at', 'last', 'achieved', 'A', 'was', 'and', 'had', 'paid', 'fears', 'unallayed', 'That', 'had', 'accepted', 'was', 'had', 'taken', 'was', 'GREATEST', 'ASSET', 'Campbell', 'same', 'again', 'years', 'and', 'Magazine', 'said', 'was', 'handing', 'that', 'had', 'at', 'a', 'and', 'said', 'necessarily', 'agree', 'another', 'read', 'and', 'hadn', 'about', 'crazy', 'about', 'unable', 'because', 'was', 'ashamed', 'and', 'was', 'great', 'man', 'feared', 'as', 'jackass', 'taking', 'that', 'had', 'added', 'favor', 'many', 'many', 'had', 'And', 'case', 'as', 'that', 'years', 'have', 'far', 'than', 'years', 'stayed', 'and', 'that', 'population', 'Earth', 'estimated', 'rate', 'increase', 'that', 'population', 'years', 'rate', 'Increase', 'can', 'maintained', 'years', 'year', 'A', 'human', 'and', 'equal', 'total', 'animal', 'Earth', 'that', 'above']\n"
     ]
    }
   ],
   "source": [
    "words = []\n",
    "with open('2430AD') as tale:\n",
    "    for line in tale.readlines():\n",
    "        match = re.findall(r\"[A-Za-z]*[aA][A-Za-z]*\", line)\n",
    "        for line in match:\n",
    "            words.append(line)\n",
    "print(words)\n",
    "# len(words)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d35f400e-ca91-4dec-b938-c794843deb20",
   "metadata": {},
   "source": [
    "**4. Извлеките из рассказа все восклицательные предложения  (5 баллов)**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "71c8815b-ca1d-4f4e-8ab5-9477302a0392",
   "metadata": {
    "collapsed": true,
    "jupyter": {
     "outputs_hidden": true
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Yes!', 'Literally!', ' There was once a time!', ' Centuries ago!', ' Cranwitz!', 'If we succeed!']\n"
     ]
    }
   ],
   "source": [
    "exclamation = []\n",
    "with open('2430AD') as tale:\n",
    "    for line in tale.readlines():\n",
    "        match = re.findall(r\"[A-Za-z ]*!\", line)\n",
    "        for line in match:\n",
    "            exclamation.append(line)\n",
    "            \n",
    "print(exclamation)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d91cb64b-f7aa-4c4e-9307-8ddfe16630a2",
   "metadata": {},
   "source": [
    "**5. Постройте гистограмму распределения длин уникальных слов (без учёта регистра, длина от 1) в тексте.   (5 баллов)**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "cc20804e-2702-40de-9af7-7d35ce1ffa88",
   "metadata": {
    "collapsed": true,
    "jupyter": {
     "outputs_hidden": true
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "unique_lengths = {}\n",
    "unique_words_list = []\n",
    "all_words = []\n",
    "length_n_prop = {}\n",
    "\n",
    "# Creating list will all words\n",
    "\n",
    "with open('2430AD') as tale:\n",
    "    for line in tale.readlines():\n",
    "        match = re.findall(r\"[\\w'-]*\", line)\n",
    "        for line in match:\n",
    "            all_words.append(line.lower())\n",
    "\n",
    "# Creating list of unique words\n",
    "unique_words_list = list(set(all_words)) \n",
    "\n",
    "# Creating new dictianory with unique words and their lengths \n",
    "\n",
    "for word in unique_words_list:\n",
    "    unique_lengths[word] = len(word)\n",
    "\n",
    "# Creating list of lengths    \n",
    "    \n",
    "only_lengths = list(unique_lengths.values())\n",
    "\n",
    "# Creating dictionary whith lengths and proportions\n",
    "\n",
    "for number in only_lengths:\n",
    "    length_n_prop[number] = only_lengths.count(number)/len(only_lengths)\n",
    "\n",
    "# Creating barplot    \n",
    "    \n",
    "keys = list(length_n_prop.keys())\n",
    "vals = list(length_n_prop.values())\n",
    "\n",
    "fig = sns.barplot(x = keys, y = vals)\n",
    "fig.set(xlabel='Lengths of unique words', ylabel='Portion from all words');"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6d1b474b-0897-4072-a614-46b7e0692973",
   "metadata": {},
   "source": [
    "**6. Сделайте функцию-переводчик с русского на \"кирпичный язык\" (5 баллов)**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "0863c0df-4648-427e-a523-adbe81a7a1c9",
   "metadata": {
    "collapsed": true,
    "jupyter": {
     "outputs_hidden": true
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Мяу мяу мяу аэродоставка чайного гриба в саратов\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "'акаэкэрокодокостакавкака чакайнокогоко грикибака в сакаракатоков'"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def brickify(string):\n",
    "    vowels = ['а', 'у', 'о', 'и', 'э', 'ы', 'я', 'ю', 'е', 'ё']\n",
    "    for letter in vowels:\n",
    "        string = re.sub(f'{letter}', f'{letter}к{letter}', string)\n",
    "    return string\n",
    "\n",
    "string = input('Мяу мяу мяу')                            \n",
    "brickify(string)                          "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
