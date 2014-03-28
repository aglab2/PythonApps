import sys

n = int(sys.stdin.readline())
for i in range(n):
    lSplit = sys.stdin.readline().split()
    a = int(lSplit[0])
    b = int(lSplit[1])
    print(str(a**b)[-1])