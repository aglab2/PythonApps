import math

def findDiag(t):
    return int((math.sqrt(8*t+1))/2+0.49)

def triag(n):
    return int(n*(n+1)/2)

num = int(input())

for i in range(num):
    cur = int(input())
    n = findDiag(cur)
    t = triag(n)

    #print(n, t)
    print('TERM',cur,'IS',end=' ')
    if n%2 == 0:
        print(n-t+cur, '/' ,t-cur+1, sep='')
    else:
        print(t-cur+1, '/', n-t+cur, sep='')