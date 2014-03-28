import sys

for line in sys.stdin:
    intArr = list(map(int, line.split()))
    if intArr[0]==0 and intArr[1]==0 and intArr[2]==0:
        break
    if intArr[1]*2 == intArr[0]+intArr[2]:
        print('AP ', intArr[2]*2 - intArr[1])
    if intArr[1]**2 == intArr[0]*intArr[2]:
        print('GP', (int)(intArr[2]**2/intArr[1]))