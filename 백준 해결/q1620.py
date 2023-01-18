# https://www.acmicpc.net/problem/1620
# 파이썬은 역시 개사기다

import sys
input = sys.stdin.readline

N, M = map(int, input().split(' '))

encyclopedia = dict()
for i in range(N):
    encyclopedia[i+1] = input().strip()

encyclopediaR = dict(map(reversed,encyclopedia.items()))

for i in range(M):
    test = input().strip()
    if(test.isalpha()):
        print(encyclopediaR[test])
    else:
        print(encyclopedia[int(test)])