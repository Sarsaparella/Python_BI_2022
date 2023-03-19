Задание 1 (2 балла)
Напишите класс MyDict, который будет полностью повторять поведение обычного словаря, за исключением того, что при итерации мы должны получать и ключи, и значения.

Модули использовать нельзя

class MyDict(dict):
    
    def __iter__(self):
        return iter(self.items()) # Так можно? Вроде не сказано, что нельзя так делать...
dct = MyDict({"a": 1, "b": 2, "c": 3, "d": 25})
for key, value in dct:
    print(key, value)   
a 1
b 2
c 3
d 25
for key in dct.keys():
    print(key)
a
b
c
d
dct["c"] + dct["d"]
28
​
Задание 2 (2 балла)
Напишите функцию iter_append, которая "добавляет" новый элемент в конец итератора, возвращая итератор, который включает изначальные элементы и новый элемент. Итерироваться по итератору внутри функции нельзя, то есть вот такая штука не принимается

def iter_append(iterator, item):
    lst = list(iterator) + [item]
    return iter(lst)
Модули использовать нельзя

def iter_append(iterator, item):
    yield from iterator
    yield item
    
​
my_iterator = iter([1, 2, 3])
new_iterator = iter_append(my_iterator, 4)
​
​
for element in new_iterator:
    print(element)
1
2
3
4
Задание 3 (5 баллов)
Представим, что мы установили себе некоторую библиотеку, которая содержит в себе два класса MyString и MySet, которые являются наследниками str и set, но также несут и дополнительные методы.

Проблема заключается в том, что библиотеку писали не очень аккуратные люди, поэтому получилось так, что некоторые методы возвращают не тот тип данных, который мы ожидаем. Например, MyString().reverse() возвращает объект класса str, хотя логичнее было бы ожидать объект класса MyString.

Найдите и реализуйте удобный способ сделать так, чтобы подобные методы возвращали экземпляр текущего класса, а не родительского. При этом код методов изменять нельзя

+3 дополнительных балла за реализацию того, чтобы унаследованные от str и set методы также возвращали объект интересующего нас класса (то есть MyString.replace(..., ...) должен возвращать MyString). Переопределять методы нельзя

Модули использовать нельзя

def change_outp_class():
    def wrapp(func):
        def inner_func(*args, **kwargs):
            classname = type(args[0])
            result = func(*args, **kwargs)
            return classname(result)
        return inner_func
    return wrapp
​
​
class MyString(str):
    @change_outp_class()
    def reverse(self):
        return self[::-1]
    
    @change_outp_class()
    def make_uppercase(self):
        return "".join([chr(ord(char) - 32) if 97 <= ord(char) <= 122 else char for char in self])
    
    @change_outp_class()
    def make_lowercase(self):
        return "".join([chr(ord(char) + 32) if 65 <= ord(char) <= 90 else char for char in self])
    
    @change_outp_class()
    def capitalize_words(self):
        return " ".join([word.capitalize() for word in self.split()])
    
    
class MySet(set):
    def is_empty(self):
        return len(self) == 0
    
    def has_duplicates(self):
        return len(self) != len(set(self))
    
    @change_outp_class()
    def union_with(self, other):
        return self.union(other)
    
    def intersection_with(self, other):
        return self.intersection(other)
    
    @change_outp_class()
    def difference_with(self, other):
        return self.difference(other)
string_example = MyString("Aa Bb Cc")
set_example_1 = MySet({1, 2, 3, 4})
set_example_2 = MySet({3, 4, 5, 6, 6})
​
print(type(string_example.reverse()))
print(type(string_example.make_uppercase()))
print(type(string_example.make_lowercase()))
print(type(string_example.capitalize_words()))
print()
print(type(set_example_1.is_empty()))
print(type(set_example_2.has_duplicates()))
print(type(set_example_1.union_with(set_example_2)))
print(type(set_example_1.difference_with(set_example_2)))
<class '__main__.MyString'>
<class '__main__.MyString'>
<class '__main__.MyString'>
<class '__main__.MyString'>

<class 'bool'>
<class 'bool'>
<class '__main__.MySet'>
<class '__main__.MySet'>
​
Задание 4 (5 баллов)
Напишите декоратор switch_privacy:

Делает все публичные методы класса приватными
Делает все приватные методы класса публичными
Dunder методы и защищённые методы остаются без изменений
Должен работать тестовый код ниже, в теле класса писать код нельзя
Модули использовать нельзя

def сhange_privacy(cls):
    public_methods = [m for m in dir(cls) if not m.startswith('_')]
    private_methods = [m for m in dir(cls) if m.startswith(f'_{cls.__name__}__')]
        # print(public_methods,'\n', private_methods)
​
    for method in public_methods:
        new_name = f'_{cls.__name__}__' + method
        setattr(cls, new_name, getattr(cls, method))
        delattr(cls, method)
​
    for method in private_methods:
        new_name = method.removeprefix(f'_{cls.__name__}__')
        setattr(cls, new_name, getattr(cls, method))
        delattr(cls, method)
​
    public_methods = [m for m in dir(cls) if not m.startswith('_')]
    private_methods = [m for m in dir(cls) if m.startswith(f'_{cls.__name__}__')]
    return cls
​
​
​
@сhange_privacy
class ExampleClass:
    # Но не здесь
    def public_method(self):
        return 1
    
    def _protected_method(self):
        return 2
    
    def __private_method(self):
        return 3
    
    def __dunder_method__(self):
        pass
test_object = ExampleClass()
​
test_object._ExampleClass__public_method()   # Публичный метод стал приватным
1
test_object.private_method()   # Приватный метод стал публичным
3
test_object._protected_method()   # Защищённый метод остался защищённым
2
test_object.__dunder_method__()   # Дандер метод не изменился
hasattr(test_object, "public_method"), hasattr(test_object, "private")   # Изначальные варианты изменённых методов не сохраняются
(False, False)
​
Задание 5 (7 баллов)
Напишите контекстный менеджер OpenFasta

Контекстные менеджеры это специальные объекты, которые могут работать с конструкцией with ... as ...:. В них нет ничего сложного, для их реализации как обычно нужно только определить только пару dunder методов. Изучите этот вопрос самостоятельно

Объект должен работать как обычные файлы в питоне (наследоваться не надо, здесь лучше будет использовать композицию), но:
При итерации по объекту мы должны будем получать не строку из файла, а специальный объект FastaRecord. Он будет хранить в себе информацию о последовательности. Важно, не строки, а именно последовательности, в fasta файлах последовательность часто разбивают на много строк
Нужно написать методы read_record и read_records, которые по смыслу соответствуют readline() и readlines() в обычных файлах, но они должны выдавать не строки, а объект(ы) FastaRecord
Конструктор должен принимать один аргумент - путь к файлу
Класс должен эффективно распоряжаться памятью, с расчётом на работу с очень большими файлами
Объект FastaRecord. Это должен быть датакласс (см. про примеры декораторов в соответствующей лекции) с тремя полями:

seq - последовательность
id_ - ID последовательности (это то, что в фаста файле в строке, которая начинается с > до первого пробела. Например, >GTD326487.1 Species anonymous 24 chromosome)
description - то, что осталось после ID (Например, >GTD326487.1 Species anonymous 24 chromosome)
Напишите демонстрацию работы кода с использованием всех написанных методов, обязательно добавьте файл с тестовыми данными в репозиторий (не обязательно большой)

Можно использовать модули из стандартной библиотеки

from dataclasses import dataclass
import os
@dataclass
class FastaRecord:
    id_: str
    description: str
    seq: str
class OpenFasta:
    def __init__(self, path):
        self.path = path
        self.untouched = True # Means that file is never been read
    
    def __enter__(self):
        self.file = open(self.path, 'r')
        if self.untouched == True:
            self.last_line = next(self.file)
            self.untouched = False
            # First line of file has been read and put into self.last_line
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        
    def read_record(self):
        id_, *description = self.last_line.split(' ')
        description = ' '.join(description).replace('\n','')
        sequence = []
        for line in self.file:
            line.strip('')
            if line.startswith('>'):
                self.last_line = line 
                # Rewriting last read line only to use it for next sequence
                break
            sequence.append(line)
        seq = ''.join(sequence).replace('\n','')
        
        if seq == '':
            return None
        
        return FastaRecord(id_ = id_,
                           description = description,
                           seq = seq)
    
    def read_records(self):
        while True:
            record = self.read_record()
            if record == None:
                break
            yield record
with OpenFasta(os.path.join("data", "example.fasta")) as fasta:
    print(fasta.read_record())
    print(fasta.read_record())
    print(fasta.read_record())
    print(fasta.read_record())
​
FastaRecord(id_='>NP_990849.1', description='actin, cytoplasmic 1 [Gallus gallus]', seq='MDDDIAALVVDNGSGMCKAGFAGDDAPRAVFPSIVGRPRHQGVMVGMGQKDSYVGDEAQSKRGILTLKYPIEHGIVTNWDDMEKIWHHTFYNELRVAPEEHPVLLTEAPLNPKANREKMTQIMFETFNTPAMYVAIQAVLSLYASGRTTGIVMDSGDGVTHTVPIYEGYALPHAILRLDLAGRDLTDYLMKILTERGYSFTTTAEREIVRDIKEKLCYVALDFEQEMATAASSSSLEKSYELPDGQVITIGNERFRCPEALFQPSFLGMESCGIHETTFNSIMKCDVDIRKDLYANTVLSGGTTMYPGIADRMQKEITALAPSTMKIKIIAPPERKYSVWIGGSILASLSTFQQMWISKQEYDESGPSIVHRKCF')
FastaRecord(id_='>PSN51158.1', description='actin [Blattella germanica]', seq='MCDDDVAALVVDNGSGMCKAGFAGDDAPRAVFPSIVGRPRYQGIMVGMGQKDSYVGDEAQSKRGILTVKYPIEHGIVTNWDDMEKIWHHTFYNELRVAPEEHPVLLTEAPLNPKANREKMTQIMFETFNTPAMYVAIQAVLSLYASGRTTGIVLDSGDGVSHTVPIYEDLTDYLMKILTERGYSFTTTAEREIVRDIKEKLCYVALDFEQEMATAACPEAMFQPSFLGMESCGIHETTYNSIMKCDVDIRKDLYANTVLSGGTTMYPGIADRMQKEITALAPSTMKIKIIAPPERKYSVWIGGSILASLSTFQQMWISKQEYDESGPSIVHRKCF')
FastaRecord(id_='>OON18391.1', description='Actin [Opisthorchis viverrini]', seq='MAEDEINALVIDNGSGMCKAGFAGDDAPRAVFPSIVGRPRQPGIMIGMGQKDSYVGDEAQSKRGILTLKYPIEHGIVTNWDDMEKIWHHTFYNELRVAPEEHPVLLTEAPMNPKANRNNMAEDEINALVIDNGSGMCKAGFAGDDAPRAVFPSIVGRPRQPGIMIGMGQKDSYVGDEAQSKRGILTLKYPIEHGIVTNWDDMEKIWHHTFYNELRVAPEEHPVLLTEAPMNPKANREKMTQIMFETFNTPAMYVAIQAVLSLYASGRTTGIVLDSGDGVSHTVPIYEGYALPHAILRLDLAGRDLTDYLMKIMTERGHSFTTTAEREIVRDIKEKLCYVALDFDHEMATASESSSLEKSYELPDGQVITIGNERFRCPEAMFQPSFLGMECAGLHETAYTSIMKCDVDIRKDLYANIVLSGGSTMFPGIADRMQKEITLLTPSTMKIKIIAPPERKYSVWIGGSILASLSTFHQMWITKQEYDESGPGIVHRKCF')
FastaRecord(id_='>ETN87145.1', description='Actin [Necator americanus]', seq='MTQIMFETFNTPAMYVAIQAVLSLYASGRTTGVVLDSGDGVTHTVPIYEGYALPHAILRLDLAGRDLTDYLMKILTERGYSFTTTAEREIVRDIKEKLCYVALDFEQEMATAASSSSLEKSYELPDGQVITVGNERFRCPEALFQPSFLGMESAGIHETSYNSIMKCDIDIRKDLYANTVLSGGTTMYPGIADRMQKEITALAPSTMKIKIIAPPERKYSVWIGGSILASLSTFQQMWISKQEYDESGPSIVHRKCF')
with OpenFasta(os.path.join("data", "example.fasta")) as fasta:
    for record in fasta.read_records():
        print(record)
FastaRecord(id_='>NP_990849.1', description='actin, cytoplasmic 1 [Gallus gallus]', seq='MDDDIAALVVDNGSGMCKAGFAGDDAPRAVFPSIVGRPRHQGVMVGMGQKDSYVGDEAQSKRGILTLKYPIEHGIVTNWDDMEKIWHHTFYNELRVAPEEHPVLLTEAPLNPKANREKMTQIMFETFNTPAMYVAIQAVLSLYASGRTTGIVMDSGDGVTHTVPIYEGYALPHAILRLDLAGRDLTDYLMKILTERGYSFTTTAEREIVRDIKEKLCYVALDFEQEMATAASSSSLEKSYELPDGQVITIGNERFRCPEALFQPSFLGMESCGIHETTFNSIMKCDVDIRKDLYANTVLSGGTTMYPGIADRMQKEITALAPSTMKIKIIAPPERKYSVWIGGSILASLSTFQQMWISKQEYDESGPSIVHRKCF')
FastaRecord(id_='>PSN51158.1', description='actin [Blattella germanica]', seq='MCDDDVAALVVDNGSGMCKAGFAGDDAPRAVFPSIVGRPRYQGIMVGMGQKDSYVGDEAQSKRGILTVKYPIEHGIVTNWDDMEKIWHHTFYNELRVAPEEHPVLLTEAPLNPKANREKMTQIMFETFNTPAMYVAIQAVLSLYASGRTTGIVLDSGDGVSHTVPIYEDLTDYLMKILTERGYSFTTTAEREIVRDIKEKLCYVALDFEQEMATAACPEAMFQPSFLGMESCGIHETTYNSIMKCDVDIRKDLYANTVLSGGTTMYPGIADRMQKEITALAPSTMKIKIIAPPERKYSVWIGGSILASLSTFQQMWISKQEYDESGPSIVHRKCF')
FastaRecord(id_='>OON18391.1', description='Actin [Opisthorchis viverrini]', seq='MAEDEINALVIDNGSGMCKAGFAGDDAPRAVFPSIVGRPRQPGIMIGMGQKDSYVGDEAQSKRGILTLKYPIEHGIVTNWDDMEKIWHHTFYNELRVAPEEHPVLLTEAPMNPKANRNNMAEDEINALVIDNGSGMCKAGFAGDDAPRAVFPSIVGRPRQPGIMIGMGQKDSYVGDEAQSKRGILTLKYPIEHGIVTNWDDMEKIWHHTFYNELRVAPEEHPVLLTEAPMNPKANREKMTQIMFETFNTPAMYVAIQAVLSLYASGRTTGIVLDSGDGVSHTVPIYEGYALPHAILRLDLAGRDLTDYLMKIMTERGHSFTTTAEREIVRDIKEKLCYVALDFDHEMATASESSSLEKSYELPDGQVITIGNERFRCPEAMFQPSFLGMECAGLHETAYTSIMKCDVDIRKDLYANIVLSGGSTMFPGIADRMQKEITLLTPSTMKIKIIAPPERKYSVWIGGSILASLSTFHQMWITKQEYDESGPGIVHRKCF')
FastaRecord(id_='>ETN87145.1', description='Actin [Necator americanus]', seq='MTQIMFETFNTPAMYVAIQAVLSLYASGRTTGVVLDSGDGVTHTVPIYEGYALPHAILRLDLAGRDLTDYLMKILTERGYSFTTTAEREIVRDIKEKLCYVALDFEQEMATAASSSSLEKSYELPDGQVITVGNERFRCPEALFQPSFLGMESAGIHETSYNSIMKCDIDIRKDLYANTVLSGGTTMYPGIADRMQKEITALAPSTMKIKIIAPPERKYSVWIGGSILASLSTFQQMWISKQEYDESGPSIVHRKCF')
FastaRecord(id_='>ETN76030.1', description='Actin [Necator americanus]', seq='MRLLTSAGTLWCGGYFSAVFFYEAAYPILVFSKLQVANFHLDSCKTKKYDNGRDNACKMSVPALVSVDWLDNNKNSVTLLDATYEVQPKRNHKEFKEKHYARFEELMLEKANYTQNYSTEHIPGAVLFDVGVAYYPSQYIRYDLYPPKEFERYVKLLGVNNGDHVVVYSRGPGTGMLWAARVWWTFKVYGHNKVSVLNGGLGAWKNASKPVTSDVVVVASGNWMAKPIDKSLLITFEELDQKNSDGKSLFQDLTKINYLDARPAEVFNGTEPLGIPAEGATGAHLKGAKNVPLAKVVSEHGMKSKEEIEETLKNAGYDGSLLTVAACNGGVQASLLALALDHAGKKYRVYNECHPSEMMQIRASAYFLHKPAPYGSGLLSLHVDLRAHIQLFADIHPNCLSDTIKTQGEGNHHKHTSNNCMSMSMTKLSPLVIDSGSGMCKAGFAGDDAPRAVFPSMVGRPRHQGVMVGMGQRDSYVGSEAQSKRGILTIKYPIEHGIVTNWDDMERIWQHVFANELRVSPSQHAVLLTEAPLNPRSNREKMTQIMFESFKTPAMYVAIQAVLSLYASGRTTGVVIDSGDGVTHTVPTYEGYSLPHAVQRLDLAGRDLTNYLIKILTERGYSFTTTAEREIVRDIKEKLCYVALDFEQEMTNAENYMGTIEKNYELPDGQEITIGTERFRAPEALFQPHLLGKESSGVHENCYNSVMNCDIDIRKDLYMNIVLSGGTTMYPGITDRIKREIKLLAPSTVKVKIMAPPERKYSVWIGGSVLASLSTFQMMWITKDEYDEYGASIVHRKCF')
FastaRecord(id_='>ETN74954.1', description='Actin [Necator americanus]', seq='MEDEIAALVIDNGSGMCKAGFAGDDAPRAVFPSIVGRPRHQGVMVGMGQKDSYVGDEAQSKRGILTLKYPIEHGIVTNWDEMEKIWHHTFYNELRIAPEEHPVLLTEAPLNPKTNREKMTQIMFETFNTPAMYVNIQAVLSLYASGRTTGIVLDTGDGVTHTVPIYEVSKALHHPTGYALPHAIQRIDLAGRDLTDYMMKILTERGYTFTTTAEREIVRDIKEKLCYVALDFEQELAVAGSSSSLEKSYELPDGQVITIGNERFRCPEVLFQPAFIGMENSGIHETTYQSIMKCDVDIRKDLYSNTVLSGGTSMFPGIADRMQKEIQHLAPSTMKIKIIAPPERKYSVWIGGSILASLSTFQQLWISKQEYDESGPSIVHRKCF')