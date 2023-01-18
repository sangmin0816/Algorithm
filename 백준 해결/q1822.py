# https://www.acmicpc.net/problem/1822
# 오랜만에 set 복습

import sys
input = sys.stdin.readline

A, B = map(int, input().split(' '))

Aset = set(map(int, input().split(' ')))
Bset = set(map(int, input().split(' ')))

Dset = list(Aset - Bset)
print(len(Dset))
if(len(Dset)):
    Dset.sort()
    for i in Dset:
        print(i, end=' ')