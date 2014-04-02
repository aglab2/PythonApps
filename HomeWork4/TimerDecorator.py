from time import time

def TimerDecorator(f):
    def wrap(*args, **kwargs):
        t1 = time()
        return (f(*args, **kwargs), time() - t1)
    return wrap




@TimerDecorator
def summer(n):
    t=0
    for i in range(n):
        t+=i 

print(summer(10000000))