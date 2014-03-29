print(dir(print)) #функции от функции print

def f(func,a):  
    print(func(a))


def first_decorator():
    def wraps(x):
        print('Hi dcorator!')
        return f(x)
    return wraps

@first_decorator
def inc(x):
    return x+1


def cache(user_func):
    cache = dict()
    def wrap(*args):#, **kwargs):
        if args in cache:
            return cache(args)
        else:
            result = user_func(args)
            cache[args] = result
            return result
    return wrap

#быстро чем просто функция!

@cache
def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)


from __future__ import print_function #обязательно в самом начале!
from __future__ import division

print 1,2,3,4 #python 2.6
print(3/4)    #python 3

