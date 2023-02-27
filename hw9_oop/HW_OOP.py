Задание 1 (5 баллов)
Напишите классы Chat, Message и User. Они должны соответствовать следующим требованиям:

Chat:

Должен иметь атрибут chat_history, где будут храниться все сообщения (Message) в обратном хронологическом порядке (сначала новые, затем старые)
Должен иметь метод show_last_message, выводящий на экран информацию о последнем сообщении
Должен иметь метод get_history_from_time_period, который принимает два опциональных аргумента (даты с которой и по какую мы ищем сообщения и выдаём их). Метод также должен возвращать объект типа Chat
Должен иметь метод show_chat, выводящий на экран все сообщения (каждое сообщение в таком же виде как и show_last_message, но с разделителем между ними)
Должен иметь метод recieve, который будет принимать сообщение и добавлять его в чат
Message:

Должен иметь три обязательных атрибута
text - текст сообщения
datetime - дата и время сообщения (встроенный модуль datetime вам в помощь). Важно! Это должна быть не дата создания сообщения, а дата его попадания в чат!
user - информация о пользователе, который оставил сообщение (какой тип данных использовать здесь, разберётесь сами)
Должен иметь метод show, который печатает или возвращает информацию о сообщении с необходимой информацией (дата, время, юзер, текст)
Должен иметь метод send, который будет отправлять сообщение в чат
User:

Класс с информацией о юзере, наполнение для этого класса придумайте сами
Напишите несколько примеров использования кода, которое показывает взаимодействие между объектами.

В тексте задания намерено не указано, какие аргументы должны принимать методы, пускай вам в этом поможет здравый смысл)

В этом задании не стоит флексить всякими продвинутыми штуками, для этого есть последующие

В этом задании можно использовать только модуль datetime

from datetime import datetime
import time
​
class Chat:
    def __init__(self):
        self.chat_history = []
        
    def show_last_message(self):
        last_message = self.chat_history[0]
        last_message.show()
    
    def get_history_from_time_period(self, after = datetime(2000, 1, 1, 1, 1, 1),
                                     before = datetime(2099, 1, 1, 1, 1, 1)):
        selected_messages = Chat()
        for message in self.chat_history:
            if message.datetime > after and message.datetime < before:
                selected_messages.recieve(message)
        return selected_messages.show_chat()
    
    def show_chat(self):
        for message in self.chat_history:
            message.show()
    
    def recieve(self, new_message):
        new_message.datetime = datetime.now()
        self.chat_history.insert(0, new_message)
        time.sleep(5) # Сон 5 секунд чтобы потом можно было взять временной промежуток в get_history_from_time_period
        return self.chat_history 
        
class Message:
    def __init__(self, user, message):
        self.text = message
        self.user = user.nickname
        self.pronouns = user.pronouns
        self.datetime = None
    
    def show(self):
        info = f'''
        From: {self.user}
        Message: {self.text}
        Date and time: {self.datetime}'''
        print(info)
    
    def send(self, chat):
        chat.recieve(self)
        
class User:
    def __init__(self, nickname, kaomoji, pronouns):
        self.nickname = kaomoji + nickname + kaomoji
        self.pronouns = pronouns
    def __repr__(self):
        return f'Nickname:{self.nickname}, pronouns: {self.pronouns}.'
dio = User(' ＤＩＯ ', '🦇', 'he/him')
jojo = User(' ＪｏＪｏ ', '⭐', 'he/him')
​
m1 = Message(dio, "Oh? You're approaching me? Instead of running away, you're coming right to me?")
m2 = Message(jojo, "I can't beat the shit out of you without getting closer")
m3 = Message(dio, "Oh ho!~ Then come as close as you like")
m4 = Message(jojo, "Yare yare daze...")
m5 = Message(jojo, "Ora!Ora!Ora!Ora!")
m6 = Message(dio, "Too slow, too slow! The World is the ultimate Stand. Even without his power to stop time, his speed and power far exceed that of your Star Platinum.")
​
battle = Chat()
dio
Nickname:🦇 ＤＩＯ 🦇, pronouns: he/him.
m2.show()

        From: ⭐ ＪｏＪｏ ⭐
        Message: I can't beat the shit out of you without getting closer
        Date and time: None
m1.send(battle)
m2.send(battle)
battle.show_chat()

        From: ⭐ ＪｏＪｏ ⭐
        Message: I can't beat the shit out of you without getting closer
        Date and time: 2023-02-24 14:35:30.753319

        From: 🦇 ＤＩＯ 🦇
        Message: Oh? You're approaching me? Instead of running away, you're coming right to me?
        Date and time: 2023-02-24 14:35:25.751524
m3.send(battle)
m4.send(battle)
m5.send(battle)
m6.send(battle)
m5.send(battle)
battle.show_chat()

        From: ⭐ ＪｏＪｏ ⭐
        Message: Ora!Ora!Ora!Ora!
        Date and time: 2023-02-24 14:35:55.801231

        From: 🦇 ＤＩＯ 🦇
        Message: Too slow, too slow! The World is the ultimate Stand. Even without his power to stop time, his speed and power far exceed that of your Star Platinum.
        Date and time: 2023-02-24 14:35:50.797180

        From: ⭐ ＪｏＪｏ ⭐
        Message: Ora!Ora!Ora!Ora!
        Date and time: 2023-02-24 14:35:55.801231

        From: ⭐ ＪｏＪｏ ⭐
        Message: Yare yare daze...
        Date and time: 2023-02-24 14:35:40.789306

        From: 🦇 ＤＩＯ 🦇
        Message: Oh ho!~ Then come as close as you like
        Date and time: 2023-02-24 14:35:35.784470

        From: ⭐ ＪｏＪｏ ⭐
        Message: I can't beat the shit out of you without getting closer
        Date and time: 2023-02-24 14:35:30.753319

        From: 🦇 ＤＩＯ 🦇
        Message: Oh? You're approaching me? Instead of running away, you're coming right to me?
        Date and time: 2023-02-24 14:35:25.751524
battle.get_history_from_time_period(after = datetime(2023, 2, 24, 14, 35, 29),
                                    before = datetime(2023, 2, 24, 14, 35, 40))

        From: ⭐ ＪｏＪｏ ⭐
        Message: I can't beat the shit out of you without getting closer
        Date and time: 2023-02-24 14:36:36.080990

        From: 🦇 ＤＩＯ 🦇
        Message: Oh ho!~ Then come as close as you like
        Date and time: 2023-02-24 14:36:31.078827
​
Задание 2 (3 балла)
В питоне как-то слишком типично и неинтересно происходят вызовы функций. Напишите класс Args, который будет хранить в себе аргументы, а функции можно будет вызывать при помощи следующего синтаксиса.

Использовать любые модули нельзя, да и вряд-ли это как-то поможет)

class Args:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
    
    def __rlshift__(self, function):
        return function(*self.args, **self.kwargs)
sum << Args([1, 2])
3
(lambda a, b, c: a**2 + b + c) << Args(1, 2, c=50)
53
Задание 3 (5 баллов)
Сделайте класс наследник float. Он должен вести себя как float, но также должен обладать некоторыми особенностями:

При получении атрибутов формата <действие>_<число> мы получаем результат такого действия над нашим числом
Создавать данные атрибуты в явном виде, очевидно, не стоит
Подсказка: если в процессе гуглёжки, вы выйдете на такую тему как "Дескрипторы", то это НЕ то, что вам сейчас нужно

Примеры использования ниже

class StrangeFloat(float):
    def __init__(self, number):
        self.number = number
        super().__init__()
        
    def __getattr__(self, item):
        function, number2 = item.split('_')
        if function == 'add':
            return StrangeFloat(self.number + float(number2))
        if function == 'subtract':
            return StrangeFloat(self.number - float(number2))
        if function == 'multiply':
            return StrangeFloat(self.number * float(number2))
        if function == 'divide':
            return StrangeFloat(self.number / float(number2))
number = StrangeFloat(3.5)
number.add_1
4.5
number.subtract_20
-16.5
number.multiply_5
17.5
number.divide_25
0.14
number.add_1.add_2.multiply_6.divide_8.subtract_9
-4.125
getattr(number, "add_-2.5")   # Используем getattr, так как не можем написать number.add_-2.5 - это SyntaxError
1.0
number + 8   # Стандартные для float операции работают также
11.5
number.as_integer_ratio()   # Стандартные для float операции работают также  (это встроенный метод float, писать его НЕ НАДО)
(7, 2)
Задание 4 (3 балла)
В данном задании мы немного отдохнём и повеселимся. От вас требуется заменить в данном коде максимально возможное количество синтаксических конструкций на вызовы dunder методов, dunder атрибутов и dunder переменных.

Маленькая заметка: полностью всё заменить невозможно. Например, function() можно записать как function.__call__(), но при этом мы всё ещё не избавляемся от скобочек, так что можно делать так до бесконечности function.__call__.__call__.__call__.__call__.....__call__() и при всём при этом мы ещё не избавляемся от . для доступа к атрибутам. В общем, замените всё, что получится, не закапываясь в повторы, как в приведённом примере. Чем больше разных методов вы найдёте и используете, тем лучше и тем выше будет балл

Код по итогу дожен работать и печатать число 4420.0, как в примере. Структуру кода менять нельзя, просто изменяем конструкции на синонимичные

И ещё маленькая подсказка. Заменить здесь можно всё кроме:

Конструкции for ... in ...:
Синтаксиса создания лямбда функции
Оператора присваивания =
Конструкции if-else
dir(matrix)
import numpy as np
​
​
matrix = list.__call__()
for idx in range(0, 100, 10):
    matrix.__iadd__([list.__call__(range(idx, idx.__add__(10)))])
    
selected_columns_indices = list.__call__(filter(lambda x: x in range(1, 5, 2), range(matrix.__len__())))
selected_columns = map(lambda x: [x.__getitem__(col) for col in selected_columns_indices], matrix)
​
arr = np.array(list.__call__(selected_columns))
​
mask = (arr.__getitem__((slice.__call__(None), 1)) % 3).__eq__(0)
new_arr = arr.__getitem__(mask)
​
product = new_arr.__matmul__(new_arr.T)
​
if (product.__getitem__(0).__lt__(1000)).all().__and__((product.__getitem__(2).__gt__(1000)).any()):
    print(product.mean())
4420.0
​
import numpy as np
​
​
matrix = []
for idx in range(0, 100, 10):
    matrix += [list(range(idx, idx + 10))]
    
selected_columns_indices = list(filter(lambda x: x in range(1, 5, 2), range(len(matrix))))
selected_columns = map(lambda x: [x[col] for col in selected_columns_indices], matrix)
​
arr = np.array(list(selected_columns))
​
mask = arr[:, 1] % 3 == 0
new_arr = arr[mask]
​
product = new_arr @ new_arr.T
​
if (product[0] < 1000).all() and (product[2] > 1000).any():
    print(product.mean())
4420.0
Задание 5 (10 баллов)
Напишите абстрактный класс BiologicalSequence, который задаёт следующий интерфейс:

Работа с функцией len
Возможность получать элементы по индексу и делать срезы последовательности (аналогично строкам)
Вывод на печать в удобном виде и возможность конвертации в строку
Возможность проверить алфавит последовательности на корректность
Напишите класс NucleicAcidSequence:

Данный класс реализует интерфейс BiologicalSequence
Данный класс имеет новый метод complement, возвращающий комплементарную последовательность
Данный класс имеет новый метод gc_content, возвращающий GC-состав (без разницы, в процентах или в долях)
Напишите классы наследники NucleicAcidSequence: DNASequence и RNASequence

DNASequence должен иметь метод transcribe, возвращающий транскрибированную РНК-последовательность
Данные классы не должны иметь публичных методов complement и метода для проверки алфавита, так как они уже должны быть реализованы в NucleicAcidSequence.
Напишите класс AminoAcidSequence:

Данный класс реализует интерфейс BiologicalSequence
Добавьте этому классу один любой метод, подходящий по смыслу к аминокислотной последовательности. Например, метод для нахождения изоэлектрической точки, молекулярного веса и т.д.
Комментарий по поводу метода NucleicAcidSequence.complement, так как я хочу, чтобы вы сделали его опредедённым образом:

При вызове dna.complement() или условного dna.check_alphabet() должны будут вызываться соответствующие методы из NucleicAcidSequence. При этом, данный метод должен обладать свойством полиморфизма, иначе говоря, внутри complement не надо делать условия а-ля if seuqence_type == "DNA": return self.complement_dna(), это крайне не гибко. Данный метод должен опираться на какой-то общий интерфейс между ДНК и РНК. Создание экземпляров NucleicAcidSequence не подразумевается, поэтому код NucleicAcidSequence("ATGC").complement() не обязан работать, а в идеале должен кидать исключение NotImplementedError при вызове от экземпляра NucleicAcidSequence

Вся сложность задания в том, чтобы правильно организовать код. Если у вас есть повторяющийся код в сестринских классах или родительском и дочернем, значит вы что-то делаете не так.

Маленькое замечание: По-хорошему, между классом BiologicalSequence и классами NucleicAcidSequence и AminoAcidSequence, ещё должен быть класс-прослойка, частично реализующий интерфейс BiologicalSequence, но его писать не обязательно, так как задание и так довольно большое (правда из-за этого у вас неминуемо возникнет повторяющийся код в классах NucleicAcidSequence и AminoAcidSequence)

from abc import ABC, abstractmethod
​
class BiologicalSequence(ABC):
    @abstractmethod
    def __len__(self):
        pass
    
    @abstractmethod
    def __str__(self):
        pass
    
    @abstractmethod
    def __getitem__(self, item):
        pass
    
    @abstractmethod
    def alphabet_check(self):
        pass
    
class NucleicAcidSequence(BiologicalSequence):
    def __init__(self, sequence):
        self.sequence = sequence
        self.allowed = None 
        self.complement_dict = None
        
    def __len__(self):
        return len(self.sequence)
    
    def __str__(self):
        return str(self.sequence)
    
    def __getitem__(self, slc):
        return self.sequence[slc]
    
    def alphabet_check(self):
        if self.allowed == None:
            raise NotImplementedError
        else:
            alphabet = set(self.sequence)
            if alphabet.issubset(self.allowed):
                return 'Good alphabet'
            else:
                raise ValueError('Wrong alphabet')
        
    def complement(self):
        if self.complement == None:
            raise NotImplementedError
        else:
            self.complemented = []
            for letter in self.sequence:
                self.complemented.append(self.complement_dict[letter])
        return ''.join(self.complemented)
            
    
class DNASequence(NucleicAcidSequence):
    def __init__(self, sequence):
        super().__init__(sequence)
        self.allowed = {'A', 'T', 'G', 'C'}
        self.complement_dict = {'A':'T', 'T':'A',
                                'G':'C', 'C':'G'}
    
    def transcribe(self):
        return self.sequence.replace('T', 'U')
​
​
class RNASequence(NucleicAcidSequence):
    def __init__(self, sequence):
        super.__init__(sequence)
        self.allowed = {'A', 'C', 'G', 'U'}
        self.complement_dict = {'A':'U', 'U':'A',
                                'G':'C', 'C':'G'}
        
class AminoAcidSequence(BiologicalSequence):
    def __init__(self, sequence):
        self.sequence = sequence
        self.allowed = {'A', 'R', 'N', 'D',
                        'C', 'Q', 'E', 'G',
                        'H', 'I', 'L', 'K',
                        'M', 'F', 'P', 'S',
                        'T', 'W', 'Y', 'V'}
​
        self.composition = {'A': 0, 'R': 0, 'N': 0, 'D': 0,
                            'C': 0, 'Q': 0, 'E': 0, 'G': 0,
                            'H': 0, 'I': 0, 'L': 0, 'K': 0,
                            'M': 0, 'F': 0, 'P': 0, 'S': 0,
                            'T': 0, 'W': 0, 'Y': 0, 'V': 0}
    def __len__(self):
        return len(self.sequence)
    
    def __str__(self):
        return str(self.sequence)
    
    def __getitem__(self, slc):
        return self.sequence[slc]
    
    def alphabet_check(self):
        alphabet = set(self.sequence)
        if alphabet.issubset(self.allowed):
            return 'Good alphabet'
        else:
            raise ValueError('Wrong alphabet')
    
    def count_composition(self):
        for am_acid in self.sequence:
            self.composition[am_acid] += 1
        for am_acid in self.composition:
            self.composition[am_acid] =  round(self.composition[am_acid] * 100 / len(self.sequence), 2)
​
        return self.composition
    
    
# Не сделала класс-прослойку и код повторяется, ам сорри, я устал( очень сложно далось осознать даже это все
seq_fna = DNASequence('ATGCTGTGTCTCTCA')
seq_fna2 = NucleicAcidSequence('ATGCTGTGTCTCTCA')
seq_fna.alphabet_check()
'Good alphabet'
seq_fna.transcribe()
'AUGCUGUGUCUCUCA'
seq_fna2.alphabet_check()
---------------------------------------------------------------------------
NotImplementedError                       Traceback (most recent call last)
Cell In[68], line 1
----> 1 seq_fna2.alphabet_check()

Cell In[64], line 18, in NucleicAcidSequence.alphabet_check(self)
     16 def alphabet_check(self):
     17     if self.allowed == None:
---> 18         raise NotImplementedError
     19     else:
     20         alphabet = set(self.sequence)

NotImplementedError: 
seq_faa = AminoAcidSequence('MGDEDVAALVVDNGSGMCKAGFAGDDAPRAV')
seq_faa.alphabet_check()
'Good alphabet'
seq_faa.count_composition()
{'A': 19.35,
 'R': 3.23,
 'N': 3.23,
 'D': 16.13,
 'C': 3.23,
 'Q': 0.0,
 'E': 3.23,
 'G': 16.13,
 'H': 0.0,
 'I': 0.0,
 'L': 3.23,
 'K': 3.23,
 'M': 6.45,
 'F': 3.23,
 'P': 3.23,
 'S': 3.23,
 'T': 0.0,
 'W': 0.0,
 'Y': 0.0,
 'V': 12.9}
​
​
​

