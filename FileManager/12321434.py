status = 1
e = 710627287
n = 832003547
x = 0

while status:
    x+=1
    num = pow(x,e,n)
    if num==2014:
        status = 0
print(x)
