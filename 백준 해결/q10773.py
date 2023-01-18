# https://www.acmicpc.net/problem/10773

import sys
input = sys.stdin.readline

K = int(input())
account = list()

for i in range(K):
    temp = int(input())
    if temp==0:
        account.pop()
    else:
        account.append(temp)

print(sum(account))