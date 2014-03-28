from os.path import join as mjoin #склейка путей
from os import getcwd as chdir

print(mjoin('a/b/c', 'd\e\\f')) #корректность
print(mjoin('a/b', '/var', 'c\d')) #/var/c/def
print(chdir())

def f(a, *args): #несколько аргументов
    print(a, args) #args - кортеж
    
f(1)
f(2,'a', {2:3})

def f1(a, *args, b): #плохо и нельзя!
    print(1)

def f2(a, *args, b, **kw):#kw - словарь аргументов
    print(a, args, b, kw) #'b':2; 'd':3
f2(1, 'a', 'bc', b=4, d=3)

def f3():
    '''I'm a docstring'''#в переменную doc
    return 42
print(f3(), f3.__doc__)

s = "hello, {}! i'm {}"
s.capitalize() #большая первая буква
s.center(27, '$') #добивка до 27, без аргуметов пробелами
s.count('{}') #нахождение подстрок
s.endswith('{}') #заканчиватся ли строка на строку
s.find('oo') #первое вхождение, возвращает индекс или значение
s.format('world', 'string') #подстановка строки в строку
s.join(['hello', 'world']) #правильная склейка строк
s.rjust #правильное выравнивание
'QWE'.lower() #перевод в регистр
s.partition('{}') #кортеж - до.сам.после
s.replace('{}', '[]') #замена

l = ['apple', 't4e', 'appd']
l.sort()#сортировка
l.sort(key=len, reverse=True) #сортиовка по длине
l.sort(key=lambda x:x[1]) #сортировка по первому элементу  lambda - безымянные функции

f = lambda x,y,z : x+y+z

n = [1,2,3]
m = map(l, n)

#t = map(lambda x,y:'{} and {}'.format(x,y))

n = [x for x in range(10)]
l = filter(lambda x:not x%2, n)

for x in l:
    print(x)
print()

from functools import reduce
p = reduce(lambda x,y:x+y, n, -30) #-30 - начальное значение  сумма
print(p)


