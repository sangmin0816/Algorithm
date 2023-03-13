import sys
input = sys.stdin.readline

S = list(input().rstrip())
reversed_S = list()
flag = False

for s in S:
    if s=='<':
        flag = True

    if flag:
        reversed_S.append(s)
    else:
        temp.append(s)
    
    if s=='>':
        flag = False