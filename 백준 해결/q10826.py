# https://www.acmicpc.net/problem/10826
# 피보나치 재귀로도 1초 미만 나오게 할 수 있나??

import sys
input = sys.stdin.readline

n = int(input())
fibonacci = [-1 for i in range(n+3)]

fibonacci[0] = 0
fibonacci[1] = 1
fibonacci[2] = 1

for i in range(3,n+1):
    fibonacci[i]=fibonacci[i-1]+fibonacci[i-2]

print(fibonacci[n])