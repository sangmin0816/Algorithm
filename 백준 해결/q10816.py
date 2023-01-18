# https://www.acmicpc.net/problem/10816

import sys
input = sys.stdin.readline

N = int(input())
Narr = list(map(int, input().split(' ')))
Sang = dict()
for i in Narr:
    if i not in Sang:
        Sang[i] = 0
    Sang[i] += 1

M = int(input())
Marr = list(map(int, input().split(' ')))
for i in Marr:
    if i in Sang:
        print(Sang[i], end =' ')
    else:
        print(0, end = ' ')