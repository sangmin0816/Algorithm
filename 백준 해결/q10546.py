# 시간 초과가 날 줄 알았는데 아니였다.
# https://www.acmicpc.net/problem/10546

import sys
input = sys.stdin.readline

N = int(input())

marathoners = dict()

for i in range(N):
    name = input()
    if name in marathoners:
        marathoners[name] += 1
    else:
        marathoners[name] = 1

for i in range(N-1):
    complete = input()
    marathoners[complete] -= 1

for i in marathoners.keys():
    if marathoners[i]!=0:
        print(i.rstrip())
        break