k = int(input())

mp1 = {0:2, 1:3}

for i in range(k):
    listt = input().split()
    a = int(listt[0])
    b = int(listt[1]) 
    if a==b:
        if b%2==0:
            print(2*b)
        else:
            print(1+(b-1)*2)
    elif a-b == 2:
        if a%2==0:
            print(2+2*b)
        else:
            print(3+(b-1)*2)
    else:
        print('No Number')

        