import sys
input = sys.stdin.readline

S = list(input().rstrip())
S.append(' ')

RS = list()
flag = False
temp = list()

for s in S:
    if s=='<':
        flag = True
        while temp:
            RS.append(temp.pop())
    
    if flag:
        RS.append(s)
    elif s==' ':
        while temp:
            RS.append(temp.pop())
        RS.append(s)
    else:
        temp.append(s)
    
    if s=='>':
        flag = False

RS.pop()
print(''.join(RS))