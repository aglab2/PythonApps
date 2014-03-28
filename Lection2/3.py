a = int(input())

while a != 0:
    strg = input()
    gen = (strg[a*x:a*(x+1)][::1-2*(x%2)] for x in range(int(len(strg)/a)))
    strgNew = ''
    for i in gen:
        strgNew += i
    
    
    gen = (strgNew[(a*x+int(a*x/len(strgNew)))%len(strgNew)] for x in range(len(strgNew)))
    for i in gen:
        print(i, end='')
    print()
    a = int(input())