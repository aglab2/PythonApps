import itertools

num = int(input())

for i in range(num):
    gen = (a for a in itertools.count() if pow(a,3,1000)==888)
    k = int(input())

    for i in range(k-1):
        next(gen)
    
    print (next(gen))