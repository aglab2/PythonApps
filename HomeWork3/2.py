from math import sqrt

k = int(input())
for i in range(k):
    data = input().split()
    a = float(data[0])
    gna = float(data[1])
    gnb = float(data[2])
    gnc = float(data[3])
    area = (3*gna*a)/2
    b = a*gna/gnb
    c = a*gna/gnc
    r = (a*b*c)/(4*area)
    hg = (2/3)*sqrt(abs(9*r*r-(a*a + b*b + c*c)))
    print (round(area,3), round(hg,3))