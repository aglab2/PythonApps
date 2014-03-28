N = 1000000
input()
x = range(N) # мало памяти - генератор
input()
y = list(range(N)) # много памяти

g1 = (x**2 for x in range(25) if x%2) #генератор

print(x, end=' ') #без перевода строки
None #обозначение ничего
x.rsplit(None,1) - #массив : вся строка + последний кусокЫ

r = range(10)
for i in r:
    print(r) # 0 : 9
for i in r:
    print(r) # 0 : 9
    
r = (x**3 for x in range(10))
for i in r:
    print(r) # 0 : 81
for i in r:
    print(r) # ничего


import time

#плохо
t1 = time() #засекаем время - время в секундах
total = 0 #запись
with open("input.txt") as wwwlog: #умное открывание файла
    for line in wwwlog: #посимвольное считыание
        bytestr = line.rsplit(None,1)[1] #разбивка строки
        if bytestr != '-':
            total += int(bytestr)
t2 = time() #конец времени
#хорошо
with open("input.txt") as f:
    numbytes = (line.rsplit(None,1)[1] for line in f) #генератор строчек по очереди
    num = (int(x) for x in numbytes if x != '-') #все элементы без дефисов
    total = sum(num) #подсчет элемент в последовательности (генератор, set, list)
    
l = [x**2 for x in range(10) in x%2] #список
l = {x:x**2 for x in range(15)} #словарь



def my_function(arg1, arg2="", arg3): #функция, необязательный аргумент
    return 'Hello '+arg1, arg3 #возвращение значений    
s, s1 = my_function('world !', arg3='Yet');
print(s, s1);

import time #импортирование времени
t = time.time()
from time import time#импортирование времени и только его

import time as f#импортирование как переменная
t = f.time()

sys.path#путс системы

import imp
imp.reload(foo)#перезагрузка модуля



import os#работа с файловой системой
os.getcwd()#где находимся
os.chdir()#смена каталога
os.listdir()#файлы в каталоге
os.path.splittext('filename.ext') == '.ext'#
os.isfile() os.isdir()#что именно

f = open(a)
text = """123"""
f.write(text)
f.close()

g.read() #считывание по символам
g.read(2)


#docs.python.org - документация