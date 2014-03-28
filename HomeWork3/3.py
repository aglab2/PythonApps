k = int(input())
prio = {'+':1, '-':1, '*':2, '/':2, '^':3, '(':0}

for i in range(k):
    data = input()
    stackOp = list()
    ans = ''
    for char in data:
        if char.isalpha():
            ans += char
        elif char == '(':
            stackOp.append(char)
        elif char == ')':
            curtok = stackOp.pop()
            while curtok != '(':
                ans += curtok
                curtok = stackOp.pop()
        else:
            while len(stackOp) != 0 and prio[stackOp[-1]] >= prio[char]:
                chars = stackOp.pop()
                ans += char
            stackOp.append(char)
    while len(stackOp) != 0:
        ans += stackOp.pop()
    print (ans)