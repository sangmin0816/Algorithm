# ['string']과 list('string')은 매우 다르다.

import sys
input = sys.stdin.readline

left = list(input().rstrip())
right = list()

M = int(input())

for m in range(M):
    op = input().rstrip()

    if op=='L':
        if left:
            right.append(left.pop())
    elif op=='D':
        if right:
            left.append(right.pop())
    elif op=='B':
        if left:
            left.pop()

    else:
        char = op[-1]
        left.append(char)

right.reverse()
string = left + right
print(''.join(string))