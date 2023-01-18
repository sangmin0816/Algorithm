# 파이썬 최고야
# https://www.acmicpc.net/problem/1764

import sys
input = sys.stdin.readline

N, M = map(int, input().split(' '))

hear = dict()
hearsay = list()

for i in range(N):
    hear[input().strip()]=1

for j in range(M):
    say = input().strip()
    if say in hear:
        hearsay.append(say)

print(len(hearsay))
hearsay.sort()
for i in hearsay:
    print(i)