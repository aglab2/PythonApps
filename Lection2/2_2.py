a = {0:192, 1:442, 2:692, 3:942}

def f(x):
    return a[x%4]+1000*int(x/4)
    
num = int(input())


for i in range(num):
    cur = int(input())-1
    print(f(cur))